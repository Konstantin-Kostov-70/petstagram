# Petstagram

Petstagram is a web application designed for pet lovers to share photos of their pets, manage pet profiles, and interact with other users. Built using Django and utilizing the Django Template Language (DTL), Petstagram allows users to upload pet photos, add comments, like photos, and manage their pet details.

## Features

- **User Registration & Authentication**: Users can create accounts, log in, and manage their profiles.
- **Pet Management**: Users can add pets, edit their details, and delete pet profiles.
- **Photo Sharing**: Users can upload photos of their pets, view photos of other pets, and interact with them.
- **Comments & Likes**: Users can comment on photos and like them to show appreciation.

## Project Structure
```
petstagram/
├── petstagram/
│   ├── accounts/                     # User account management
│   ├── common/                       # Shared views and utilities
│   ├── pets/                         # Pet management features
│   ├── photos/                       # Photo management features
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/                        # HTML templates using Django Template Language (DTL)
├── static/                           # Static files (CSS, JavaScript, Images)
├── requirements.txt                  # Required Python packages
└── manage.py                         # Django command-line utility for administrative tasks
```

## Installation

### Prerequisites

1. Python 3.8 or higher
2. Django 4.1 or higher
3. A PostgreSQL database (optional, but recommended)

### Setup

1. **Clone the repository**:

```bash
git clone https://github.com/Konstantin-Kostov-70/petstagram.git
cd petstagram
```
## 2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
```
## 3. Install required packages:
```bash
pip install -r requirements.txt
```
## 4. Set up the database (if using PostgreSQL):
Create a PostgreSQL database and update your settings.py file with the database configuration.

## 5. Run migrations:
```bash
python manage.py migrate
```
## 6. Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```
## 7. Run the development server:
```bash
python manage.py runserver
```
Open your web browser and visit http://127.0.0.1:8000 to access Petstagram!




