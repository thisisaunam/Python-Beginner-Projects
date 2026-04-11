# taking user input

# input 1: name of the item
item = input("what item would you like to buy?: ")

# input 2: price of the item
price = float(input("what is the price?: "))

# input 3: quantity of the item you're purchasing
quantity = int(input("how many would you like?: "))

# calculate total cost
total = price * quantity

# billing
print(f"\nyou've bought {quantity} x {item}")
# showing total amount with decimals upto 2 places
print(f"your total is: ${total:.2f}")
