#!/usr/bin/python3
""" blueprint for API """

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.blueprints.customers import *
from api.v1.blueprints.users import *
from api.v1.blueprints.services import *
from api.v1.blueprints.invoices import *
from api.v1.blueprints.invoice_services import *
from api.v1.blueprints.payments import *
from api.v1.blueprints.items import *
from api.v1.blueprints.procurements import *
from api.v1.blueprints.described_items import *
from api.v1.blueprints.descriptions import *
from api.v1.blueprints.chatgpt import *
