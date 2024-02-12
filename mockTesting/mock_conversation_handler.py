from mockTesting.main_testing import test_handler


def test_get_all_conversations():
    method = "GET"
    path = "/conversation_handler/get_all_conversations"
    body = {}
    res = test_handler(method, path, body)
    return res


def test_update_conversation():
    method = "PUT"
    path = "/conversation_handler/update_conversation"
    body = {"phoneNumber": "558599663533", "isBotActive": False}
    res = test_handler(method, path, body)
    return res


def test_update_multiple_conversations():
    method = "PUT"
    path = "/conversation_handler/update_multiple_conversations"
    body = {"metaData": {"ip": "127.0.0.0",
                         "sender": "John",
                         "phoneNumber": "558599663533"},
            "userMessage": "Hello, I need help with my order",
            "botAnswer": "Hello, how can I help you?"
            }
    res = test_handler(method, path, body)
    return res


def __main():
    res = test_update_multiple_conversations()
    print(res)
    return res


if __name__ == '__main__':
    __main()
