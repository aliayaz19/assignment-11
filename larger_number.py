#Develop a program that prompts the user to enter two numbers and prints out the larger of the 
#two.
while True:

    x=int(input("Enter a number 1: "))
    y=int(input("Enter a number 2: "))
    if x>y:
        print("number 1 is larger")
    elif y>x:
        print("number 2 is larger")
    elif x==y:
        print("This is equal number. X ")
    elif y==x:
        print("This is equal number. Y ")
    else:
        print("Invaild Number")
