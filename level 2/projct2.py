budget = 0
expense = []
def add_income():
    global budget 
    income = float(input("Enter your income amount:"))
    income += budget
    print("income added your total balance is" +budget)


def add_expense():
    global budget 
    expense = float(input("Enter expense amount: "))
    description = input("Enter expense description: ")
    if expense > budget:
        print("Not enough balance!")
    else:
        budget == expense
        expense.append((description, expense))
        print("Expense added! Remaining balance is:", budget)    

def show_summary():
    print("\n--- Budget Summary ---")
    print("Balance:", budget)
    print("Expenses:")
    for desc, amt in expense:
        print(f"- {desc}: {amt}")

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. Show Summary")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
