# FormCraft Backend

Python FastAPI backend for the Universal Form Designer & Print Studio.

## Tech Stack

- **Python 3.12** + **FastAPI**
- **Supabase** (Auth, DB, Storage)
- **WeasyPrint** (PDF rendering)
- **AWS Bedrock** (AI suggestions)
- **Pydantic v2** (validation)

## Project Structure

```
app/
├── api/           # FastAPI routes and dependencies
├── core/          # Config, security, audit, middleware
├── models/        # Pydantic domain models
├── schemas/       # Request/response schemas
└── services/      # Business logic (AI, PDF, validators, templates, users)
supabase/
├── migrations/    # SQL migrations
└── seed.sql       # Seed data
tests/
├── unit/          # Unit tests
└── integration/   # Integration tests
```

## Setup

### Prerequisites

- Python 3.12+
- System deps for WeasyPrint: `libpango`, `libcairo`, `libgdk-pixbuf`

### Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configure

```bash
cp .env.example .env
# Edit .env with your Supabase and AWS credentials
```

### Run

```bash
uvicorn app.main:app --reload --port 8000
```

### Test

```bash
pytest
```

### Docker

```bash
docker build -t formcraft-backend .
docker run -p 8000:8000 --env-file .env formcraft-backend
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /api/health | Health check |
| POST | /api/auth/login | User login |
| POST | /api/auth/register | Register user (admin) |
| POST | /api/auth/refresh | Refresh token |
| GET | /api/users/me | Get profile |
| PUT | /api/users/me | Update profile |
| CRUD | /api/templates/* | Template management |
| CRUD | /api/templates/pages/* | Page management |
| CRUD | /api/templates/elements/* | Element management |
| POST | /api/ai/suggest-control | AI suggestion |
| POST | /api/pdf/render/{id} | Render PDF |
| GET | /api/pdf/preview/{id} | Preview PDF |
| GET | /api/admin/audit-logs | Query audit logs |
