# Little Lemon Restaurant API

A REST API for the Little Lemon restaurant, built with Django REST Framework.

## Features

- Menu Items Management
- Table Booking System
- User Authentication
- API Token Authorization
- Browsable API Interface

## API Endpoints

### Menu Endpoints
- `GET /api/menu/`: List all menu items
- `POST /api/menu/`: Create a new menu item
- `GET /api/menu/{id}/`: Retrieve a menu item
- `PUT /api/menu/{id}/`: Update a menu item
- `DELETE /api/menu/{id}/`: Delete a menu item

### Booking Endpoints
- `GET /api/booking/`: List all bookings
- `POST /api/booking/`: Create a new booking
- `GET /api/booking/{id}/`: Retrieve a booking
- `PUT /api/booking/{id}/`: Update a booking
- `DELETE /api/booking/{id}/`: Delete a booking

### Authentication Endpoints
- `POST /api-token-auth/`: Obtain auth token
- `POST /auth/users/`: Register a new user
- `POST /auth/token/login/`: User login

## Technologies Used

- Django
- Django REST Framework
- MySQL
- Djoser
- Token Authentication

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Walid-Khalfa/Little-Lemon-WebApp.git
```
