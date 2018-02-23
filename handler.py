import base64
import json

from json_to_spreadsheet_template import SpreadsheetCreator


def generate(event, context):
    print(json.dumps(event))
    body = json.loads(event['body'])
    print(json.dumps(body))
    schema_base_uri = body['schema_base_uri']
    schema_types = body['schema_types']
    schema_modules = body['schema_modules']
    filename = body['output_filename']
    output = "/tmp/" + filename
    spreadsheet_creator = SpreadsheetCreator()
    spreadsheet_creator.generate_spreadsheet(schema_base_uri, schema_types, schema_modules, output)
    with open(output, "rb") as output_file:
        encoded_string = base64.b64encode(output_file.read())

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "Content-Disposition": "inline; filename=" + filename
        },
        "body": str(encoded_string.decode("utf-8")),
        "isBase64Encoded": True
    }
    return response
