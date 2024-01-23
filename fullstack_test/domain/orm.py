from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from fullstack_test.db_config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

engine = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)
Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()
