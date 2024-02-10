#Implement a program that takes a user's input of a year and month and prints out the number 
#of days in that month, considering leap years.
month = input("Enter Month Name: ")
year = int(input("Enter Year: "))

leap_year = False

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("This is a leap year.")
        leap_year = True

if not leap_year:
    print("This is not a leap year.")

if month == "January":
    print("31 Days")
elif month == "February":
    if leap_year:
        print("29 Days")
    else:
        print("28 Days")
elif month == "March":
    print("31 Days")
elif month == "April":
    print("30 Days")
elif month == "May":
    print("31 Days")
elif month == "June":
    print("30 Days")
elif month == "July":
    print("31 Days")
elif month == "August":
    print("31 Days")
elif month == "September":
    print("30 Days")
elif month == "October":
    print("31 Days")
elif month == "November":
    print("30 Days")
elif month == "December":
    print("31 Days")
else:
    print("Invalid month")

  