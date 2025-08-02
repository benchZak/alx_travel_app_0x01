# ALX Travel App - Django Backend

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white)

A travel listing platform backend built with Django, Django REST Framework, and MySQL.

## Features

- RESTful API architecture
- MySQL database integration
- Automated API documentation with Swagger
- CORS support for frontend integration
- Environment variable configuration
- Ready for Celery task queue integration

## Prerequisites

- Python 3.8+
- MySQL 8.0+
- RabbitMQ (for Celery, optional)
- Fedora Linux (recommended for development)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/benchzak/alx_travel_app.git
cd alx_travel_app

# ALX Travel App API

## API Documentation

The API is documented using Swagger UI. You can access it at:
- `/api/docs/`

## Endpoints

### Listings
- GET `/api/listings/` - List all listings
- POST `/api/listings/` - Create a new listing
- GET `/api/listings/{id}/` - Retrieve a specific listing
- PUT `/api/listings/{id}/` - Update a listing
- PATCH `/api/listings/{id}/` - Partially update a listing
- DELETE `/api/listings/{id}/` - Delete a listing

### Bookings
- GET `/api/bookings/` - List all bookings
- POST `/api/bookings/` - Create a new booking
- GET `/api/bookings/{id}/` - Retrieve a specific booking
- PUT `/api/bookings/{id}/` - Update a booking
- PATCH `/api/bookings/{id}/` - Partially update a booking
- DELETE `/api/bookings/{id}/` - Delete a booking

## Testing

You can test the API endpoints using tools like Postman or curl.

Example requests:
```bash
# Get all listings
curl -X GET http://localhost:8000/api/listings/

# Create a new listing
curl -X POST -H "Content-Type: application/json" -d '{"title":"Beach Villa","description":"Luxury villa by the beach","price":200}' http://localhost:8000/api/listings/
