from data.dumb_import import dumb_import_function


def __get_last_segment(event):
    path = event['path']
    return path.split('/')


def lambda_handler(event, context):
    last_segment = dict(event)
    return {
        'statusCode': 200,
        'body': "last_segment",
        'headers': {
            'Content-Type': 'text/plain'
        }
    }
