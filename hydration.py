#Hydration Helper: Design a program that prompts the user for their weight and desired level of 
#hydration (e.g., light, moderate, intense exercise). Use nested if-else statements to suggest the 
#amount of water they should drink throughout the day.
while True:
    weight = float(input("Enter Your Weight: "))
    exercise_level = input("Enter 'Light', 'Moderate', or 'Intense': ")

    if weight < 50:
        if exercise_level == 'Light':
            print("Drink at least 8 glasses of water.")
        elif exercise_level == 'Moderate':
            print("Drink at least 9 glasses of water.")
        elif exercise_level == 'Intense':
            print("Drink at least 10 glasses of water.")
        else:
            print("Enter Valid Exercise Level.")
    elif 50 < weight <= 70:
        if exercise_level == 'Light':
            print("Drink at least 9 glasses of water.")
        elif exercise_level == 'Moderate':
            print("Drink at least 10 glasses of water.")
        elif exercise_level == 'Intense':
            print("Drink at least 11 glasses of water.")
        else:
            print("Enter Valid Exercise Level.")
    elif 70 < weight <= 90:
        if exercise_level == 'Light':
            print("Drink at least 10 glasses of water.")
        elif exercise_level == 'Moderate':
            print("Drink at least 11 glasses of water.")
        elif exercise_level == 'Intense':
            print("Drink at least 12 glasses of water.")
        else:
            print("Enter Valid Exercise Level.")
    else:
        print("Enter Valid Weight.")

