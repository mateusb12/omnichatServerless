import json

from app import handler


def __test_handler(method: str, path: str, body: dict) -> dict:
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


def __test_get_all_conversations():
    method = "GET"
    path = "/conversation_handler/get_all_conversations"
    body = {}
    res = __test_handler(method, path, body)
    return res


def __test_create_order():
    method = "POST"
    path = "/order_handler/create_order"
    orderItems = [{"price": 30, "quantity": 1, "size": "medium", "flavors": ["Pepperoni"], "type": "pizza"},
                  {"price": 12.5, "quantity": 1, "size": "2L", "flavors": ["Coca-Cola"], "type": "drink"},
                  {"price": 10, "quantity": 1, "size": "small", "flavors": ["Chocolate"], "type": "dessert"}]
    body = {"customerName": "Wellington", "status": "pending", "address": "Rua do Verão", "platform": "whatsapp",
            "communication": "welly_10@gmail.com", "orderItems": orderItems}
    res = __test_handler(method, path, body)
    return res


def __main():
    res = __test_create_order()
    print(res)


if __name__ == '__main__':
    __main()
