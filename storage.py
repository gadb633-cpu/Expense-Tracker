from Show_all_expenses import *
from typer import *
app = Typer()

@app.command()
def add(title, category, amount):
    amount = float(amount)
    add_expense(list_of_expenses, title, category, amount)
    show_expenses(list_of_expenses)
    console = Console()
    console.print(f"Total: [bold green]${calculate_total(list_of_expenses):.2f}[/bold green]")
@app.command("list")
def show_list():
    show_expenses(list_of_expenses)
    console = Console()
    console.print(f"Total: [bold green]${calculate_total(list_of_expenses):.2f}[/bold green]")
