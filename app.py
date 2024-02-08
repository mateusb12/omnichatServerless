import json
from typing import List

from cruds.conversation_crud import get_all_conversations, update_conversation, update_multiple_conversations
from cruds.order_crud import create_order, get_order_handler, update_order, delete_order


def __get_standard_error_message(msg: str):
    return {"statusCode": 400,
            "headers": {
                "Content-Type": "text/plain",
            },
            "body": msg}


def __get_invalid_method_error_message(path_list: List[str], method_list: List[str]):
    tag = "/".join(filter(None, path_list))
    msg = f"'/{tag}' is an invalid operation! Valid operations are "
    for item in method_list:
        msg += f"'/{item}', "
    msg = msg[:-2]
    return __get_standard_error_message(msg)


def handler(event, context):
    headers = event["headers"] if "headers" in event else {}
    http_method = event['requestContext']['http']['method']
    path = event["requestContext"]["http"]["path"].split("/")[1:]
    main_suffix = path[0]
    secondary_suffix = path[1] if len(path) > 1 else None
    available_operations = ["conversation_handler", "order_handler"]
    if main_suffix not in available_operations:
        return __get_standard_error_message(f'Invalid operation /{main_suffix}.'
                                            f' Only available operations are {available_operations}')
    if main_suffix == "conversation_handler":
        return conversation_handler(path_list=path, http_method=http_method, event=event)
    elif main_suffix == "order_handler":
        return order_handler(path_list=path, http_method=http_method, event=event)


def conversation_handler(path_list: List[str], http_method: str, event: dict):
    available_operations = ["get_all_conversations", "update_conversation", "update_multiple_conversations"]
    suffix = path_list[-1]
    if suffix not in available_operations:
        return __get_invalid_method_error_message(path_list=path_list, method_list=available_operations)
    operation_dict = {
        "get_all_conversations": ("GET", get_all_conversations),
        "update_conversation": ("PUT", update_conversation),
        "update_multiple_conversations": ("PUT", update_multiple_conversations)
    }
    required_method, operation_func = operation_dict[suffix]
    if required_method != http_method:
        return __get_standard_error_message(f'Only {required_method} requests are accepted for the operation {suffix}')
    body = json.loads(event["body"]) if "body" in event else {}
    content, reason, response_code = operation_func(body)
    return {"headers": {"Content-Type": "application/json"}, "statusCode": response_code,
            "body": json.dumps(content) if content else json.dumps(reason)}


def order_handler(path_list: List[str], http_method: str, event: dict):
    available_operations = ["create_order", "read_order", "update_order", "delete_order"]
    suffix = path_list[-1]
    if suffix not in available_operations:
        return __get_invalid_method_error_message(path_list=path_list, method_list=available_operations)
    operation_dict = {
        "create_order": ("POST", create_order),
        "read_order": ("GET", get_order_handler),
        "update_order": ("PUT", update_order),
        "delete_order": ("DELETE", delete_order)
    }
    required_method, operation_func = operation_dict[suffix]
    if required_method != http_method:
        return __get_standard_error_message(f'Only {required_method} requests are accepted for the operation {suffix}')
    body = json.loads(event["body"]) if "body" in event else {}
    content, reason, response_code = operation_func(body)
    return {"headers": {"Content-Type": "application/json"}, "statusCode": response_code,
            "body": json.dumps(content) if content else json.dumps(reason)}
