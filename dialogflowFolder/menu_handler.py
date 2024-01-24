from references.loader import loadSpeisekarte
from utils.patterns import singleton


@singleton
class MenuItemHandler:
    def __init__(self):
        self.speisekarte = loadSpeisekarte()
        self.params = {"pizzas": [], "drinks": []}

    # def analyzeTotalPriceWithMenuPrices(self, structuredOrder: dict):
    #     totalPrice, orderItems = getTotalPrice(structuredOrder=structuredOrder, menu=self.speisekarte)
    #     final_message = generateOrderFinalMessage(totalPrice=totalPrice, orderItems=orderItems)
    #     return {"totalPrice": totalPrice, "orderItems": orderItems, "finalMessage": final_message}