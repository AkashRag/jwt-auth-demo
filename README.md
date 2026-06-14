# 🔐 JWT Authentication API with Supabase

A production-ready authentication system built with FastAPI — featuring JWT tokens, bcrypt password hashing, and real PostgreSQL database via Supabase.

## 🚀 Live Demo
👉 Coming soon (Railway deploy in progress)

## 🛠️ Tech Stack
- **FastAPI** — Backend framework
- **Supabase (PostgreSQL)** — Real database for user storage
- **python-jose** — JWT token generation & verification
- **passlib (bcrypt)** — Password hashing
- **Pydantic** — Request validation
- **Railway** — Deployment

## ✅ API Endpoints

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/register` | ❌ | Register new user (bcrypt hashed) |
| POST | `/login` | ❌ | Login + get JWT token |
| GET | `/profile` | ✅ | Protected route — token required |

## 🔄 How It Works
Register → bcrypt hash → save to Supabase DB

Login → fetch from Supabase → verify hash → JWT token

Protected Route → verify JWT → access granted/denied

## ⚙️ Setup Locally

```bash
git clone https://github.com/AkashRag/jwt-auth-demo.git
cd jwt-auth-demo
pip install -r requirements.txt
```

Create `.env` file:
SUPABASE_URL=your_url

SUPABASE_KEY=your_key

Run:
```bash
python -m uvicorn main:app --reload
```

Open: `http://127.0.0.1:8000/docs`

## 🔐 Security Features
- Passwords never stored as plain text — bcrypt hashing
- JWT tokens expire in 30 minutes
- Protected routes require valid Bearer token
- Credentials stored in environment variables

---
**Built by [Akash Raghuwanshi](https://github.com/AkashRag)** | AI Automation Engineering Portfolio
