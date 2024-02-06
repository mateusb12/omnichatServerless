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


def lambda_handler(event, context) -> dict:
    headers = event["headers"]
    http_method = event['requestContext']['http']['method']
    path = event["requestContext"]["http"]["path"].split("/")
    available_operations = ["get_all_conversations", "update_conversation", "update_multiple_conversations"]
    suffix = path[-1]
    if suffix not in available_operations:
        return __get_invalid_method_error_message(path, available_operations)
    operation_dict = {
        "get_all_conversations": ("GET", get_all_conversations),
        "update_conversation": ("PUT", update_conversation),
        "update_multiple_conversations": ("PUT", update_multiple_conversations)
    }
    required_method, operation_func = operation_dict[suffix]
    if required_method != http_method:
        return __get_standard_error_message(f'Only {required_method} requests are accepted for the operation {suffix}')
    result = operation_func()
    return {"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": json.dumps(result)}
    # return {"statusCode": 200,
    #         "headers": {
    #             "Content-Type": "text/html",
    #         },
    #         "body":
    #             f"""
    #             <h1> Query string parameters </h1>
    #             <p> {headers} </p>
    #             <br>
    #             <h1> Path </h1>
    #             <p> {path} </p>
    #             <br>
    #             <h1> Http method </h1>
    #             <p> {http_method} </p>
    #             <br>
    #             <h1> First suffix </h1>
    #             <p> {suffix} </p>
    #             """}
