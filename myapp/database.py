import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Resolve the database URL.  If the environment variable DATABASE_URL is set we
# use it, otherwise default to the bundled SQLite database.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///movie_recommender.db")

# Create the engine for sqlite
engine = create_engine(
    DATABASE_URL,
    connect_args= {"check_same_thread": False} #It allows multiple threads to use the same database connection, which SQLite does not allow by default.
    )

# Create the local session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Import models here so that Base is defined before calling create_all
from myapp.models import Base

# Ensure all tables are created when the application starts.  This
# allows running the API without manually invoking the sql_load script
# when using a fresh database.
Base.metadata.create_all(bind=engine)

'''
Python file to create database connection and session
'''