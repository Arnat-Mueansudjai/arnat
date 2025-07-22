# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True :
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")


        if choice== "1":
            print("Your balance is : ",balance)
        elif choice== "2":
            w=float(input("How much do you want to withdraw?: "))
            if balance>w:
                balance=balance-w
                print(f"Your balance is :{balance:.2f} \nThank you for using.")
            else :
                print("Insufficient balance!!!")
                print("Your balance is : ",balance)
        elif choice== "3" :
            d=float(input("How much do you want to deposit?: "))
            balance=balance+d
            print(f"Your balance is : {balance:.2f}")
        elif  choice== "4" :
            print("Thank you for using.")
            break
        else :
            print("This not choice please chose 1-4!!! ")

        
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")
