from sqlalchemy.orm import Session, sessionmaker
from app.database.database import engine


SessionLocal = sessionmaker(
    bind= engine,
    autocommit = False,
    autoflush = False
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
