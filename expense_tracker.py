# Expense tracker project
#expense = khaarcha
expenses = [] # list of expenses in form of dictionaries
print("Welcome to the Expense Tracker!")

while True:
    print("=======MENU=======")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total expenses")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    #ADD AN EXPENSE
    if(choice=='1'):
        date = input("Enter the date of the expense : ")
        category = input("Enter the category of the expense(food , travel , makeup ,car,etc): ")
        discription = input("Enter the discription (details) of the expense : ")
        amount = float(input("Enter the amount of the expense : "))
        expense = {
            "date": date,
            "category": category,
            "discription": discription,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    #VIEW ALL EXPENSES
    elif(choice=='2'):
        if len(expenses) == 0:
            print("No expenses to show.")
        else:
            print("=======ALL EXPENSES=======")
        count = 1
        for expense in expenses:
            print(f"expense number {count} -> {expense['date']} , {expense['category']}, {expense['discription']} , {expense['amount']}") 
            count += 1

    #VIEW TOTAL EXPENSES
    elif(choice=='3'):
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
        print(f"Total expenses: {total}")

    #EXIT
    elif(choice=='4'):
        print("Exiting the Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. TRY AGAIN!")