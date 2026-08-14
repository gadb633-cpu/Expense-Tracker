from time import *
from rich.console import Console
from rich.table import Table
from questionary import *


list_of_expenses = []
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


def add_expense(list_of_expenses,titel,category,amount):
    list_of_expenses.append({"date":strftime("%Y-%m-%d"),"titel": titel,"category":category,"amount":amount })
    return list_of_expenses
def ask_for_expense(list_of_expenses):
    titel = text("enter titel").ask()
    category = select("what category your expense",choices = ["food","travel","school","entertainment","other"]).ask()
    amount = float(text("enter amount").ask())
    add_expense(list_of_expenses,titel,category,amount)
def manager():
    status = True
    while status == True:
        enswer = select("you want to add an expense? ",choices = ["yes","no"]).ask()
        if enswer == "yes":
            ask_for_expense(list_of_expenses)
            show_expenses(list_of_expenses)
            console = Console()
            console.print(f"Total: [bold green]${calculate_total(list_of_expenses):.2f}[/bold green]")
        elif enswer == "no":
            status = False
            show_expenses(list_of_expenses)
            console = Console()
            console.print(f"Total: [bold green]${calculate_total(list_of_expenses):.2f}[/bold green]")