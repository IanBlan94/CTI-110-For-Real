"""
CTI-110

P1Lab2 - Sales

8/31
Simple Point Of Sales

"""
store_name = "Floyds Shoes"
product = "shoes"
Stock = 500
price = 10.00

# Greet Customer
print("Hey there, welcome to", store_name)
print("Whats your name?")

customer_name = input()

print("Very nice to meet you,", customer_name)

#Explain Product
print()
print("Today were running a special on our", product)
print("Our price on", product, "today is", price)
print("With over", Stock, product, "left, we've got all your needs!")

# Take Order
print()

print("How many", product, "would you like to buy?")

#input gives us a string
order = input()
# convert it to a number

order = int(order)
if (order > Stock):
  order = Stock
  print("Sorry, we can only sell you", order)

print("how many", product, "would you like to buy?")
order = int(input())
# order = int(input())

total = order * price


print("Perfect, with", order, "orders that will be", total)

