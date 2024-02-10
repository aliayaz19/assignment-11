#Write a Python program to check if a given number is positive, negative, or zero.
while True:

    x=int(input("Enter a number: "))
    if x>0:
        print("Number is Possitive.")
    elif x<0:
        print("Number is Negetive.")
    elif x==0:
        print("NUmber is 0.")
    else:
        print("Invalid Number.")