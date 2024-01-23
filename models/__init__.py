#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
from sqlalchemy import text

storage_t = getenv("DSE_TYPE_STORAGE")
# from sqlalchemy import text

if storage_t == "db":
    from models.engine.db_storage import DB_Storage
    storage = DB_Storage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
