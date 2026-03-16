# Modular Entity and Mapping System

This project implements a modular backend architecture using Django REST Framework. 
Each entity and mapping is separated into independent apps to improve scalability 
and maintainability.


## Installation

Clone the repository

git clone https://github.com/rahilaaaa/modular-entity-system.git


Create virtual environment

python -m venv venv

Activate virtual environment

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt


## Installed Apps

### Master Apps
- vendor
- product
- course
- certification

### Mapping Apps
- vendor_product_mapping
- product_course_mapping
- course_certification_mapping


## Run the Project

Run migrations

python manage.py migrate

Start server

python manage.py runserver

## API Documentation

Swagger UI
http://127.0.0.1:8000/swagger/

Redoc
http://127.0.0.1:8000/redoc/

## API Usage Examples

### Create Vendor

POST /api/vendor/

Request Body

{
  "name": "Vendor A"
}

Response

{
  "id": 1,
  "name": "Vendor A"
}


### Get Vendors

GET /api/vendor/

Response

[
  {
    "id": 1,
    "name": "Vendor A"
  }
]


modular_entity_system/
│
├── env/                          # Python virtual environment
│
├── modular_entity_system/        # Main Django project folder
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── vendor/      
--common/                 # Vendor master entity
├── product/                      # Product master entity
├── course/                       # Course master entity
├── certification/                # Certification master entity
│
├── vendor_product_mapping/       # Mapping: Vendor → Product
├── product_course_mapping/       # Mapping: Product → Course
├── course_certification_mapping/ # Mapping: Course → Certification
│
├── common/                       # Shared utilities / base classes
│
├── db.sqlite3                    # SQLite database
├── manage.py                     # Django management script
└── README.md                     # Project documentation