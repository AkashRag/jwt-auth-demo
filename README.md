# 🔐 JWT Authentication API

A FastAPI-based authentication system implementing industry-standard JWT (JSON Web Token) security.

## 🚀 Features

- **User Registration** — Secure password hashing using bcrypt
- **Login** — JWT access token generation
- **Protected Routes** — Token-based authentication using OAuth2 + JWT

## 🛠️ Tech Stack

- **FastAPI** — Backend framework
- **python-jose** — JWT token creation & verification
- **passlib (bcrypt)** — Password hashing
- **Pydantic** — Request validation

## 📋 API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|----------------|
| POST | `/register` | Register new user | ❌ |
| POST | `/login` | Login & get JWT token | ❌ |
| GET | `/profile` | Get user profile | ✅ |

## 🔄 How It Works

1. **Register** → Password hashed with bcrypt → stored
2. **Login** → Password verified → JWT token issued (30 min expiry)
3. **Protected Route** → Token verified → Access granted/denied

## 🧪 Testing

```bash
# Register
curl -X POST http://127.0.0.1:8000/register -H "Content-Type: application/json" -d '{"Username":"akash","password":"test123"}'

# Login
curl -X POST http://127.0.0.1:8000/login -H "Content-Type: application/json" -d '{"Username":"akash","password":"test123"}'

# Access protected route
curl http://127.0.0.1:8000/profile -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## 📦 Setup

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

---

**Built by [Akash Raghuwanshi](https://github.com/AkashRag)** | Part of AI Automation Engineering portfolio
