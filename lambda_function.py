from data.dumb_import import dumb_import_function


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': dumb_import_function(),
        'headers': {
            'Content-Type': 'text/plain'
        }
    }