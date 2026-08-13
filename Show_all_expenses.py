from time import *
from rich.console import Console
from rich.table import Table
list_of_expenses = [{"date": strftime("%Y-%m-%d"),"titel": "Notebook","category":"school","amount":24.90},{"date": strftime("%Y-%m-%d"),"titel": "coffee","category":"food","amount":12.00}]
def show_expenses(list_of_expenses):
    table = Table(title="list of expenses")
    table.add_column("date", justify="right", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("category", justify="right", style="green")
    table.add_column("amount", justify="right", style="black")
    for i in list_of_expenses:
        table.add_row(i["date"],i["titel"],i["category"],str(i["amount"]))
    console = Console()
    console.print(table)
show_expenses(list_of_expenses)
def calculate_total(list_of_expenses):
    total = 0
    for i in list_of_expenses:
        total += i["amount"]
    return total
console = Console()
console.print(f"Total: [bold green]${calculate_total(list_of_expenses):.2f}[/bold green]")

def add_expense(list_of_expenses,titel,category,amount):
    list_of_expenses.append({"date":strftime("%Y-%m-%d"),"titel": titel,"category":category,"amount":amount })
    return list_of_expenses
def ask_for_expense(list_of_expenses):
    titel = input("enter titel")
    category = input("enter category")
    amount = input("enter amount")
    add_expense(list_of_expenses,titel,category,amount)

