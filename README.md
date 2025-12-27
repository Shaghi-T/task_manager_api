# Task Management REST API

A complete REST API for managing projects and tasks, built with Django REST Framework.

## Features

- User authentication with JWT
- CRUD operations for Projects and Tasks
- Filter, Search, and Ordering
- Pagination
- Swagger/OpenAPI documentation

## Tech Stack

- Python 3.11
- Django 5
- Django REST Framework
- PostgreSQL / SQLite
- JWT Authentication
- Swagger (drf-yasg)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Shaghi-T/task-manager-api.git
cd task-manager-api
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/accounts/register/ | Register new user |
| POST | /api/accounts/login/ | Get JWT token |
| POST | /api/accounts/token/refresh/ | Refresh token |
| GET | /api/accounts/profile/ | Get user profile |

### Projects
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/projects/ | List all projects |
| POST | /api/projects/ | Create project |
| GET | /api/projects/{id}/ | Get project detail |
| PUT | /api/projects/{id}/ | Update project |
| DELETE | /api/projects/{id}/ | Delete project |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasks/ | List all tasks |
| POST | /api/tasks/ | Create task |
| GET | /api/tasks/{id}/ | Get task detail |
| PUT | /api/tasks/{id}/ | Update task |
| DELETE | /api/tasks/{id}/ | Delete task |

### Query Parameters
- Filter: `?status=done&priority=high`
- Search: `?search=meeting`
- Order: `?ordering=-created_at`

## Documentation

- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## Project Structure

```
task-manager-api/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
│   ├── models.py      # Custom User model
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── tasks/
│   ├── models.py      # Project, Task models
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

## Author

Shaghayegh Tamouk
