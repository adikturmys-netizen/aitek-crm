from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Замени username, password, localhost:5432 и aitek_crm на свои данные из pgAdmin
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Fedos1098@localhost:5432/aitek_crm"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()