from flask import abort, Response
from flask.views import MethodView
from marshmallow import ValidationError

from app.schemas import SourceSchema
from .source_repository import SourceRepository
from ..utils.schema_validation import validate_schema


class SourceResource(MethodView):
    repository = SourceRepository()

    @validate_schema(SourceSchema)
    def post(self, data: dict):
        try:
            instance = self.repository.create_instance(data)
        except RuntimeError as e:
            abort(Response("An error occurred while inserting data", 500))
        except ValidationError as e:
            abort(Response(str(e), 400))
        response_data = (SourceSchema().dump(instance))
        return response_data, 201
