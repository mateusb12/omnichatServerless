import json

from data.dumb_import import dumb_import_function


def __get_last_segment(event):
    path = event['path']
    return path.split('/')


def lambda_handler(event, context):
    body = json.loads(event['body'])
    required_params = ["transactionId", "type", "amount"]
    for item in required_params:
        if item not in event["queryStringParameters"]:
            return {'statusCode': 400, 'headers': {'Content-Type': 'application/json'},
                    'body': json.dumps({"message": f"missing query parameter: {item}"})}
    transactionId = event["queryStringParameters"]["transactionId"]
    transactionType = event["queryStringParameters"]["type"]
    transactionAmount = event["queryStringParameters"]["amount"]

    print("transactionId=" + transactionId)
    print("transactionType=" + transactionType)
    print("transactionAmount=" + transactionAmount)

    transactionResponse = {'transactionId': transactionId, 'type': transactionType, 'amount': transactionAmount,
                           'message': f"{body} Hello from Lambda land"}

    responseObject = {'statusCode': 200, 'headers': {'Content-Type': 'application/json'},
                      'body': json.dumps(transactionResponse)}
    return responseObject
