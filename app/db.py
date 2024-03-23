
from app import db
from app import app
from flask import current_app


def init_db():
    from app.models.email import Email
    db.create_all()

def init_db_command():
    """Create database tables."""
    with current_app.app_context():
        init_db()
        print("Initialized the database.")