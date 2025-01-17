import os

from dotenv import load_dotenv
from flask import Flask
from app.database import DatabaseSession
from .resources import CreateSourceResource, SourceResource

load_dotenv()

def create_app(test_mode=False):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    if test_mode:
        database_url = os.getenv("TEST_DATABASE_URL")
    else:
        database_url = os.getenv("DATABASE_URL")

    DatabaseSession.create_engine(database_url)
    DatabaseSession.create_tables()

    #init_db()
    app.add_url_rule('/sources', view_func=CreateSourceResource.as_view('create-source'))
    app.add_url_rule('/sources/<string:domain>', view_func=SourceResource.as_view('source'))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
