import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

load_dotenv()

database_url = os.getenv("DATABASE_URL")
test_database = os.getenv("TEST_DATABASE_URL")
Base = declarative_base()


class DatabaseSession:
    _session = None
    _engine = None

    @classmethod
    def create_engine(cls, database_url):
        cls._engine = create_engine(database_url)
        cls._session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=cls._engine))
        Base.metadata.bind = cls._engine

    @classmethod
    def get_session(cls):
        if not cls._session:
            raise RuntimeError("DatabaseSession not initialized")
        return cls._session

    @classmethod
    def create_tables(cls):
        if not cls._engine:
            raise RuntimeError("DatabaseSession not initialized")
        Base.metadata.create_all(cls._engine)

    @classmethod
    def drop_tables(cls):
        if not cls._engine:
            raise RuntimeError("DatabaseSession not initialized")
        Base.metadata.drop_all(cls._engine)
