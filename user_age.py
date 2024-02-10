#Create a program that asks the user to enter their age and prints out whether they are a child, 
#teenager, adult, or senior citizen.

while True:

    x = int(input("Enter your age: "))
    if 10 <= x < 15:
        print("You are a child.")
    elif 15 <= x <= 20:
        print("You are a teenager.")
        break
    elif x > 20:
        print("You are a senior citizen.")
