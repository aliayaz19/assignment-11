#Design a Python program that calculates the total cost of items purchased by a customer based 
#on the provided unit price and quantity, applying a discount of 10% if the total cost exceeds 
#$1000
price = int(input("Enter price: "))
quantity = int(input("Enter quantity: "))
cost = price * quantity

if cost > 1000:
    cost_with_discount = cost * 0.9
    print("Cost after 10% discount:", cost_with_discount)
else:
    print("Cost without discount:", cost)
