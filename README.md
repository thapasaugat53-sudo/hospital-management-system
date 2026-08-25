# Hospital Management System

A web-based **Hospital Management System (HMS)** developed using **Python Django** and **MySQL**. The system is designed to simplify hospital operations by managing patients, doctors, appointments, and related hospital information.

## 📌 Project Overview

The Hospital Management System provides a centralized platform for managing hospital activities. It allows users to manage patient information, doctor information, appointments, and other hospital-related operations through a web interface.

The backend is developed using Django, while MySQL is used as the database.

## 🛠️ Technologies Used

* **Backend:** Python, Django
* **Database:** MySQL
* **Frontend:** HTML, CSS, JS
* **Version Control:** Git & GitHub
* **Development Environment:** VS Code 

## ✨ Features

### 👤 Patient Management

* Add and manage patient information
* View patient details
* Update patient information
* Manage patient records

### 👨‍⚕️ Doctor Management

* Add and manage doctor information
* View doctor profiles
* Manage doctor availability
* Allow doctors to manage appointments

### 📅 Appointment Management

* Patients can request appointments
* Doctors can view appointments
* Doctors can confirm appointments
* Doctors can cancel appointments
* Appointment status can be tracked

### 🔐 Authentication

* User registration and login
* User logout
* Role-based access for different users
* Protected pages using Django authentication

## 🏗️ System Architecture

The system follows a simple three-layer architecture:

```text
┌─────────────────────┐
│      Frontend       │
│   HTML / CSS / JS   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Django Backend   │
│  Views / Models /   │
│      Forms / URLs   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       MySQL         │
│      Database       │
└─────────────────────┘
```

## 📂 Project Structure

```text
hospital-management-system/
│
├── manage.py
│
├── hospital_management/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── migrations/
│
├── templates/
│   ├── base.html
│   ├── accounts/
│   ├── patient/
│   └── doctor/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── requirements.txt
└── README.md
```

> The exact structure may vary depending on the apps and files in the project.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone 
```

Move into the project directory:

```bash
cd hospital-management-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install Django manually:

```bash
pip install django
```

Install the MySQL database driver if required:

```bash
pip install mysqlclient
```

## 🗄️ Database Configuration

Make sure **MySQL Server** is installed and running.

Create the database in MySQL:

```sql
CREATE DATABASE hospital_management;
```

Configure the database in `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "hospital_management",
        "USER": "root",
        "PASSWORD": "your_mysql_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

Replace `your_mysql_password` with your MySQL password.

## 🔄 Run Migrations

After configuring the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

Check migration status:

```bash
python manage.py showmigrations
```

## 👨‍💻 Create Admin User

Create a Django superuser:

```bash
python manage.py createsuperuser
```

Follow the instructions displayed in the terminal.

## ▶️ Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

The Django admin panel can be accessed at:

```text
http://127.0.0.1:8000/admin/
```

## 🔑 User Roles

The system can support different types of users, such as:

| Role    | Main Responsibilities                            |
| ------- | ------------------------------------------------ |
| Admin   | Manage doctors, patients, and system information |
| Doctor  | View, confirm, and cancel appointments           |
| Patient | Manage profile and request appointments          |

## 📅 Appointment Workflow

```text
Patient
   │
   ▼
Request Appointment
   │
   ▼
Doctor Views Appointment
   │
   ├──── Confirm ────► CONFIRMED
   │
   └──── Cancel ─────► CANCELLED
```

## 🔒 Security

The project uses Django's built-in authentication and authorization features.

Security considerations include:

* Login protection
* Authentication-required views
* User-specific access control
* CSRF protection
* Django password hashing
* Database validation

## 🧪 Testing

Run Django's test suite using:

```bash
python manage.py test
```

Run the Django system check:

```bash
python manage.py check
```

## 🚀 Future Improvements

Possible future enhancements include:

* Online payment integration
* Prescription management
* Medical report management
* Email/SMS appointment notifications
* Doctor availability calendar
* Patient medical history
* REST API integration
* Advanced admin dashboard
* Appointment reminders
* Deployment to a cloud server

## 👥 Project Team


**Hospital Management System**

Developed as a college project using Django and MySQL.

### Backend

* Python
* Django
* MySQL
* Authentication
* Appointment management

### Frontend

* HTML
* CSS
* JavaScript

## 📄 License

This project was developed for educational purposes.
