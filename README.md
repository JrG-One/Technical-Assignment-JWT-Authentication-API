# JWT Authentication API

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-5.2-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

A lightweight Django REST Framework API implementing JSON Web Token (JWT) authentication. Easily integrate secure login, token refresh, and validation endpoints into your projects.
This project was built under the assignment given by **Sharp Stakes**.

---

## 🚀 Features

* **User Authentication** with JWT (access + refresh tokens)
* **Token Refresh** and **Blacklist** (rotate & revoke)
* **Token Validation** endpoint returning user info and expiry
* **Dockerized** for consistent development & deployment
* **Publicly accessible**—no hardcoded credentials

---

## 🛠️ Tech Stack

* Python 3.11
* Django 5.2.4
* Django REST Framework
* `djangorestframework-simplejwt`
* SQLite (default) or any DB via `DATABASE_URL`
* Docker + Dockerfile

---

## 📦 Prerequisites

* Docker & Docker Compose (optional)
* Git

---

## 📝 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/jwt-auth-api.git
cd jwt-auth-api
```

### 2. Configure Environment

> **Note:** This service is publicly accessible—no sensitive creds are stored in code.

Create a `.env` file in the project root (optional override):

```env
SECRET_KEY=your_production_secret_key
DEBUG=False
DATABASE_URL=sqlite:///db.sqlite3
```

### 3. Build & Run with Docker

```bash
docker build -t jwt_auth_api .
docker run -d -p 8000:8000 \
  -e SECRET_KEY="$SECRET_KEY" \
  -e DEBUG="$DEBUG" \
  -e DATABASE_URL="$DATABASE_URL" \
  jwt_auth_api
```

### 4. Access the API

```
http://<your-host>:8000/api/auth/
```

| Endpoint     | Method | Description                        |
| ------------ | ------ | ---------------------------------- |
| `/login/`    | POST   | Obtain `access` & `refresh` tokens |
| `/refresh/`  | POST   | Rotate & obtain new access token   |
| `/verify/`   | POST   | Check if a given token is valid    |
| `/validate/` | GET    | Validate bearer token & user info  |

---

## 🔧 Usage Examples

### 1. Login

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
     -H 'Content-Type: application/json' \
     -d '{
       "username": "admin",
       "password": "adminpass"
     }'
```

**Response:**

```json
{
  "refresh": "<your_refresh_token>",
  "access": "<your_access_token>"
}
```

---

### 2. Refresh Token

```bash
curl -X POST http://localhost:8000/api/auth/refresh/ \
     -H 'Content-Type: application/json' \
     -d '{
       "refresh": "<your_refresh_token>"
     }'
```

**Response:**

```json
{
  "access": "<new_access_token>",
  "refresh": "<rotated_refresh_token>"
}
```

---

### 3. Validate Access Token

```bash
curl -X GET http://localhost:8000/api/auth/validate/ \
     -H 'Authorization: Bearer <your_access_token>'
```

**Response:**

```json
{
  "valid": true,
  "user": "admin",
  "expires": 1751953905
}
```

---

### 4. Verify Any Token

```bash
curl -X POST http://localhost:8000/api/auth/verify/ \
     -H 'Content-Type: application/json' \
     -d '{
       "token": "<any_jwt_token>"
     }'
```

**Response (valid):**

```json
{ "valid": true }
```

**Response (invalid):**

```json
{ "valid": false }
```

---

## 🧪 Example Test Case

Use the following test user to quickly verify your setup:

* **Username:** `TestUser`
* **Password:** `12345678`

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
     -H 'Content-Type: application/json' \
     -d '{
       "username": "TestUser",
       "password": "12345678"
     }'
```

You should receive a JSON response with both `access` and `refresh` tokens.

---
