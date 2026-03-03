# Project-Phase-I2025-26
*Jan Samasya Portal (Grievance Redressal System):

Jan Samasya Portal is a web-based grievance redressal application designed to help citizens report public issues efficiently and transparently. The system enables users to submit grievances, track their status, and allows administrators to manage, assign, and resolve complaints through a centralized platform.

*Project Structure:

The project is organized into three main components:
Frontend (templates / static/): User and Admin interfaces built using HTML, CSS, JavaScript, and Jinja2 templates.
Backend (app.py / routes/): Flask-based backend handling authentication, grievance management, and business logic.
Database (database/): Relational database (MySQL / SQLite) used for storing users, grievances, and status updates.

*Prerequisites:

Before setting up the project, ensure you have the following installed:
Python (v3.8 or higher)
Flask
MongoDB
Web Browser (Chrome/Firefox)

*Setup Instructions:

Follow these steps to get the application running locally.
1. Backend Setup (Flask)
The backend handles API requests, authentication, and database operations.
cd project-folder
pip install -r requirements.txt
Configuration:
Update database credentials and secret keys in the configuration file.
Run Development Server:
python app.py
Server typically runs on http://localhost:5000
2. Frontend Setup
The frontend is served using Flask templates.
HTML files are located in the templates/ folder
CSS and JavaScript files are located in the static/ folder
No separate build process is required.

*Usage:

Start the Flask Server
Open your browser and navigate to http://localhost:5000
Register as a user and log in
Submit a grievance with relevant details
Track grievance status from the dashboard
Admin can log in to view, assign, and resolve grievances

*Features:

User Registration and Login
Grievance Submission
Grievance Status Tracking
Admin Dashboard
Role-based Access Control
Secure Data Handling

*Technologies Used:

Frontend: HTML, CSS, JavaScript, Jinja2
Backend: Python (Flask)
Database: MySQL / SQLite
