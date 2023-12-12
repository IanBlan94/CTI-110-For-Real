"""

CTI-110
P2LAB1 - Gas Prices
Blanchard
9-7-23

"""

# ask for miles per gallon
mpg = float(input("How many miles per gallon does your car get? "))

#Ask for price per gallom
price_per_gallon = float(input("What is the price per gallon? "))

# show price per mile to drive
price_per_mile = price_per_gallon / mpg

# Display how much it costs to drive one mile

#print("This car costs", price_per_mile, "to drive 1 mile")

print(f"This car costs ${price_per_mile:.2f} to drive 1 mile")

# this will display how much it costs to drive 20 miles
print(f"To drive 20 miles it would cost {price_per_mile * 20:.2f}")

# this will display how much it costs to drive 100 miles
print(f"To drive 100 miles it would cost {price_per_mile * 100:.2f}")

# this will display how much it costs to drive 500 miles
print(f"To drive 500 miles it would cost {price_per_mile * 500:.2f}")