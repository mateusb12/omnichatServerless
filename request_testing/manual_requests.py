import json

import requests

BASE_URL = "https://us-central1-middleware-omnichat.cloudfunctions.net"
GET_ALL_CONVERSATIONS = "conversation_handler/get_all_conversations"
GET_ALL_ORDERS = "order_handler/read"


def test_all_conversations():
    base = BASE_URL
    suffix = GET_ALL_ORDERS
    url = f"{base}/{suffix}"
    response = requests.get(url)
    response_body = json.loads(response.text)
    response_body = json.dumps(response_body, ensure_ascii=False)

    # Print the status code and the response body
    print("Status code:", response.status_code)
    print("Response body:", response_body)


def __main():
    test_all_conversations()


if __name__ == '__main__':
    __main()
