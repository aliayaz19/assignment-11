#Create a program that simulates a simple ATM machine. It should ask the user for their PIN, 
#verify it, and then allow them to withdraw money if the balance is sufficient.
print("   WELCOME TO MEEZAN BANK ATM   ")
pin = int(input("Enter your pin: "))
name = input("Enter your name: ")


correct_pin = 2222
account_balance = 100000

if pin == correct_pin:
    print(f"Welcome To Meezan Bank ATM, Sir {name}")
    
    fast_cash = [500, 1000, 2000, 5000, 10000, 20000, 25000]

    user_input = input("Enter 'fast cash', 'I want other amount', or 'current balance': ")

    if user_input == 'fast cash':
        print("Fast Cash List:", fast_cash)
        selected_amount = int(input("Select one amount for withdrawal: "))
        if selected_amount in fast_cash:
            if selected_amount <= account_balance:
                account_balance -= selected_amount
                print("Amount withdrawn successfully.")
                print("Remaining account balance:", account_balance)
                print("Collect Your Cash.")
                print("Pick Up Your Card And Thanks For Using ATM!")
            else:
                print("Insufficient funds. Cannot withdraw this amount.")
        else:
            print("Invalid amount selection.")
    elif user_input == 'I want other amount':
        new_amount = int(input("Enter the desired amount in rupees: "))
        if new_amount <= account_balance:
            account_balance -= new_amount
            print("Amount withdrawn successfully.")
            print("Remaining account balance:", account_balance)
            print("Collect Your Cash.")
            print("Pick Up Your Card And Thanks For Using ATM!")
        else:
            print("Insufficient funds. Cannot withdraw this amount.")
    elif user_input == 'Current Balance':
        print("Your Current Balance is:", account_balance, "PKR")
    else:
        print("Invalid input.")
else:
    print("Incorrect PIN. Please try again later.")
