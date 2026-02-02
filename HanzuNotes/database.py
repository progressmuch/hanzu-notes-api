from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"},  # sslmode is the one used when using Supabase
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Function to talk with the Database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
