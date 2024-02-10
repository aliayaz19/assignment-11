#Write a Python script to determine whether a given year is a leap year or not
while True:
    year=int(input("Enter a year: "))
    if year %4==0:
        if 100!=0:
            print("This is leap year.")
    elif 400==0:
        print("This is leap year.")        
    else:
        print("This is not a lap year.")