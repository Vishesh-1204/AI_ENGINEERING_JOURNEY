from database import (
    add_expense,
    view_expenses,
    delete_expense,
    update_expense,
    close_connection
)

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Update Expense")
    print("5. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        name = input("Expense Name: ")

        category = input("Category: ")

        amount = float(
            input("Amount: ")
        )

        add_expense(
            name,
            category,
            amount
        )

        print("Expense Added Successfully")

    elif choice == "2":

        expenses = view_expenses()

        print("\nExpenses:\n")

        for expense in expenses:

            print(expense)

    elif choice == "3":

        expense_id = int(
            input("Expense ID: ")
        )

        delete_expense(
            expense_id
        )

        print("Expense Deleted")

    elif choice == "4":

        expense_id = int(
            input("Expense ID: ")
        )

        amount = float(
            input("New Amount: ")
        )

        update_expense(
            expense_id,
            amount
        )

        print("Expense Updated")

    elif choice == "5":

        close_connection()

        print("Goodbye!")

        break

    else:

        print(
            "Invalid Choice"
        )