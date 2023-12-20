from Class import GroceryItem, Cashier, StockManager

def main():
    stock_manager = StockManager()
    cashier = Cashier()

    while True:
        print("[1] Create new item.")
        print("[2] Check the stock of item.")
        print("[3] Check the balance.")
        print("[4] Pay the items.")
        print("[0] Exit.")

        choice = input("Enter your choice : ")

        if choice == '1':
            name = input("Item name : ")
            quantity = int(input("Item quantity : "))
            price = float(input("Item price : "))
            item = GroceryItem(name, quantity, price)
            stock_manager.addItem(item)
            print(f'{name} added to the stock.')

        elif choice == '2':
            name = input("Item name : ")
            quantity = stock_manager.checkStock(name)
            print(f'Quantity of {name} : {quantity} item/items.')
            
        elif choice == '3':
            amount = cashier.getTotalPrice()
            print(f'Current amount : {amount} bath.')

        elif choice == '4':
            item = input("Enter the item name : ")
            quantity = int(input("Enter the quantity sold : "))
            stock_manager.updateStock(item, -quantity)
            dataItem = stock_manager.items[item]
            cashier.scanItem(dataItem, quantity)
            print(f'{quantity} quantity of {item} has been sold.')
            print(f'Current item quantity : {dataItem} item/items.')
        elif choice == '0':
            break
        else:
            print('Wrong command. Please try again')


if __name__ == "__main__":
    main()