from flask import abort, Response
from flask.views import MethodView
from marshmallow import ValidationError
from app.schemas import SourceSchema
from .source_repository import SourceRepository
from ..utils.schema_validation import validate_schema


class CreateSourceResource(MethodView):
    repository = SourceRepository()

    @validate_schema(SourceSchema)
    def post(self, data: dict):
        try:
            instance = self.repository.create_instance(data)
        except RuntimeError as e:
            abort(Response(f"An error occurred while inserting data: {e}", 500))
        except ValidationError as e:
            abort(Response(str(e), 400))
        response_data = (SourceSchema().dump(instance))
        return response_data, 201


class SourceResource(MethodView):
    repository = SourceRepository()

    def get(self, domain):
        instance = self.repository.get_instance(domain=domain)
        print(instance)
        if not instance:
            abort(Response("Instance not found", 404))
        response_data = (SourceSchema().dump(instance))
        return response_data, 200

    def delete(self, domain):
        try:
            self.repository.delete_instance(domain=domain)
        except ValidationError as e:
            abort(Response(str(e), 404))
        return {"message": "Deleted succesfully"}, 200
