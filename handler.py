import base64
import json

from json_to_spreadsheet_template import SpreadsheetCreator


def generate(event, context):
    print(json.dumps(event))
    body = json.loads(event['body'])
    schema_uri = body['schema_uri']
    schema_types = body['schema_types']
    schema_modules = body['schema_modules']

    for index, schema_module in enumerate(schema_modules):
        schema_modules[index] = schema_uri + schema_module

    filename = body['output_filename']
    output = "/tmp/" + filename
    spreadsheet_creator = SpreadsheetCreator()
    spreadsheet_creator.generateSpreadsheet(schema_uri, schema_types, schema_modules, output)
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
