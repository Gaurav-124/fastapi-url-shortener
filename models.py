from sqlalchemy import Column, Integer, String
from database import Base

class URLMap(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String, unique=True, index=True)
    original_url = Column(String)


