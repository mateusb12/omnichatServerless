import json
from typing import List

from cruds.conversation_crud import get_all_conversations, update_conversation, update_multiple_conversations


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
    path = event["requestContext"]["http"]["path"].split("/")
    main_suffix = path[0]
    secondary_suffix = path[1] if len(path) > 1 else None
    available_operations = ["conversation_handler"]
    if main_suffix not in available_operations:
        return __get_standard_error_message(f'Invalid operation /{main_suffix}.'
                                            f' Only available operations are {available_operations}')
    return conversation_handler(path_list=path, http_method=http_method, event=event)


def conversation_handler(path_list: List[str], http_method: str, event: dict):
    available_operations = ["get_all_conversations", "update_conversation", "update_multiple_conversations"]
    suffix = path_list[-1]
    if suffix not in available_operations:
        return __get_invalid_method_error_message(path_list, available_operations)
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
