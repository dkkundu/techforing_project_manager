# Project Management API

This is a Django-based project management API that allows users to manage projects, tasks, and comments.

## Features

- **User authentication and management**
- **Project creation and collaboration**
- **Task assignment and tracking**
- **Comments on tasks for better communication**

---

## Installation and Setup

### Prerequisites

- Python 3.11 or later
- pip (Python package installer)
- Virtual environment tool (`venv` or `virtualenv`)
- A PostgreSQL database (or SQLite for development)

---

### Steps to Set Up

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Create a Virtual Environment**
   ```
   python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate

   ```
3. **Install Dependencies**
   ```
   pip install -r requirements.txt

   ```
4. **Configure the Database**
    Update the database settings in settings.py:
   ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',  # Or 'sqlite3' for development
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',  # Default PostgreSQL port
        }
    }

   ```

5. **Run Database Migrations**
   ```
    python manage.py makemigrations
    python manage.py migrate
   ```


6. **Create a Superuser**
   ```
    python manage.py createsuperuser
   ```
7. **Start the Development Server**
   ```
    python manage.py runserver
   ```
8. **Access the Application**
   ```
    Open http://127.0.0.1:8000 in your browser.
   ```
8. **Access the Application**
   ```
    Open http://127.0.0.1:8000/documentations/ in your browser.
   ```

## Licensed
    This project is licensed under the MIT License.

## Contact
    For questions or suggestions, contact Dipto Kumar Kundu at dkkundu00@gmail.com.