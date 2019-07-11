Stocks = {
    'Brands': ["HP", "Dell", "Apple Macbook", "Asus"],
    'Quantity': [20, 50, 12, 30],
}
# for i in range(4):
#     print(Stocks["Brands"][i],":",Stocks["Quantity"][i])
# print("Apple Macbook: ", Stocks["Quantity"][Stocks["Brands"].index("Apple Macbook")])
item = input('Search for: ')
print(item,":",Stocks["Quantity"][Stocks["Brands"].index(item)])