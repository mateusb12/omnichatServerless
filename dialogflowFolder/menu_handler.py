from references.loader import loadSpeisekarte
from utils.patterns import singleton


def createMenuString(menu: dict, category: str = None) -> str:
    if category is None:
        raise ValueError("Category cannot be None")
    menuString = f"Cardápio de {category}:\n"

    for item in menu:
        name = item['nome']
        price = item['preço']

        itemString = f"- {name} - R${price:.2f}\n"
        menuString += itemString

    return menuString


@singleton
class MenuItemHandler:
    def __init__(self):
        self.speisekarte = loadSpeisekarte()
        self.params = {"pizzas": [], "drinks": []}

    def get_menu_pizza_string(self):
        return createMenuString(menu=self.speisekarte["Pizzas"], category="pizzas")

    # def analyzeTotalPriceWithMenuPrices(self, structuredOrder: dict):
    #     totalPrice, orderItems = getTotalPrice(structuredOrder=structuredOrder, menu=self.speisekarte)
    #     final_message = generateOrderFinalMessage(totalPrice=totalPrice, orderItems=orderItems)
    #     return {"totalPrice": totalPrice, "orderItems": orderItems, "finalMessage": final_message}
