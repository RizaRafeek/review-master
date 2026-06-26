Review Master — Project Documentation
Overview
Review Master is a spaced repetition study scheduler. Users add lecture topics or chapters, and the system automatically schedules when to review them based on recall quality using the SM-2 algorithm.

Stack
Layer → Technology
Algorithm → Python (SM-2)

Backend → FastAPI

Database → Supabase (PostgreSQL)

Frontend → HTML, CSS, JavaScript

Hosting → Render (backend + frontend)

Repository
GitHub: github.com/RizaRafeek/review-master

Live: https://review-master-1.onrender.com/index.html

Project Structure
review-master/

├── main.py          — FastAPI app and endpoints

├── database.py      — Supabase CRUD operations

├── topic.py         — SM-2 algorithm

├── index.html       — Home page (today's due topics)

├── topics.html      — Full topics list

├── style.css        — Deep space theme

├── requirements.txt — Python dependencies

└── .env             — Environment variables (not committed)

How It Works

User adds a topic via the frontend
Topic is saved to Supabase with next_review_date set to today
Each day, the home page shows topics due for review
User clicks a topic and rates recall from 1 to 5
SM-2 algorithm calculates the next review date based on the rating
Topic is updated in the database and removed from today's list


SM-2 Algorithm
The SM-2 algorithm adjusts two values per topic:
Easiness Factor (EF) — how easy the topic is (default 2.5)

Interval — days until next review
Rules:

Rating ≥ 3 → interval increases, EF stays or improves
Rating < 3 → interval resets to 1, review again tomorrow
Minimum EF is 1.3


API Endpoints
GET     /topics              — Get all topics

GET     /topics/{id}         — Get a single topic

POST    /add-topic?name=     — Add a new topic

GET     /review?id=&quality= — Submit a review rating

DELETE  /delete-topic?id=    — Delete a topic

Database Schema
Table: topics
id               — uuid    — Primary key

name             — text    — Topic name

easiness_factor  — float   — SM-2 EF value

interval         — int     — Days until next review

repetitions      — int     — Number of successful reviews

next_review_date — date    — Date of next review

Environment Variables
Set in Render dashboard and never committed to GitHub:
SUPABASE_URL=your_supabase_project_url

SUPABASE_KEY=your_supabase_key

Local Development
Terminal 1 — backend:

uvicorn main:app --reload
Terminal 2 — frontend:

python -m http.server 3000
Open: http://localhost:3000/index.html
CORS in main.py allows localhost:3000 and the Render frontend URL.

Deployment
Both services hosted on Render.
Backend → Render Web Service

Start command: uvicorn main:app --host 0.0.0.0 --port 10000
Frontend → Render Static Site

Publish directory: .
Environment variables are managed via Render dashboard and never committed to GitHub.

Dependencies
fastapi

uvicorn

supabase

python-dotenv