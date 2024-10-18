# Step 1: Import Required Libraries
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Step 2: Define the MySQL Database URL
# Step 2: Define the SQLite Database URL
DATABASE_URL = "sqlite:///./test.db"

# Step 3: Create the Engine
engine = create_engine(DATABASE_URL)

# Step 4: Create SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Step 5: Define the Base Class
Base = declarative_base()

# Step 6: Define the Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()