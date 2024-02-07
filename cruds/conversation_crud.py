import datetime
import json
from typing import List

from factory.core_instantiations import fcm
from utils.cloudFunctionsUtils import log_memory_usage
from utils.corsBlocker import createResponseWithAntiCorsHeaders


def get_all_conversations(body=None) -> List[str]:
    conversations = fcm.getAllConversations()
    arrayOfConversations = list(conversations.values()) if conversations is not None else ["None"]
    return arrayOfConversations


def update_conversation(body=None):
    positive_response = 'conversation updated successfully'
    negative_response = 'error updating conversation, conversation does not exist'
    response = positive_response if fcm.updateConversation(body) else negative_response
    response_code = 200 if positive_response else 500
    return {"response": response, "statusCode": response_code}


def update_multiple_conversations(request=None):
    try:
        payload = request.get_json()
        userMessage = payload["userMessage"]
        botAnswer = payload["botAnswer"]
        metaData = payload["metaData"]
        metaData.pop("userMessage")
        phoneNumber = metaData["phoneNumber"]
        userMessageDict = {"body": userMessage, "timestamp": datetime.datetime.now().strftime('%d-%b-%Y %H:%M'), **metaData}
        botMessageDict = {"body": botAnswer, "timestamp": datetime.datetime.now().strftime('%d-%b-%Y %H:%M'),**metaData,
                          "sender": "Bot"}
        messagePot = [userMessageDict, botMessageDict]

        result = fcm.appendMultipleMessagesToWhatsappNumber(messagesData=messagePot, whatsappNumber=phoneNumber)
        response_code = 200 if result is True else 500
        final_response = json.dumps({'response': 'messages appended successfully'}), response_code

        return createResponseWithAntiCorsHeaders(final_response)

    except Exception as e:
        return createResponseWithAntiCorsHeaders((json.dumps({'error': f"An error occurred: {str(e)}"}), 500))
