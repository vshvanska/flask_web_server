from flask import Flask
from .resources import CreateSourceResource, SourceResource
from .database import init_db




def create_app():
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True


    init_db()
    app.add_url_rule('/sources', view_func=CreateSourceResource.as_view('create-source'))
    app.add_url_rule('/sources/<string:domain>', view_func=SourceResource.as_view('source'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
