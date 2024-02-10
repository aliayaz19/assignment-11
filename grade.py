#Create a program that asks the user to enter their exam score and prints out their grade based 
#on the following criteria: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
while True:

    score=int(input("Entter your score: "))
    if score >=90 <= 100:
        print("A grade.")
    elif  score >=80 <= 89:
        print("B grade.")
    elif score >=70 <= 79:
        print("C grade.")
    elif score >=60 <= 69:
        print("D grade.")
    elif score < 60:
        print("F grade.")
    else:
        print("Invalid number")