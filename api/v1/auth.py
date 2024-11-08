#!/usr/bin/env python3
"""
Module manages authentication and authorization
"""

import bcrypt
from models import storage
from models.users import User
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def hash_pwd(pswd: str) -> str:
    """Method hashes password"""
    if pswd is None:
        raise ValueError("Password cannot be None")
    return bcrypt.hashpw(pswd.encode(), bcrypt.gensalt())

def generate_uuid() -> str:
    """Generates uuid4"""
    return str(uuid4())


class Auth:
    """authorization, authentication"""
    def register_user(self, name: str, gender: str, email: str, password: str,
                      contact: str=None, role: str=None, age: int=None) -> User:
    
        user = storage.search_one("User", "email", email)
        #user = db.session.query(User).filter_by(email=email).first()
        if user is None:
            password = hash_pwd(password)
            user = User(name=name, age=age, gender=gender, email=email, password=password,
                        contact=contact, role=role)
            storage.create(User)
            storage.save()
            return user
        else:
            raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """check if user exists"""
        user = None
        try:
            user = storage.search_one("User", "email", email)
        except NoResultFound:
            pass

        if user:
            encoded_password = password.encode()
            user_password = user.password.encode()
            if bcrypt.checkpw(encoded_password, user_password):
                return True
        return False

    def create_session(self, email: str) -> str:
        """create session 4 user"""
        try:
            user = storage.search_one("User", email=email)
        except NoResultFound:
            return None

        session_id = generate_uuid()
        key = "User" + "." + user.id
        storage.update(key, session_id=session_id)
        return session_id

    def retrieve_user_by_session_id(self, session_id: str) -> User:
        """Returns user object via session_id"""
        try:
            user = storage.search_one("User", session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, email: str) -> None:
        """Destroys session"""
        try:
            user = storage.search_one("User", email=email)
        except NoResultFound:
            return None
        key = "User" + "." + user.id
        storage.update(key, session_id=None)
        return None

    def password_reset_token(self, email: str) -> str:
        """Get reset token"""
        try:
            user = storage.search_one("User", email=email)
        except NoResultFound:
            raise ValueError
        
        reset_token = generate_uuid()
        key = "User" + "." + user.id
        storage.update(key, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update password"""
        if reset_token is None or password is None:
            return None
        try:
            user = storage.search_one("User", reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        password = hash_pwd(password)
        key = "User" + "." + user.id
        storage.update(key, password=password, reset_token=None)
        return None
