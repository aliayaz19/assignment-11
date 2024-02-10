#Develop a Python script that takes a user's input of a month (as a number) and prints out the 
#number of days in that month.
month = input("Enter Month Number: ")

if month == '1':
    print("31 Days Are In January.")
elif month == '2':
    print("28 or 29 Days Are In February.")
elif month == '3':
    print("31 Days Are In March.")
elif month == '4':
    print("30 Days Are In April.")
elif month == '5':
    print("31 Days Are In May.")
elif month == '6':
    print("30 Days Are In June.")
elif month == '7':
    print("31 Days Are In July.")
elif month == '8':
    print("31 Days Are In August.")
elif month == '9':
    print("30 Days Are In September.")
elif month == '10':
    print("31 Days Are In October.")
elif month == '11':
    print("30 Days Are In November.")
elif month == '12':
    print("31 Days Are In December.")
else:
    print("Invalid month number.")
