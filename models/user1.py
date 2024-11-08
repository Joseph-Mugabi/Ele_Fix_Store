
class User(BaseModel, UserMixin, Base):    
    """The representation of a class User"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        full_name = Column(String(128), nullable=False)
        age = Column(Integer, nullable=True)
        gender = Column(String(60), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        location = Column(String(128), nullable=True)
        contact = Column(String(60), nullable=True)
        role = Column(String(128), nullable=True)
        session_id = Column(String(256))
        reset_token = Column(String(256))

    else:
        # Placeholder attributefor non-database storage
        full_name = ""
        email = ""
        password = ""
        location = ""
        contact = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the User"""
        print(kwargs)
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """Set password with secure hashing"""
        if name == "password":
            value = generate_password_hash(value)
        super().__setattr__(name, value)

    def check_password(self, password):
        """Check if the provided password matches the hashed password"""
        return check_password_hash(self.password, password)

    def get_id(self):
        """Convert user id to string"""
        return str(self.id)

    # Flask-Login needs methods
    def is_authenticated(self):
        """Check if user is authenticated"""
        return True  # Assume all users are authenticated

    def is_active(self):
        """Check if user is active"""
        return True  # Assume all users are active

    def is_anonymous(self):
        """Check if user is anonymous"""
        return False  # Assume all users are not anonymous
