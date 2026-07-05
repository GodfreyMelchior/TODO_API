# Todo API

A Django REST API for managing todo tasks with status tracking, due dates/times, archiving, filtering, and auto-generated documentation.

## Features

- Full CRUD operations for todos
- Six-state status tracking (Pending, In Progress, On Hold, In Review, Completed, Cancelled)
- Overdue detection based on due date/time and current status
- Archive/unarchive support without deleting data
- Rich filtering (status, archive state, overdue state, text search)
- Interactive API documentation (Swagger UI and ReDoc) via drf-spectacular

## Requirements

- Python 3.10+
- Django 6.0+
- djangorestframework
- django-filter
- drf-spectacular

## Installation

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd todo_api_project

# 2. Create and activate a virtual environment
python -m venv venv

# Mac/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

## Running the Project

```bash
# 1. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 2. Create a superuser (optional, for Django admin access)
python manage.py createsuperuser

# 3. Run the development server
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/`.

## Documentation

Interactive, auto-generated API documentation is available at:

| URL | Description |
|---|---|
| `/api/docs/` | Swagger UI (interactive — try requests directly in the browser) |
| `/api/redoc/` | ReDoc (clean, read-focused reference) |
| `/api/schema/` | Raw OpenAPI schema (YAML/JSON) |

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/api/todos/` | GET | List all non-archived todos |
| `/api/todos/` | POST | Create a new todo |
| `/api/todos/{id}/` | GET | Retrieve a specific todo (including archived) |
| `/api/todos/{id}/` | PUT | Full update of a todo |
| `/api/todos/{id}/` | PATCH | Partial update of a todo |
| `/api/todos/{id}/` | DELETE | Delete a todo (including archived) |

> **Note:** The default list view hides archived todos. Retrieve, update, and delete operate on all todos, including archived ones.

## Filtering

Available query parameters on `GET /api/todos/`:

| Parameter | Type | Example |
|---|---|---|
| `status` | exact match | `?status=PENDING` |
| `is_archived` | boolean | `?is_archived=true` |
| `is_overdue` | boolean (computed) | `?is_overdue=true` |
| `title` | text search (icontains) | `?title=report` |
| `description` | text search (icontains) | `?description=urgent` |

Filters can be combined, e.g.:

```
GET /api/todos/?status=IN_PROGRESS&is_overdue=true
```

## Validation Rules

- `title` cannot be empty or whitespace-only.
- `due_datetime` cannot be set in the past — enforced on both create and update.
- `is_archived` is ignored on create (new todos are never created as archived); it can be set on update.

## Todo Model

| Field | Type | Notes |
|---|---|---|
| `id` | integer | Auto-generated, read-only |
| `title` | string | Max 100 characters |
| `description` | string | Optional |
| `status` | choice | `PENDING`, `IN_PROGRESS`, `ON_HOLD`, `IN_REVIEW`, `COMPLETED`, `CANCELLED` |
| `is_archived` | boolean | Hides the todo from the default list view |
| `created_at` | datetime | Auto-set on creation, read-only |
| `due_datetime` | datetime | Deadline for the task, defaults to now |
| `is_overdue` | boolean (computed) | True if `due_datetime` has passed and status is not `COMPLETED`/`CANCELLED` |
| `is_completed` | boolean (computed) | True if status is `COMPLETED` |

## Project Structure

```
todo_api_project/
├── config/             # Project settings, root URLs
├── todos/              # Todo app: models, serializers, views, filters
├── requirements.txt
├── manage.py
└── README.md
```