# Todo API

A Django REST API for managing todo tasks with status tracking and due dates.

## Features

- Full CRUD operations for todos
- Status filtering (Pending, Completed, Cancelled, On Hold, In Progress, In Review)
- Overdue task detection
- Archive/unarchive functionality
- OpenAPI schema generation with drf-spectacular

## Requirements

- Python 3.10+
- Django 6.0+
- djangorestframework
- django-filter
- drf-spectacular

## Installation

```bash
pip install -r requirements.txt
```

## Running the Project

```bash
# Apply migrations
python manage.py migrate

# Create a superuser (optional, for admin access)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/todos/` | GET | List all non-archived todos |
| `/api/todos/` | POST | Create a new todo |
| `/api/todos/{id}/` | GET | Retrieve a specific todo |
| `/api/todos/{id}/` | PUT/PATCH | Update a todo |
| `/api/todos/{id}/` | DELETE | Delete a todo |

## Filtering

Todos can be filtered by status:

```
GET /api/todos/?status=PENDING
GET /api/todos/?status=COMPLETED
```

## Todo Model

- `title` - Task title (max 100 characters)
- `description` - Optional task description
- `status` - One of: PENDING, COMPLETED, CANCELLED, ON_HOLD, IN_PROGRESS, IN_REVIEW
- `is_archived` - Boolean flag for archived todos
- `due_date` - Date field with today as default
- `is_overdue` - Computed property (overdue if due date passed and not completed/cancelled)