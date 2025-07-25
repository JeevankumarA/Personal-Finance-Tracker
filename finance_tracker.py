import csv

filename = "expenses.csv"

def add_expense(category, amount):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])
    print("Expense added.")

def view_expenses():
    total = 0
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Category: {row[0]}, Amount: {row[1]}")
            total += float(row[1])
    print(f"Total Spent: ₹{total}")

# Uncomment to use interactively:
# while True:
#     choice = input("1. Add Expense\n2. View Expenses\n3. Exit\nEnter: ")
#     if choice == '1':
#         c = input("Category: ")
#         a = input("Amount: ")
#         add_expense(c, a)
#     elif choice == '2':
#         view_expenses()
#     else:
#         break