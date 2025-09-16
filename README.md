# Citizen-AI-Intelligent-Citizen-Engagement-Platform

This is a reimagined implementation with the same goal: enable citizens to chat with an AI assistant,
submit civic concerns, and view a lightweight analytics dashboard. The internal code is intentionally
different from any single reference project while preserving the high-level functionality.

Features:
- Flask application with SQLite persistence via SQLAlchemy
- Modular package layout: `citizen_ai` with `routes`, `models`, `services`
- Simple LLM adapter stub (pluggable)
- Dockerfile for containerized runs
- Minimal UI with responsive templates

Quick start (local):
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=run.py
flask db init   # creates migrations (optional)
flask db migrate
flask db upgrade
flask run
```

Or with Docker:
```
docker build -t citizen-ai .
docker run -p 5000:5000 citizen-ai
```
