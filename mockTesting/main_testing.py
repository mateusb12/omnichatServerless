import json
from main import order_handler, fulfillment_endpoint
from mockTesting.mock_utils.mock_templates import mock_order_1, fulfillment_mock
from mockTesting.mock_utils.mock_object import MockRequest


def __test_order_handler(headers: dict) -> dict:
    mock_request3 = MockRequest(path="/order_handler/read", method="GET", headers=headers, json_data=mock_order_1)
    response3 = order_handler(mock_request3)
    return json.loads(response3.data.decode('utf-8'))


def __test_fulfillment_endpoint(headers: dict):
    fulfillment_request = MockRequest(path="/webhook", method="GET", headers=headers, json_data=fulfillment_mock)
    return fulfillment_endpoint(fulfillment_request)


def __main():
    headers = {
        "Content-Type": "application/json"
    }
    res = __test_fulfillment_endpoint(headers)
    print(res)


if __name__ == '__main__':
    __main()
