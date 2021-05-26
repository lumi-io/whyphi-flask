from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

create_posting_schema = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "aboutUs": {
            "type": "string"
        },
        "qualifications": {
            "type": "string"
        },
        "essay": {
            "type": "array"
        },
        "deadline": {
            "type": "string",
            "format": "date-time" # 2020-09-15T23:59:99+00:00
        },
        "isVisible": {
            "type": "boolean"
        }

    },
    "required": ["title", "aboutUs", "qualifications", "deadline", "isVisible"],
    "additionalProperties": False
}


def validate_create_posting_schema(data):
    try:
        validate(data, create_posting_schema)
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}

def validate_edit_posting_schema(data):
    try:
        validate(data, create_posting_schema)
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}