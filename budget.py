import json

try:
    with open("expenses.json", "r") as file:
            expenses = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):

    expenses = []

print("<<<MY MONTHLY BUDGET>>>\n")


while True:

        print("1. Add expense")
        print("2. View all expenses")
        print("3. Total expense")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            expenses.append({
                "amount": amount,
                "category": category,
                "description": description
                })
            print("expenses added")

        elif choice == 2:
            if not expenses:
                print("No expenses yet.")
            else:
                for expense in expenses:
                    print(expense)
        elif choice == 3:
            Total = 0
            for item in expenses:
                Total += item['amount']
            print(f"Total amount: {Total}")

        elif choice == 4:
            with open("expenses.json", "w") as file:
                json.dump(expenses, file)
            print("Exiting tracker...")

            break

        else:
            print("Invalid Input, Please try again")