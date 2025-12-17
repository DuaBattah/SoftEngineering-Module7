import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv


load_dotenv()

# Prefer explicit DATABASE_URL from environment. If not set and we're running tests,
# fall back to an in-memory SQLite DB so tests won't try to connect to an external Postgres host.
env_db = os.getenv('DATABASE_URL')
is_pytest = 'PYTEST_CURRENT_TEST' in os.environ or any('pytest' in arg for arg in sys.argv)

if env_db:
	DATABASE_URL = env_db
elif is_pytest:
	DATABASE_URL = 'sqlite:///:memory:'
else:
	DATABASE_URL = 'postgresql://myuser:mypassword@localhost/myappdb'


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()