# Review Master

A spaced repetition study scheduler built with Python and FastAPI. Users add lecture topics, and the system schedules reviews using the SM-2 algorithm based on recall quality.

🔗 **Live:** https://review-master-1.onrender.com/index.html

---

## Stack

| Layer | Technology |
|---|---|
| Algorithm | Python (SM-2) |
| Backend | FastAPI |
| Database | Supabase (PostgreSQL) |
| Frontend | HTML, CSS, JavaScript |
| Hosting | Render |

---

## How It Works

1. User adds a topic via the frontend
2. Topic is saved to Supabase with `next_review_date` set to today
3. Each day, the home page shows topics due for review
4. User clicks a topic and rates recall from 1 to 5
5. SM-2 algorithm calculates the next review date based on the rating
6. Topic is updated in the database and removed from today's list

---

## SM-2 Algorithm

Adjusts two values per topic:

- **Easiness Factor (EF)** — how easy the topic is (default 2.5)
- **Interval** — days until next review

Rules:
- Rating ≥ 3 → interval increases
- Rating < 3 → interval resets to 1, review again tomorrow
- Minimum EF is 1.3

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/topics` | Get all topics |
| GET | `/topics/{id}` | Get a single topic |
| POST | `/add-topic?name=` | Add a new topic |
| GET | `/review?id=&quality=` | Submit a review rating |
| DELETE | `/delete-topic?id=` | Delete a topic |

---

## Database Schema

| Column | Type | Description |
|---|---|---|
| id | uuid | Primary key |
| name | text | Topic name |
| easiness_factor | float | SM-2 EF value |
| interval | int | Days until next review |
| repetitions | int | Successful review count |
| next_review_date | date | Date of next review |

---

## Local Development

```bash
# Terminal 1 — backend
uvicorn main:app --reload

# Terminal 2 — frontend
python -m http.server 3000
```

Open `http://localhost:3000/index.html`

---

## Deployment

- **Backend** → Render Web Service
- **Frontend** → Render Static Site
- Environment variables managed via Render dashboard, never committed to GitHub

---

## Dependencies

```
fastapi
uvicorn
supabase
python-dotenv
```