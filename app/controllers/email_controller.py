# app/controllers/email_controller.py

from flask import Blueprint, request, jsonify
from app.models.email import Email
from app import db
from datetime import datetime

email_bp = Blueprint('email', __name__)

@email_bp.route('/save_emails', methods=['POST'])
def save_emails():
    data = request.get_json()
    event_id = data.get('event_id')
    email_subject = data.get('email_subject')
    email_content = data.get('email_content')
    timestamp_str = data.get('timestamp')

    # Convert timestamp string to datetime object
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')

    new_email = Email(event_id=event_id, email_subject=email_subject, email_content=email_content, timestamp=timestamp)
    db.session.add(new_email)
    db.session.commit()

    return jsonify({'message': 'Email saved successfully!'}), 200
