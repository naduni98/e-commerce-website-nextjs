from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Load database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@db:3306/mydatabase")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for models
Base = declarative_base()

# Metadata for migrations
metadata = MetaData()
