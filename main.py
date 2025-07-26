from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import generate_short_code
from models import Base, URLMap
from database import SessionLocal, engine
from fastapi.responses import RedirectResponse


Base.metadata.create_all(bind=engine)

app = FastAPI()

class URLRequest(BaseModel):
    original_url: str

@app.post("/shorten")
def shorten_url(request: URLRequest):
    db = SessionLocal()
    short_code = generate_short_code()
    db_url = URLMap(short_code=short_code, original_url=request.original_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db.close()
    return {"short_url": f"http://localhost:8000/r/{short_code}"}

@app.get("/r/{short_code}")
def redirect_url(short_code: str):
    db = SessionLocal()
    url_entry = db.query(URLMap).filter(URLMap.short_code == short_code).first()
    db.close()
    if url_entry:
        return RedirectResponse(url=url_entry.original_url)
    else:
        raise HTTPException(status_code=404, detail="Short URL not found")
