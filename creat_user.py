#!/usr/bin/python3

from models import storage, User
user = User(name="Green Joselyn", age=23, gender="Female", email="gui@hbtn.co", password="12345", location="entebbe", contact="0123456789", role="user", session_id="1", reset_token="1")
storage.new(user)
storage.save()
print(f"User {user.name} has been created successfully!")