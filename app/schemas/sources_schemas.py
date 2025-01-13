from marshmallow import Schema, fields
from marshmallow.validate import OneOf

from app.enums import VerdictEnum


class SourceSchema(Schema):
    domain = fields.String(required=True)
    verdict = fields.Function(required=True,
                              serialize=lambda obj: obj.verdict.value,
                              deserialize=lambda val: val,
                              validate=OneOf(
                               [verdict.value for verdict in VerdictEnum]),
                              )
