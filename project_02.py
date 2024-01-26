import json
from datetime import datetime

EXPENSE_FILE = "expense_data.json"

def get_user_input():
    try:
        amount = float(input("Enter expense amount: "))
        description = input("Enter a brief description: ")
        category = input("Enter expense category (food, transportation, entertainment, etc.): ").lower()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {"amount": amount, "description": description, "category": category, "date": date}
    except ValueError:
        print("Invalid input. Please enter a valid number for the expense amount.")
        return None

def save_expense_data(data):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(data, file)

def load_expense_data():
    try:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def display_summary(data):
    print("\nExpense Summary:")
    for category, expenses in data.items():
        total_amount = sum(expense['amount'] for expense in expenses)
        print(f"{category.capitalize()}: ${total_amount:.2f}")

def display_monthly_summary(data):
    current_month = datetime.now().strftime("%Y-%m")
    monthly_expenses = {category: [] for category in set(expense['category'] for expenses in data.values() for expense in expenses)}

    for category, expenses in data.items():
        for expense in expenses:
            if expense['date'].startswith(current_month):
                monthly_expenses[category].append(expense)

    print(f"\nMonthly Expense Summary ({current_month}):")
    for category, expenses in monthly_expenses.items():
        total_amount = sum(expense['amount'] for expense in expenses)
        print(f"{category.capitalize()}: ${total_amount:.2f}")

def main():
    expense_data = load_expense_data()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expense Summary")
        print("3. View Monthly Summary")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            expense = get_user_input()
            if expense:
                category = expense["category"]
                if category not in expense_data:
                    expense_data[category] = []
                expense_data[category].append(expense)
                save_expense_data(expense_data)
                print("Expense added successfully.")
        elif choice == "2":
            display_summary(expense_data)
        elif choice == "3":
            display_monthly_summary(expense_data)
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
