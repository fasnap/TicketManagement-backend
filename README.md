# Simple Ticket Management System

## Overview
This project is a simple ticket management system that allows users to raise support tickets, view their status, and allows administrators to manage these tickets (assign, resolve, etc.). The project is split into a backend (Django) and a frontend (React).

## Features
- Users can create, view, update, and delete their support tickets.
- Administrators can manage all tickets.
- Basic user authentication and authorization.
- User-friendly interface with filtering options for tickets based on status and priority.

## Requirements
### Backend (Django)
- Django REST API with endpoints for ticket management.
- Basic user authentication using Django's built-in system.
- User permissions to ensure users can only interact with their own tickets, while administrators have full access.

### Frontend (React)
- User interface for managing tickets.
- Pages for login, dashboard, ticket details, and admin management.
- Responsive design using Material UI or Tailwind CSS.

## Endpoints
### Backend (Django)
- `POST /tickets/`: Create a new support ticket.
- `GET /tickets/`: List all tickets with filters for status, priority, and user.
- `PUT /tickets/<id>/`: Update a ticket's details.
- `DELETE /tickets/<id>/`: Delete a ticket.
- `GET /tickets/<id>/`: Get details of a specific ticket.

## Installation and Setup
### Backend (Django)
1. **Clone the backend repository:**
    ```sh
    git clone <backend-repo-url>
    cd backend-repo
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the requirements:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser for accessing the admin panel:**
    ```sh
    python manage.py createsuperuser
    ```

6. **Start the development server:**
    ```sh
    python manage.py runserver
    ```

### Frontend (React)
1. **Clone the frontend repository:**
    ```sh
    git clone <frontend-repo-url>
    cd frontend-repo
    ```

2. **Install the dependencies:**
    ```sh
    npm install
    ```

3. **Start the development server:**
    ```sh
    npm start
    ```

## Usage
- **Login Page:** Users can log in with their credentials.
- **Dashboard Page:** Displays a list of all tickets with filtering options. Users can create new tickets and see their own tickets.
- **Ticket Detail Page:** Shows details of a specific ticket with options to update or delete it.
- **Admin Page:** Shows all tickets to administrators with options to update the status, assign users, or delete tickets.

## Assessment Criteria
- **Code Quality:** Clear, concise, and well-structured code with meaningful comments.
- **Full-Stack Understanding:** Ability to work on both frontend and backend seamlessly.
- **API Integration:** Proper integration between React frontend and Django backend.
- **Security:** Basic authentication and authorization mechanisms.
- **User Interface:** A clean, responsive, and user-friendly UI that follows good design principles.
- **Documentation:** Clear instructions on setting up and running the project locally.
