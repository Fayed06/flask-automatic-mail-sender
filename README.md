# Scheduled Email Sender using Flask

a simple web application that is able to serve a POST endpoint. The main function of the endpoint is to store in the database an email for a particular group of recipients. The emails are then to be sent automatically at a later time

## Overview

This project is a simple web application built using Flask, allowing users to store email messages for a group of recipients and schedule them to be sent at a later time.

## Setup Local Environment

Follow these steps to set up the project environment locally:

1. Clone the repository:

``git clone <repository-url>``

``cd <project-folder>``

2. Create and activate a virtual environment (optional but recommended):

``python -m venv env``

``source env/bin/activate # For Unix/Linux``

``\env\Scripts\activate # For Windows``


3. Install dependencies:
``pip install -r requirements.txt``


4. Set up environment variables:

``cp .env.example .env``

Edit the `.env` file and fill in the required configurations.

## Running the Application

To run the Flask application locally, execute the following command:

``python run.py``

Access the application in your web browser at `http://localhost:5000`.

## Running Unit Tests

To run the unit tests, use the following command:

``python -m unittest discover tests``


## Screenshots

![Screenshot of Landing Page](screenshots/landing_page.png)