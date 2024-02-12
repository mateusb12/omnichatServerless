import json
from app import handler


def test_handler(method: str, path: str, body: dict) -> dict:
    event = {
        "requestContext": {
            "http": {
                "method": method,
                "path": path
            }
        },
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }
    response = handler(event, {})
    return response


def __main():
    pass


if __name__ == '__main__':
    __main()
