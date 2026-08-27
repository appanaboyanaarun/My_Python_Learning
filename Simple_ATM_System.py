Balance = 10000

Admin = input("Admin: ")
Password = input("Enter your password: ")

if Admin == "Admin":

    if Password == "1234":

        while True:

            print("***************")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Balance")
            print("4. Exit")
            print("***************")

            choose = int(input("Please enter: "))

            if choose == 1:

                amount = int(input("Enter Withdraw amount: "))

                if amount > 0 and amount <= Balance:
                    Balance = Balance - amount
                    print("Withdraw successful")
                else:
                    print("Insufficient Balance or Invalid Amount")

            elif choose == 2:

                amount = int(input("Enter Deposit amount: "))

                if amount > 0:
                    Balance = Balance + amount
                    print("Deposit Completed")
                else:
                    print("Invalid amount")

            elif choose == 3:

                print("Current Balance:", Balance)

            elif choose == 4:

                print("Thank you!")
                break

            else:
                print("Invalid choice")

    else:
        print("Incorrect Password")

else:
    print("Invalid Admin")