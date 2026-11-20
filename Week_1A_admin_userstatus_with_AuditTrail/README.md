# Week XX: Challenge Name

## Overview
What this project does, in 1-2 sentences.

## Tech Stack
-

## Setup
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
python -m uvicorn app.main:app --reload
```

Or with Docker:
```bash
docker compose up --build
```

## API Endpoints
| Method | Path | Description | Auth |
|--------|------|-------------|------|
| | | | |

## Running Tests
```bash
pytest -v
```

## Design Decisions
- What I chose and why
- Trade-offs I made