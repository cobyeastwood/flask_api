"""
@desc: configuration for app.py, wraps server with additional tools for JSON serialization/deserialization.
@made: (07/24/2020), by Coby Eastwood

"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

from app import app

db = SQLAlchemy()
ma = Marshmallow(app)

bcrypt = Bcrypt(app)