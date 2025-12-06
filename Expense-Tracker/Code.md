```
"""
Expense Tracker - Simple Console App
--------------------------------------
A small Python project to record daily expenses.
Data is saved to a CSV file so that it persists between runs.

Concepts used:
- File handling (read/write)
- Loops and conditionals
- Dictionaries
- Basic input validation
"""

import csv
import os

# The file where expenses will be saved
FILENAME = "expenses.csv"


def initialize_file():
    """Creates the CSV file if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Description", "Amount"])
        print(f"Created new file: {FILENAME}\n")


def add_expense():
    """Adds a new expense entry."""
    category = input("Enter category (e.g., Food, Travel, Bills): ").strip()
    description = input("Enter short description: ").strip()
    try:
        amount = float(input("Enter amount spent (in ₹): "))
    except ValueError:
        print("Invalid amount. Please enter a number.\n")
        return

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, description, amount])

    print("Expense added successfully!\n")


def view_expenses():
    """Displays all recorded expenses."""
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.\n")
        return

    print("\n--- Expense Records ---")
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        total = 0
        count = 0
        for row in reader:
            if len(row) == 3:
                print(f"{row[0]:<10} | {row[1]:<20} | ₹{row[2]}")
                total += float(row[2])
                count += 1
        print(f"\nTotal entries: {count}")
        print(f"Total spent: ₹{total:.2f}\n")


def clear_expenses():
    """Deletes all data from the CSV file."""
    confirm = input("Are you sure you want to delete all expenses? (y/n): ").lower()
    if confirm == "y":
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Description", "Amount"])
        print("All expense records cleared.\n")
    else:
        print("Operation cancelled.\n")


def main():
    """Main program loop."""
    initialize_file()

    while True:
        print("""
===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Clear All Expenses
4. Exit
============================
""")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            clear_expenses()
        elif choice == "4":
            print("Goodbye! Stay mindful of your spending.")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")


if __name__ == "__main__":
    main()
```
