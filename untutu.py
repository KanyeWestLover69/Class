expenses = []

def add_expense(description, amount):
    expenses.append({"description": description, "amount": amount})

def display_expenses():
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['description']}: ${expense['amount']}")

def get_total_expenses():
    return sum(expense['amount'] for expense in expenses)

def display_total_expenses():
    print(f"Total expenses: ${get_total_expenses()}")

while True:
    try:
        print("\nOptions: 1. Add expense, 2. Display expenses, 3. Display total expenses, 4. Quit")
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(description, amount)
        elif user_input == 2:
            display_expenses()
        elif user_input == 3:
            display_total_expenses()
        elif user_input == 4:
            print("bye")
            break
        else:
            print("invalid, choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")