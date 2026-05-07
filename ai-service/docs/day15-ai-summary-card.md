# AI Developer 2 - Day 15 Summary Card

## Project Name
SentinelIQ AI Service

---

## 1. Project Overview
SentinelIQ AI Service is a Flask-based AI backend system that integrates with Groq API to provide real-time AI-generated responses through REST API endpoints.

This system demonstrates lightweight, scalable AI inference using modern LLM integration.

---

## 2. Tech Stack

- Python
- Flask (Backend API)
- Groq API (LLM Integration)
- Requests (Testing API)
- dotenv (Environment variables)
- Git & GitHub (Version control)

---

## 3. API Endpoints

### 1. /generate (POST)
- Accepts user prompt in JSON format
- Returns AI-generated response

**Example Input:**
```json
{
  "prompt": "Explain dark mode UI"
}