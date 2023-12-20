class GroceryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def get_name(self):
        return self.name
    
    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price

    def updateQuantity(self, quantityChange):
        self.quantity += quantityChange
        print(f'Current stock of {self.name} : {self.quantity} item/items.')

    
class StockManager:
    def __init__(self):
        self.items = {}

    def addItem(self, item):
        self.items[item.name] = item

    def checkStock(self, name):
        return self.items.get(name).quantity if name in self.items else 0

    def updateStock(self, name, quantity):
        self.items[name].updateQuantity(quantity)

class Cashier:
    def __init__(self):
        self.totalPrice = 0.0

    def scanItem(self, item, quantity):
        self.totalPrice += item.price * quantity
        print(f'Current amount : {self.totalPrice} bath.')

    def getTotalPrice(self):
        return self.totalPrice