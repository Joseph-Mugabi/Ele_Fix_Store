#!/usr/bin/python3
"""populate the view"""

import models
from flask import Flask, jsonify, request, render_template, session, redirect, url_for, flash
from models import storage
from models.users import User
from sqlalchemy.orm.exc import NoResultFound
from models.customers import Customer
from models.items import Item
from models.base_model import BaseModel
from models.payments import Payment
from models.services import Service
from models.messages import Message
from models.procurements import Procurement
import random
from flask_mail import Mail, Message
import requests
from datetime import datetime, timedelta, timezone
from itsdangerous import URLSafeTimedSerializer
from werkzeug.datastructures import MultiDict
import pytz
import secrets
from functools import wraps
from flask_socketio import SocketIO, send 
from api.v1.auth import Auth
from werkzeug.security import generate_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required


app = Flask(__name__)
app.debug = True
app.secret_key = secrets.token_hex(32)
app.config["SECRET_KEY"] = secrets.token_hex(32)
socketio = SocketIO(app, cors_allowed_origins="*")
Auth = Auth()
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mugabijoshgreen@gmail.com'
app.config['MAIL_PASSWORD'] = 'Dr.josegreen'
app.config['MAIL_DEFAULT_SENDER'] = 'mugabijoshgreen@gmail.com'

login_manager = LoginManager(app)
login_manager.init_app(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
mail = Mail(app)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("login"))

@login_manager.user_loader
def load_user(user_id):
    """load user frm e db based on user id, retrn usr objct or none"""
    return models.storage.search_one("User", id=user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """user login"""
    if request.method == 'POST':
        models.storage.save()
        email = request.form["email"]
        password = request.form["password"]

        # check validaty email, passwrd against usr's credentials on db
        user = models.storage.search_one("User", email=email)
        if user and user.check_password(password):  #  login user
            login_user(user)
            return redirect(url_for("all_customers"))
        else:
            flash("Invalid email or password")
            return redirect(url_for("login"))
    else:
        return render_template("login_signup.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        email = request.form.get('email')
        password = request.form.get('password')
        contact = request.form.get('contact')
        location = request.form.get('location')
        role = request.form.get('role')

        # Create a new User instance
        new_user = User(
            name=name,
            age=age,
            gender=gender,
            email=email,
            password=generate_password_hash(password),
            contact=contact,
            location=location,
            role=role
        )
        user = models.storage.search_one("User", email=email)
        if user:
            abort(403)
        new_user.save()
        # Save the new user to the database
        
        login_user(new_user)
        # Log in e user aftr succssful signup

        return render_template("customers_page.html")
        # Redirect e usr to the home page or any desired page

    return render_template('login_signup.html')

@app.route('/logout')
@login_required
def logout():
    """loging out user"""
    logout_user()
    return redirect(url_for('login'))

@app.route('/profile')
@login_required
def profile():
    """accessing current user """
    user = current_user
    return render_template("profile.html", user=user)

@app.route('/password-update', methods=['GET', 'POST'])
@login_required
def password_update():
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']

        # Validating e usr's current password and update e password in e database
        user = current_user
        if user.check_password(current_password):
            user.password = generate_password_hash(new_password)
            user.save()
            flash('Password updated successfully')
            return redirect(url_for('profile'))
        else:
            flash('Invalid current password')
    return render_template("update_password.html")

def generate_token(user_id):
    """ Generating a token"""
    token = serializer.dumps(user_id)
    return token

def send_password_reset_email(user, token):
    """send reset an email"""
    reset_link = url_for('passwd', token=token, _external=True)
    subject = 'Password Reset Request'
    body = f'Hello {user.name}, To reset your password, please click the following link: {reset_link}'
    email = Message(subject, recipients=[user.email], body=body)
    mail.send(email)

@app.route("/reset_password_token", methods=["GET", "POST"])
def reset():
    """Resets password"""
    if request.method == "POST":
        email = request.form["email"]
        user = models.storage.search_one("User", email=email)
        token = generate_token(user.id)
        user.reset_token = token
        user.save()
        send_password_reset_email(user, token)
        return render_template("forgot_password.html")
    else:
        return render_template("forgot_password.html")

@app.route("/reset_password", methods=["GET", "POST"])
def passwd():
    """resets forgetten password"""
    if request.method == 'POST':
        token = request.args.get("token")
        user = models.storage.search_one("User", reset_token=token)
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        if new_password == confirm_password:
            user.password = generate_password_hash(new_password)
            user.save()
        return jsonify({"password": new_password})
    return render_template('reset_password.html')

@app.route('/chat')
@login_required
def index():
    user = current_user
    return render_template('messaging.html', user=user)

@socketio.on('message')
def handle_message(data):
    print('Received message: ' + data)
    if data != "I\'m connected!":
        #new_message = Message(content=data, sender=name)
        #new_message.save()
        send(data, broadcast=True)

@app.route("/", strict_slashes=False)
@login_required
def all_customers():
    """Populates all customers view"""
    if models.storage_t == "db":
        models.storage.save()
    else:
        models.storage.reload()
    image_urls = ["../static/images/p1.jpeg", "../static/images/p2.jpeg", "../static/images/p3.jpeg", "../static/images/p4.jpeg", "../static/images/p5.jpeg", "../static/images/p6.jpeg", "../static/images/p7.jpeg", "../static/images/p8.jpeg"]
    customers = sorted(list(models.storage.all("Customer").values()),
                      key=lambda a: a.created_at)
    if models.storage_t == "db":
        for customer in customers:
            random.shuffle(image_urls)
            customer.image_url = image_urls.pop(0)
            image_urls.append(customer.image_url)
    return render_template("customers_page.html", customers=customers, storage_t=models.storage_env)


@app.route("/store", strict_slashes=False)
@login_required
def stor():
    """Implements store view"""
    if models.storage_t == "db":
        models.storage.save()
    else:
        models.storage.reload()
    item_urls = ["../static/images/item1.jpeg", "../static/images/item2.jpeg", "../static/images/item3.jpeg", "../static/images/item4.jpeg", "../static/images/item5.jpeg", "../static/images/item6.jpeg", "../static/images/item7.jpeg", "../static/images/item8.jpeg"]
    items = sorted(list(models.storage.all("Item").values()),
                   key=lambda x: x.name)
    if models.storage_t == "db":
        for item in items:
            random.shuffle(item_urls)
            item.item_img = item_urls.pop(0)
            item_urls.append(item.item_img)
    return render_template("store_page.html", items=items, storage_t=models.storage_t)

@app.route("/single/<string:customer_id>", strict_slashes=False)
@login_required
def single_customer(customer_id):
    """Handles single customer view"""
    image_urls = ["../static/images/p1.jpeg", "../static/images/p2.jpeg", "../static/images/p3.jpeg", "../static/images/p4.jpeg", "../static/images/p5.jpeg", "../static/images/p6.jpeg", "../static/images/p7.jpeg", "../static/images/p8.jpeg"]
    if models.storage_t == "db":
        models.storage.save()
    else:
        models.storage.reload()
    random.shuffle(image_urls)
    chosen = image_urls[0]
    customer = models.storage.get("Customer", customer_id)
    return render_template("single_customer.html", customer=customer, chosen=chosen)

@app.route("/create_customer", strict_slashes=False)
def create_customer():
    """Returns custmer form"""
    return render_template("customer_form.html")

@app.route("/edit_customer/<string:customer_id>", strict_slashes=False)
def edit_customer(customer_id):
    """Returns custmer form"""
    customer = models.storage.get("Customer", customer_id)
    return render_template("customer_edit_form.html", customer=customer)

@app.route("/create_item", strict_slashes=False)
def create_item():
    """Displays item form"""
    return render_template("item_form.html")

@app.route("/descriptions/<string:customer_id>", strict_slashes=False)
@login_required
def add_descriptions(customer_id):
    """Displays descriptions for a custmer"""
    if models.storage_t == "db":
        models.storage.save()
    else:
        models.storage.reload()
    customer = models.storage.get("Customer", customer_id)
    descriptions = sorted(models.storage.search_with_customer_id("Drescription", customer_id), key=lambda x: x.created_at, reverse=True)
    now = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
    user = current_user
    return render_template("descriptions_view.html", customer=customer, descriptions=descriptions, now=now, user=user)

@app.route("/single_description/<string:description_id>/<string:customer_id>")
@login_required
def display_description(description_id, customer_id):
    """Shows single description"""
    models.storage.save()
    description = models.storage.get("Description", description_id)
    now = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
    user = current_user
    customer = models.storage.get("Customer", customer_id)
    described_items =sorted(models.storage.search_with_description_id("Described_item", description_id), key=lambda x: x.created_at, reverse=True)
    for item in described_items:
        actual_item = models.storage.get("Item", item.item_id)
        item.item_name = actual_item.name
    return render_template("description_display.html", description=description, customer=customer, now=now, user=user, described_items=described_items)

@app.route("/invoices/<string:customer_id>", strict_slashes=False)
def show_invoices(customer_id):
    """Displays descriptions for a custmr"""
    if models.storage_t == "db":
        models.storage.save()
    else:
        models.storage.reload()
    customer = models.storage.get("Customer", customer_id)
    invoices = sorted(models.storage.search_with_customer_id("Invoice", customer_id), key=lambda x: x.created_at, reverse=True)
    total_amount = 0
    invoice_status = None
    for invoice in invoices:
        description_id = invoice.description_id
        described_items =sorted(models.storage.search_with_description_id("Described_item", description_id), key=lambda x: x.created_at, reverse=True)
        total_amount = 0
        for item in described_items:
            actual_item = models.storage.get("Item", item.item_id)
            item.quantity = item.frequency * item
            total_amount += actual_item.price * item.quantity
        invoiced_services = invoice.invoiced_services
        service_ids = []
        for obj in invoiced_services:
            service_ids.append(obj.service_id)
        services = []
        for s_id in service_ids:
            service = models.storage.get("Service", s_id)
            services.append(service)
        for service in services:
            if service.price is None:
                pass
            else:
                total_amount += service.price
        invoice.total_amount = total_amount
        payment = models.storage.search_one("Payment", invoice_id=invoice.id)
        if payment is None:
            invoice.paid = 0
        else:
            invoice.paid = payment.paid
        if invoice.paid >= invoice.total_amount:
            invoice.status = "Paid"
        else:
            invoice.status = "Open"
    
    return render_template("invoices.html", customer=customer, invoices=invoices)

@app.route("/all_payments/<string:customer_id>", strict_slashes=False)
def all_payments(customer_id):
    """Displays payments"""
    if models.storage_t == "db":
        models.storage.save()
    else:
        models.storage.reload()
    customer = models.storage.get("Customer", customer_id)
    payments = sorted(list(models.storage.all("Payment").values()), key=lambda x: x.created_at, reverse=True)

    customer_payments = []
    for payment in payments:
        if payment.customer_id == customer_id:
            customer_payments.append(payment)

    for payment in customer_payments:
        invoice_id = payment.invoice_id
        invoice = models.storage.get("Invoice", invoice_id)
        description_id = invoice.description_id
        described_items =sorted(models.storage.search_with_description_id("Described_item", description_id), key=lambda x: x.created_at, reverse=True)
        payment.total_amount = 0
        for item in described_items:
            actual_item = models.storage.get("Item", item.item_id)
            item.price = actual_item.price
            item.quantity = item.frequency * item
            item.pay = item.quantity * item.price
            payment.total_amount += item.pay
    return render_template("payments_view.html", customer=customer, customer_payments=customer_payments)


@app.route("/single_invoice/<string:invoice_id>", strict_slashes=False)
@login_required
def single_invoice(invoice_id):
    """shows single invoice"""
    models.storage.save()
    if not invoice_id:
        abort(404)
    invoice = models.storage.get("Invoice", invoice_id)
    if not invoice:
        abort(404)
    customer_id = invoice.customer_id
    customer = models.storage.get("Customer", customer_id)
    user = current_user
    description_id = invoice.description_id
    described_items =sorted(models.storage.search_with_description_id("Prescribed_item", description_id), key=lambda x: x.created_at, reverse=True)
    total_amount = 0
    for item in described_items:
        actual_item = models.storage.get("Item", item.item_id)
        item.item_name = actual_item.name
        item.price = actual_item.price
        item.quantity = item.frequency * item
        item.pay = item.quantity * item.price
        total_amount += item.pay
    invoiced_services = invoice.invoiced_services
    service_ids = []
    for obj in invoiced_services:
        service_ids.append(obj.service_id)
    services = []
    for s_id in service_ids:
        service = models.storage.get("Service", s_id)
        services.append(service)
    for service in services:
        if service.price is None:
            pass
        else:
            total_amount += service.price
    payment = models.storage.search_one("Payment", invoice_id=invoice.id)
    if payment is None:
        invoice.paid = 0
    else:
        invoice.paid = payment.paid
    if invoice.paid < total_amount:
        invoice.status = "Open"
    else:
        invoice.status = "Paid"
    invoice.amount_due = total_amount - invoice.paid
    return render_template("customer_invoices.html", invoice=invoice, customer=customer, user=user, described_items=described_items, total_amount=total_amount, services=services)

@app.route("/create_payment/<string:customer_id>/<string:invoice_id>", strict_slashes=False)
def create_payment(customer_id, invoice_id):
    """creates payment against customer"""
    return render_template("payment_form.html")

@app.route("/edit_payment/<string:payment_id>", strict_slashes=False)
def edit_payment(payment_id):
    """Displays payment edit form"""
    payment = models.storage.get("Payment", payment_id)
    customers = list(models.storage.all("Customer").values())
    customer = None
    for cust in customers:
        if cust.id == payment.customer_id:
            customer = models.storage.get("Customer", cust.id)
    return render_template("payment_edit_form.html", payment=payment, customer=customer)

@app.route("/single_item/<string:item_id>", strict_slashes=False)
def single_item(item_id):
    """Displays single item"""
    if models.storage_t == "db":
        models.storage.save()
    else:
        models.storage.reload()
    item = models.storage.get("Item", item_id)
    return render_template("single_item.html", item=item)

@app.route("/edit_item/<string:item_id>", strict_slashes=False)
def edit_item(item_id):
    """Edits item"""
    item = models.storage.get("Item", item_id)
    return render_template("item_edit_form.html", item=item)

@app.route("/search_customers", strict_slashes=False)
def search_customer():
    """Displays customers based on a query string"""
    query = request.args.get('q')
    
    customers = models.storage.search(query, "Customer")
    return render_template("customer_search.html", customers=customers)

@app.route("/search_items", strict_slashes=False)
def search_item():
    """Displays items based on a query string"""
    query = request.args.get("q")
    items = models.storage.search(query, "Item")
    return render_template("pharmacy_search.html", items=items)

@app.route("/search_description/<string:customer_id>", strict_slashes=False)
def search_descriptions(customer_id):
    """Displays items based on a search query"""
    customer = models.storage.get("Customer", customer_id)
    query = request.args.get("q")
    items = models.storage.search(query, "Item")
    return render_template("description_search.html", items=items)

"""
@app.route("/appointments", strict_slashes=False)
@login_required
def telemedicine():
    #Display appointments from calendly api
    access_token = "eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjgwMDA2NjMzLCJqdGkiOiI5ZWM0YTU2Yy02MGY3LTRhZTYtYTdhNy1hNThiODQyNzM0ODEiLCJ1c2VyX3V1aWQiOiJhMzk0ZjgxMS1mNjdlLTQyYTMtODcyYS1iYzM4MzU4NzM1YzAifQ.4Iz5ISUjOf0oy5J6HjHTU1kv-sTG2ff2A9w_R6-aGGjcDvNx5qj3BxxRu8WC-055bXTBsAA5QkQAp0uOXNDlmg"
    endpoint = "https://api.calendly.com/scheduled_events"
    
    now = datetime.utcnow()
    min_start_time = now - timedelta(days=7)
    min_start_time_utc = min_start_time.replace(tzinfo=timezone.utc)
    min_start_time = min_start_time_utc.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    params = {"user": "https://api.calendly.com/users/a394f811-f67e-42a3-872a-bc38358735c0", "min_start_time": min_start_time}

    response = requests.get(endpoint, headers=headers, params=params)
    response = response.json()
    
    all_events = events(response)
    all_invitees = invitees(all_events, headers)

    for event in all_events:
        for invitee in all_invitees:
            if event["uri"] in invitee:
                event.update(invitee[event["uri"]])
    return render_template("appointments.html", all_events=all_events)
"""

@app.route("/log", strict_slashes=False)
def log():
    """renders login page"""
    return render_template("login_signup.html")

@app.route("/signup")
def sign_up():
    """renders login page"""
    return render_template("login_signup.html")

@app.route("/services", strict_slashes=False)
def services():
    """Displays all services"""
    if models.storage_t == "db":
        models.storage.save()
    else:
        models.storage.reload()
    services = sorted(list(models.storage.all("Service").values()), key=lambda x: x.name)
    return render_template("services.html", services=services, storage_env=models.storage_t)

@app.route("/edit_service/<string:service_id>", strict_slashes=False)
def edit_service(service_id):
    """Displays service edit form"""
    service = models.storage.get("Service", service_id)
    return render_template("service_edit_form.html", service=service)

@app.route("/create_service", strict_slashes=False)
@login_required
def create_service():
    """Displays service creation form"""
    return render_template("service_create_form.html")

@app.route("/service/<string:service_id>", strict_slashes=False)
def single_service(service_id):
    """Displays a single service"""
    if models.storage_t == "db":
        models.storage.save()
    else:
        models.storage.reload()
    service = models.storage.get("Service", service_id)
    return render_template("single_service.html", service=service)

@app.route("/search_services", strict_slashes=False)
def search_service():
    """Displays items based on a query string"""
    query = request.args.get("q")
    services = models.storage.search(query, "Service")
    return render_template("service_search.html", services=services)

@app.route("/procurements", methods=["GET"])
def get_procurements():
    """Displays all procurements"""
    if models.storage_t == "db":
        models.storage.save()
    else:
        models.storage.reload()
    procurements = sorted(list(models.storage.all("Procurement").values()),
                          key=lambda p: p.created_at)
    return render_template("procurements.html", procurements=procurements)

@app.route('/procurements/<procurement_id>')
def show_procurement_details(procurement_id):
    procurements = models.storage.all("Procurement").values()
    procurements_with_id = [procurement.to_dict() for procurement in procurements if procurement.procurement_id == procurement_id]
    if not procurements_with_id:
        abort(404)
    return render_template("procurement_details.html", procurements=procurements_with_id)

@app.route("/create_procurement", strict_slashes=False)
@login_required
def create_procurement():
    """Displays service creation form"""
    return render_template("procurement_create.html")

@app.route("/descriptions_page/<string:customer_id>", strict_slashes=False)
@login_required
def describe(customer_id):
    models.storage.save()
    if not customer_id:
        abort(404)
    customer = models.storage.get("Customer", customer_id)
    if not customer:
        abort(404)
    user = current_user
    items = list(models.storage.all("Item").values())
    description = sorted(list(models.storage.all("Prescription").values()), key=lambda x: x.created_at)[-1]
    description_id = description.id
    described_items = models.storage.search_with_description_id("Prescribed_item", description_id)
    for item in described_items:
        actual_item = models.storage.get("Item", item.item_id)
        item.item_name = actual_item.name
    described_items_sorted = sorted(described_items, key=lambda x: x.item_name)
    return render_template("customers_descriptions.html", customer=customer, user=user, items=items, description=description, described_items=described_items_sorted)

@app.route("/descriptions_edit/<string:description_id>/<string:customer_id>", strict_slashes=False)
@login_required
def edit_description(description_id, customer_id):
    """Edits descriptions"""
    models.storage.save()
    if not description_id:
        abort(404)
    description = models.storage.get("Prescription", description_id)
    if not description:
        abort(404)
    items = sorted(list(models.storage.all("Item").values()), key=lambda x: x.name)
    user = current_user
    #customer_id = description.customer_id
    customer = models.storage.get("Customer", customer_id)
    described_items =sorted(models.storage.search_with_description_id("Prescribed_item", description_id), key=lambda x: x.created_at, reverse=True)
    for item in described_items:
        actual_item = models.storage.get("Item", item.item_id)
        item.item_name = actual_item.name
    return render_template("description_edit.html", customer=customer, user=user, items=items, description=description, described_items=described_items)

@app.route("/edit_described_item_form/<string:item_id>/<string:description_id>/<string:customer_id>", strict_slashes=False)
def edit_described(item_id, description_id=None, customer_id=None):
    """Renders description form"""
    item = models.storage.get("Prescribed_item", item_id)
    actual_item = models.storage.get("Item", item.item_id)
    items = list(models.storage.all("Item").values())
    if not item:
        abort(404)
    return render_template("edit_des.html", item=item, items=items, actual_item=actual_item)
    
@app.route("/invoice_service/<string:invoice_id>", strict_slashes=False)
def add_service_invoice(invoice_id):
    """adds service to invoice"""
    if not invoice_id:
        abort(404)
    invoice = models.storage.get("Invoice", invoice_id)
    services = list(models.storage.all("Service").values())
    if not invoice:
        abort(404)
    return render_template("invoice_service_form.html", invoice=invoice, services=services)

def events(response):
    """returns all events in last 7 days"""
    event_details = []

    for event in response["collection"]:
        uri = event["uri"]
        uri = uri.split("/")[4]
        location = event["location"].get("join_url", None)
        name = event["name"]
        start_time = event["start_time"]
        start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        start_time = pytz.utc.localize(start_time).astimezone(pytz.timezone('AFRICA/Nairobi'))
        start_time = start_time.strftime('%Y-%m-%d | %H:%M:%S')
        status = event["status"]
        event_details.append({"uri": uri, "location": location, "name": name, "start_time": start_time, "status": status})
    return(event_details)

"""
def invitees(all_events, headers):
    Returns invitee details
    invitee_ids = []
    for event in all_events:
        invitee_ids.append(event["uri"])

    invitee_details = []
    for invitee_id in invitee_ids:
        invitee_url = f"https://api.calendly.com/scheduled_events/{invitee_id}/invitees"
        r = requests.get(invitee_url, headers=headers)
        r = r.json()
        if "collection" in r:
            user_name = r.get("collection", None)[0]["name"]
            user_email = r.get("collection", None)[0]["email"]
            invitee_details.append({invitee_id: {"user_name": user_name, "user_email": user_email}})
    return(invitee_details)
"""

@app.route("/AI", strict_slashes=False)
@login_required
def chat():
    """Powers chat app"""
    user = current_user
    return render_template("chatAI.html", user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5000")
    socketio.run(app, host='0.0.0.0', port="5000")
