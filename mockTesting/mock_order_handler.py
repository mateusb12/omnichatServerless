from mockTesting.main_testing import test_handler


def test_create_order():
    method = "POST"
    path = "/order_handler/create_order"
    orderItems = [{"price": 30, "quantity": 1, "size": "medium", "flavors": ["Pepperoni"], "type": "pizza"},
                  {"price": 12.5, "quantity": 1, "size": "2L", "flavors": ["Coca-Cola"], "type": "drink"},
                  {"price": 10, "quantity": 1, "size": "small", "flavors": ["Chocolate"], "type": "dessert"}]
    body = {"customerName": "Wellington", "status": "pending", "address": "Rua do Verão", "platform": "whatsapp",
            "communication": "welly_10@gmail.com", "orderItems": orderItems}
    res = test_handler(method, path, body)
    return res


ORDER_UNIQUE_ID = "01_Dec_2023_15_15_08_550"


def test_read_order():
    method = "GET"
    path = "/order_handler/read_order"
    body = {"unique_id": ORDER_UNIQUE_ID}
    res = test_handler(method, path, body)
    return res


def test_update_order():
    method = "PUT"
    path = "/order_handler/update_order"
    body = {"unique_id": ORDER_UNIQUE_ID, "status": "delivered"}
    res = test_handler(method, path, body)
    return res


def test_delete_order():
    method = "DELETE"
    path = "/order_handler/delete_order"
    body = {"unique_id": ORDER_UNIQUE_ID}
    res = test_handler(method, path, body)
    return res


def __main():
    res = test_read_order()
    print(res)
    return res


if __name__ == '__main__':
    __main()
