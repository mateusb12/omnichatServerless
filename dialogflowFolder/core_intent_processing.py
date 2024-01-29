import logging

from starlette.responses import JSONResponse
from dialogflowFolder.dialogflow_utils import sendWebhookCallback, structureNewDialogflowContext
from factory.core_instantiations import menuHandler


def fulfillment_processing(requestContent) -> JSONResponse:
    print("FULFILLMENT ENDPOINT!")
    outputContexts = requestContent['queryResult']['outputContexts']
    menuHandler.params["baseContextName"] = outputContexts[0]['name'].rsplit('/contexts/', 1)[0]
    queryText = requestContent['queryResult']['queryText']
    print("@@@ QUERY_TEXT → " + queryText)
    userMessage = [item["name"] for item in queryText] if isinstance(queryText, list) else queryText
    currentIntent = requestContent['queryResult']['intent']['displayName']
    logging.info(f"current Intent: {currentIntent}")
    params = requestContent['queryResult']['parameters']
    if currentIntent == "Order.drink":
        # return __handleOrderDrinkIntent(params, userMessage)
        return sendWebhookCallback("Order.drink")
    elif currentIntent == "Order.pizza - drink no":
        # params = menuHandler.params
        # fullOrder = buildFullOrder(params)
        # totalPriceDict = menuHandler.analyzeTotalPriceWithMenuPrices(fullOrder)
        # finalMessage = totalPriceDict["finalMessage"]
        # return sendWebhookCallback(finalMessage)
        return sendWebhookCallback("Order.pizza - drink no")
    elif currentIntent == "Order.pizza - drink yes":
        # drinkString = menuHandler.getDrinksString()
        # return sendWebhookCallback(drinkString)
        return sendWebhookCallback("Order.pizza - drink yes")
    elif currentIntent == "Order.pizza":
        # return __handleOrderPizzaIntent(queryText, requestContent)
        return sendWebhookCallback("Order.pizza")
    elif currentIntent == "Welcome":
        pizzaMenu = menuHandler.get_menu_pizza_string()
        welcomeString = f"Olá! Bem-vindo à Pizza do Bill! Funcionamos das 17h às 22h.\n {pizzaMenu}." \
                        f" \nQual pizza você vai querer?"
        startContext = structureNewDialogflowContext(contextName="Start", lifespan=1)
        return sendWebhookCallback(botMessage=welcomeString, nextContext=startContext)
    return sendWebhookCallback(botMessage="a")

