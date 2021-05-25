from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

application_schema = {
    "type": "object",
    "properties": {
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "phone": {
            "type": "string",
            "pattern": "^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$"
        },
        "gradYear": {
            "type": "string"
        },
        "major": {
            "type": "string"
        },
        # "minor": {
        #     "type": "string"
        # },
        "linkedin": {
            "type": "string"
        },
        "website": {
            "type": "string"
        },
        "marketing": {
            "type": "string"
        }
    },
    "required": ["firstName", "lastName", "email", "phone", "gradYear", "major"],
    "additionalProperties": True
}

def validate_application(data):
    try:
        validate(data, application_schema)
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}