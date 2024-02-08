import datetime
import json
from typing import List, Tuple

from factory.core_instantiations import fcm
from utils.cloudFunctionsUtils import log_memory_usage
from utils.corsBlocker import createResponseWithAntiCorsHeaders


def get_all_conversations(body=None) -> Tuple[List[str], str, int]:
    conversations = fcm.getAllConversations()
    arrayOfConversations = list(conversations.values()) if conversations is not None else ["None"]
    return arrayOfConversations, "Conversations retrieved successfully", 200


def update_conversation(body=None) -> Tuple[any, str, int]:
    reason, result = fcm.updateConversation(body)
    response_code = 200 if result else 404
    content = None
    return content, reason, response_code


def update_multiple_conversations(body=None) -> Tuple[any, str, int]:
    """Example body json
    {"metaData": {"ip": "127.0.0.0", "sender": "John", "phoneNumber": "+558599663533"},
    "userMessage": "Hello, I need help with my order",
    "botAnswer": "Hello, how can I help you?"}
    """
    if "metaData" not in body:
        return None, "'metaData' value not found in the request json", 400
    if "userMessage" not in body:
        return None, "'userMessage' value not found in the request json", 400
    if "botAnswer" not in body:
        return None, "'botAnswer' value not found in the request json", 400
    required_metadata_values = ["ip", "sender", "phoneNumber"]
    for item in required_metadata_values:
        if item not in body["metaData"]:
            return None, f"body['metadata']['{item}'] value not found in the request json", 400
    try:
        userMessage = body["userMessage"]
        botAnswer = body["botAnswer"]
        metaData = body["metaData"]
        phoneNumber = metaData["phoneNumber"]
        timestamp = datetime.datetime.now().strftime('%d-%b-%Y %H:%M')
        userMessageDict = {"body": userMessage, "timestamp": timestamp, **metaData}
        botMessageDict = {"body": botAnswer, "timestamp": timestamp, **metaData, "sender": "Bot"}
        messagePot = [userMessageDict, botMessageDict]

        response_code, reason = fcm.appendMultipleMessagesToWhatsappNumber(messagesData=messagePot,
                                                                           whatsappNumber=phoneNumber)
        return None, reason, response_code

    except Exception as e:
        return None, str(e), 500
