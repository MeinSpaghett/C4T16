Stocks = {
    "Brands": ["HP", "Dell", "Macbook", "Asus", "Acer", "Toshiba", "Fujitsu", "Alienware"],
    "Price": [600, 650, 12000, 400, 350, 600, 900, 1000]
}

# print("Total: ", Stocks["Price"][Stocks["Brands"].index("Asus")]*5)

item_buy = input("Buy: ")
item_quantity = int(input("Quantity: "))
print ("Total: ", Stocks["Price"][Stocks["Brands"].index(item_buy)]*item_quantity)