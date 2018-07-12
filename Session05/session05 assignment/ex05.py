
prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}

stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15
}

total = 0
print("List of inventory:")
print()

for key in prices.keys():
    print("* {0}".format(key))
    print("* price: {0}".format(prices[key]))
    print("* stock: {0}".format(stock[key]))
    print()

for key in prices.keys():
    sales = prices[key] * stock[key]
    print("Sales of {0} is {1}".format(key, sales))

    total += sales

print()
print("Total sales is: {0}".format(total))
