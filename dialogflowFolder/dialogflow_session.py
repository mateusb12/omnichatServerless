import os
from dotenv import load_dotenv
from google.cloud.dialogflow_v2 import DetectIntentResponse
import google.cloud.dialogflow_v2 as dialogflow
from dialogflowFolder.dialogflow_auth import getDialogflowCredentials


class DialogflowSession:
    def __init__(self):
        creds = getDialogflowCredentials()
        self.sessionClient = dialogflow.SessionsClient(credentials=creds)
        self.session = None
        self.agentName = None

    def initialize_session(self, user_id: str):
        if self.session is None and self.agentName is None:
            self.session = self.sessionClient.session_path(os.environ["SDK_PROJECT_ID"], user_id)
            self.agentName = self.session.split('/')[1]

    def getDialogFlowResponse(self, message: str, intent_name: str = None,
                                    user_number: str = None) -> DetectIntentResponse:
        session = self.session
        session_params = dialogflow.types.QueryParameters(payload={"phone-number": user_number})
        if intent_name:
            session = f"{self.session}/contexts/{intent_name}"
        textInput = dialogflow.types.TextInput(text=message, language_code='pt-BR')
        queryInput = dialogflow.types.QueryInput(text=textInput)
        requests = dialogflow.types.DetectIntentRequest(
            session=session, query_input=queryInput, query_params=session_params
        )
        response = self.sessionClient.detect_intent(request=requests)
        return response


def __run_multiple_messages():
    ds = DialogflowSession()
    response_dict = {}
    message_pool = ["Oi", "Vou querer duas pizzas de frango", "Sim", "Vou querer um guaraná", "Pix"]
    for message in message_pool:
        response = ds.getDialogFlowResponse(message=message)
        bot_answer = response.query_result.fulfillment_text
        response_dict[message] = bot_answer
    return response_dict


def __main():
    load_dotenv()
    ds = DialogflowSession()
    ds.initialize_session("123")
    response = ds.getDialogFlowResponse(message="Oi")
    text = response.query_result.fulfillment_text
    print(text)


if __name__ == "__main__":
    __main()
