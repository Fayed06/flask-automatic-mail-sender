import unittest
from app import app, db

class TestEmailController(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

        # Establish an application context
        self.app_context = app.app_context()
        self.app_context.push()

        # Create all tables
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Remove the tables and the application context
        with app.app_context():
            db.session.remove()
            db.drop_all()
        self.app_context.pop()

    def test_save_emails(self):
        data = {
            'event_id': 1,
            'email_subject': 'Test Subject',
            'email_content': 'Test Content',
            'timestamp': '2024-03-24 12:00:00'  # Adjust timestamp as needed
        }
        response = self.app.post('/save_emails', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email saved successfully!', response.data)

if __name__ == '__main__':
    unittest.main()