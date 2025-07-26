import pyfiglet
import json
from datetime import datetime
import os

DATA_FILE = "expenses.json"


def main():

    expenses = load_expenses()

    print("🚀RUNNING EXPENSE TRACKER")
    username = input("What is your name: ")
    print(welcome_user(username))

    while True:
        print("~Expense Tracker~")
        print("1- Add Expense")
        print("2- Check Expense")
        print("3- Veiw expence by category")
        print("4- Clear Expense")
        print("5- Clear all expense")
        print("6- Save & Exit")
        # take input what user want to do
        choice = input("Choose an option (1-6): ").strip()
        # 1 = add expense to add_expense
        if choice == "1":
            amount = get_float_input("Amount: $")
            category = input("Category: ").strip().capitalize()
            date = get_valid_date("Date (YYYY-MM-DD): ")
            add_expense(expenses, amount, category, date)
            print("✅ Expense added.")

        # 2 = view expense from view_expense
        elif choice == "2":
            view_expenses(expenses)

        # 3 = get summary of expense by category
        elif choice == "3":
            summary = get_summary(expenses)
            print("\n---summary by category---")
            for category, total in summary.items():
                print(f"{category}: $ {total:.2f}")

        # 4 = delete expense
        elif choice == "4":
            view_expenses(expenses)
            delete_expense(expenses)

        # 5 = delete all expenses
        elif choice == "5":
            confirm = input("are you sure you want to delete all expenses? (y/n): ")
            if confirm.lower() == "y":
                expenses.clear()
                print("🗑️All expenses cleared.")

        # save files
        elif choice == "6":
            save_expenses(expenses)
            print("💾Data saved. GoodBye!")

        else:
            print(" Invalid option. please choose ")


# Now add expense,category,date,amount
def add_expense(expenses: list, amount: float, category: str, date: str) -> None:
    # Add a new expense to the list.
    expenses.append({"amount": amount, "category": category, "date": date})


# In this function take float values
def get_float_input(prompt: str) -> float:
    """Prompt user until they enter a valid float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")


# validating date format in (YYYY-MM-MM)
def get_valid_date(prompt: str) -> str:
    """Prompt user for a valid date (YYYY-MM-DD)."""
    while True:
        date_str = input(prompt).strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ Invalid date format. Try again (YYYY-MM-DD).")


# view expense those u have written in add_expenses
def view_expenses(expenses: list) -> None:
    """Display all expenses"""
    if not expenses:
        print("No expense Record Found")
        return
    print("\n--- All expenses---")
    for i, e in enumerate(expenses):
        print(f"{i+1}. {e['date']}: ${e['amount']:.2f} - {e['category']}")


# here view summaryby category
def get_summary(expenses: list) -> None:
    """return total amount spent as category"""
    summary = {}
    for e in expenses:
        category = e["category"]
        summary[category] = summary.get(category, 0) + e["amount"]
    return summary


# delete expenses
def delete_expense(expense: list) -> None:
    """Delete an expense by index"""
    try:
        index = int(input("Enter the number of expense to delete: ")) - 1
        if 0 <= index < len(expense):
            removed = expense.pop(index)
            print(
                f"✅ Removed: {removed['date']} - ${removed['amount']}- {removed['category']}"
            )
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")


def save_expenses(expenses: list) -> None:
    """Save expenses to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file)


# json will handle file here
def load_expenses() -> list:
    """Load expenses from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


def welcome_user(username):

    banner = pyfiglet.figlet_format(f"Welcome {username}!")
    return banner


if __name__ == "__main__":
    main()
