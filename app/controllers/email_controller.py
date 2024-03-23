from datetime import datetime
from flask import request, jsonify
from app import app, db, mail, scheduler
from app.models.email import Email
from flask_mail import Message

@app.route('/save_emails', methods=['POST'])
def save_emails():
    data = request.get_json()
    event_id = data.get('event_id')
    email_subject = data.get('email_subject')
    email_content = data.get('email_content')
    timestamp = data.get('timestamp')

    if not all([event_id, email_subject, email_content, timestamp]):
        return jsonify({'message': 'Missing parameters'}), 400

    new_email = Email(event_id=event_id,
                email_subject=email_subject,
                email_content=email_content,
                timestamp=timestamp)
    db.session.add(new_email)
    db.session.commit()

    # Schedule email sending
    scheduler.add_job(send_email, 'date', run_date=timestamp, args=[email_subject, email_content])

    return jsonify({'message': 'Email saved successfully and scheduled for sending'}), 201

def send_email(subject, body):
    msg = Message(subject, recipients=['recipient@example.com'])
    msg.body = body
    mail.send(msg)