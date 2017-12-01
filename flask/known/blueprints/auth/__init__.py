from flask import Blueprint, current_app
from . import get_db

bp = Blueprint('auth', __name__)


def init_db():
    db = get_db()
    with current_app.open_resource('auth/schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
