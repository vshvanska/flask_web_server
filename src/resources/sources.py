from flask import abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
from src.database import db_session
from src.schemas import SourceSchema
from ..models import SourceRecord
from ..utils.schema_validation import validate_schema


class SourceResource(MethodView):
    @validate_schema(SourceSchema)
    def post(self, data: dict):
        source = SourceRecord(**data)
        try:
            db_session.add(source)
            db_session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting data")
        response_data = (SourceSchema().dump(source))
        return response_data, 201
