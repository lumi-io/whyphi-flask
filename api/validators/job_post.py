from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

job_schema = {
    "type": "object",
    "properties": {
        "isVisible": {
            "type": "boolean"
        },
        "title": {
            "type": "string"
        },
        "aboutUs": {
            "type": "string"
        },
        "qualifications": {
            "type": "array"
        },
        "deadline": {
            "type": "string",
            "format": "date-time"
        },
        "essay": {
            "type": "array"
        }

    },
    "required": ["isVisible", "title", "aboutUs", "qualifications", "deadline", "essay"],
    "additionalProperties": False
}


def validate_job(data):
    try:
        validate(data, job_schema)
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}