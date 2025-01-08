from flask import abort, request
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
from src.database import db_session
from src.schemas import SourceSchema
from ..models import SourceRecord


class SourceResource(MethodView):

    def post(self):
        """

        :return:
        """
        source = SourceRecord(domain=request.values.get('domain'), verdict=request.values.get('verdict'))
        try:
            db_session.add(source)
            db_session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting data")
        response_data = (SourceSchema().dump(source))
        return response_data, 201
