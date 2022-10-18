from email.policy import default

from marshmallow import fields, Schema, validates_schema, ValidationError

VALID_CMD_PARAMS = (
    'filter',
    'sort',
    'map',
    'unique',
    'limit',
    'regex'
)


class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate(self, values, *args, **kwargs):
        if values['cmd'] not in VALID_CMD_PARAMS:
            raise ValidationError('"cmd1" invalid value')
        return values


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
