# FastAPI URL Shortener

A simple URL shortener application built using **FastAPI**, **SQLite**, and **SQLAlchemy**.  

Create Virtual Environment & Activate

python -m venv venv
# Activate venv
# On Windows:
venv\Scripts\activate


POST /shorten
{
  "original_url": "https://www.google.com"
}


Response:
{
  "short_url": "http://localhost:8000/r/abc123"
}
