#Develop a program that prompts the user to enter their current temperature in Celsius and 
#prints out whether they should wear a jacket (if temperature is below 20°C) or not.
temp=int(input("Enter your tempreture : "))
if temp<=20:
    print("You should wear a jacket.")
elif temp > 20 :
    print("Tempreture is normal.")