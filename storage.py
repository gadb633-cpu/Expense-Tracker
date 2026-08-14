from Show_all_expenses import *
from typer import *
app = Typer()

@app.command()
def add(title, category, amount):
    add_expense(list_of_expenses, title, category, amount)
    show_expenses(list_of_expenses)

@app.command("list")
def show_list():
    show_expenses(list_of_expenses)

