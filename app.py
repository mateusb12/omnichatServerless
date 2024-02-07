import json


def handler(event, context):
    return {"headers": {"Content-Type": "application/json"}, "statusCode": 200,
            "body": json.dumps({"message": "Lambda container image invoked", "event": event})}
