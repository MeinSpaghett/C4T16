Stocks = {
    'Brands': ["HP", "Dell", "Apple Macbook", "Asus", "Acer"],
    'Quantity': [20, 50, 12, 30, 15],
}
Stocks["Brands"].append("Toshiba")
Stocks["Quantity"].append(10)
Stocks["Quantity"][Stocks["Brands"].index("Dell")] += 10
Stocks["Quantity"][Stocks["Brands"].index("Apple Macbook")] -=2
Stocks["Brands"].append("Fujitsu")
Stocks["Quantity"].append(15)
Stocks["Brands"].append("Alienware")
Stocks["Quantity"].append(5)
Stocks["Price"] = [600, 650, 12000, 400, 350, 600, 900, 1000]
Total = []
for i in range(8):
    Total.append(Stocks["Quantity"][i]*Stocks["Price"][i])
print (sum(Total))

   

