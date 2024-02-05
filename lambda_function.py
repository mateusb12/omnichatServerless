from data.dumb_import import dumb_import_function


def __get_last_segment(event):
    path = event['path']
    return path.split('/')


def lambda_handler(event, context):
    last_segment = __get_last_segment(event)
    return {
        'statusCode': 200,
        'body': last_segment + dumb_import_function(),
        'headers': {
            'Content-Type': 'text/plain'
        }
    }
