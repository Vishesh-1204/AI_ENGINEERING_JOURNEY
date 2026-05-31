from BASIC import (
    add_expense,
    view_expenses,
    close_connection
)

while True:

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Expense Name: ")
        category = input("Category: ")
        amount = float(input("Amount: "))

        add_expense(
            name,
            category,
            amount
        )

        print("Expense Added!")

    elif choice == "2":

        view_expenses()

    elif choice == "3":

        close_connection()
        break

    else:
        print("Invalid Choice")