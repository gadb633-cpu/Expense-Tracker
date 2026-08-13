from time import *
list_of_expenses = [{"date": strftime("%Y-%m-%d"),"titel": "Notebook","category":"school","amount":24.90},{"date": strftime("%Y-%m-%d"),"titel": "coffee","category":"food","amount":12.00}]
def show_expenses(list_of_expenses):
    for i in list_of_expenses:
        print(f"{i["date"],"|",i["titel"],"|",i["category"],"|",i["amount"]}")
show_expenses(list_of_expenses)

def calculate_total(list_of_expenses):
    total = 0
    for i in list_of_expenses:
        total += i["amount"]
    return total
print(f"{calculate_total(list_of_expenses)} ILS")

def add_expense(list_of_expenses,titel,category,amount):
    list_of_expenses.append({"date":strftime("%Y-%m-%d"),"titel": titel,"category":category,"amount":amount })
    