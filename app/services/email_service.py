# app/services/email_service.py

from app import app
from app import db
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from app.models.email import Email
from datetime import datetime, timedelta

mail = Mail(app)

def send_email():
    with app.app_context():
        unsent_emails = Email.query.filter(Email.timestamp <= datetime.utcnow()).all()
        for email in unsent_emails:
            msg = Message(subject=email.email_subject,
                          recipients=['recipient@example.com'],  # Change this to actual recipient
                          body=email.email_content)
            mail.send(msg)
            db.session.delete(email)
            db.session.commit()

# scheduler = BackgroundScheduler()
# scheduler.add_job(send_email, 'interval', seconds=30)  # Adjust interval as needed
# scheduler.start()
