mock_order_1 = {
    "address": "Rua da Justiça 9584",
    "communication": "Janderson@bol.com.br",
    "customerName": "Janderson",
    "observation": "Tirar cebola",
    "orderItems": [
        {
            "type": "pizza",
            "flavors": ["Portuguesa"],
            "size": "Large",
            "quantity": 1,
            "price": 15.00
        },
        {
            "type": "drink",
            "flavors": ["Coca-Cola"],
            "size": "2L",
            "quantity": 1,
            "price": 2.50
        },
        {
            "type": "pizza",
            "flavors": ["Margarita", "Frango com Catupiry"],
            "size": "Large",
            "quantity": 1,
            "price": 17.00
        }
    ],
    "platform": "WhatsApp",
    "status": "Confirmado",
}

mock_order_2 = {
    "address": "Rua Marcos Macedo 700",
    "communication": "558599663533",
    "customerName": "Mateus",
    "observation": "None",
    "orderItems": [
        {
            "type": "pizza",
            "flavors": ["Portuguesa"],
            "size": "Large",
            "quantity": 1,
            "price": 15.00
        },
        {
            "type": "drink",
            "flavors": ["Guaraná"],
            "size": "2L",
            "quantity": 1,
            "price": 2.50
        },
        {
            "type": "pizza",
            "flavors": ["Margarita", "Frango com Catupiry"],
            "size": "Large",
            "quantity": 1,
            "price": 17.00
        }
    ],
    "platform": "WhatsApp",
    "status": "Em preparação",
}

update_mult_conv_mock = {
    'botAnswer': 'Não foi possível se conectar ao fulfillment do dialogflow! Por favor, ligue a API',
    'metaData': {
        'from': ['whatsapp', '+558599663533'],
        'phoneNumber': '558599663533',
        'sender': 'Tiago',
        'userMessage': 'oi'},
    'userMessage': 'oi'
}

fulfillment_mock = {
        "responseId": "29fa6bc5-391f-49c6-b987-a0801e1d40bb-1838fa0d",
        "queryResult": {
            "queryText": "Oii",
            "action": "input.welcome",
            "parameters": {

            },
            "allRequiredParamsPresent": True,
            "fulfillmentText": "Não foi possível se conectar ao fulfillment do dialogflow! Por favor, ligue a API",
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Não foi possível se conectar ao fulfillment do dialogflow! Por favor, ligue a API"
                        ]
                    }
                }
            ],
            "outputContexts": [
                {
                    "name": "projects/catupirybase/locations/global/agent/sessions/859e5892-b2c2-6027-0334-00c272efcbf4/contexts/__system_counters__",
                    "parameters": {
                        "no-input": 0.0,
                        "no-match": 0.0
                    }
                }
            ],
            "intent": {
                "name": "projects/catupirybase/locations/global/agent/intents/acd8e087-5400-4cf9-95f3-4c681b16b516",
                "displayName": "Welcome"
            },
            "intentDetectionConfidence": 1.0,
            "languageCode": "pt-br",
            "sentimentAnalysisResult": {
                "queryTextSentiment": {
                    "score": 0.3,
                    "magnitude": 0.3
                }
            }
        },
        "originalDetectIntentRequest": {
            "source": "DIALOGFLOW_CONSOLE",
            "payload": {

            }
        },
        "session": "projects/catupirybase/locations/global/agent/sessions/859e5892-b2c2-6027-0334-00c272efcbf4"
    }
