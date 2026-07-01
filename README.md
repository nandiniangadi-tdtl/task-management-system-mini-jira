# Task Management System (Mini Jira)

A Django REST Framework project for task management.

## Features

- JWT Authentication
- Role-Based Access (Admin, Manager, Developer)
- Create Projects
- Create Tasks
- Update Task Status
- Task History
- Comments
- File Uploads
- MySQL Database

## Tech Stack

- Python
- Django
- Django REST Framework
- MySQL
- JWT Authentication
- Postman

## Installation

```bash
git clone <repository-url>
cd mini_jira

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver