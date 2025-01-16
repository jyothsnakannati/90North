# Django Chat Application

This is a real-time chat application built using Django and Django Channels for WebSocket-based communication.

## Features

- User Registration and Authentication (Signup/Login/Logout)
- Real-time Chat using WebSockets
- View List of Users
- Display chat messages between users
- Store messages in a database
- Responsive and simple UI

## Requirements

- Python 3.x
- Django 3.x or higher
- Django Channels
- Redis (for managing WebSocket connections)
- Database (SQLite for development)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/django-chat-app.git
   cd django-chat-app


## Install dependencies:

pip install -r requirements.txt

## Set up Redis (If using Redis): Make sure you have Redis installed and running locally:

brew install redis
redis-server


## Apply migrations:

python manage.py migrate

## Create a superuser for accessing the Django Admin:

python manage.py createsuperuser

## Start the development server:

python manage.py runserver

## Access the application at

http://127.0.0.1:8000/

