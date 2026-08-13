from Show_all_expenses import * 
def main():
    status = True
    while status == True:
        enswer = input("you want to add an expense ?")
        if enswer == "yes":
            ask_for_expense(list_of_expenses)
            show_expenses(list_of_expenses)
            calculate_total(list_of_expenses)
        elif enswer == "no":
            status = False
        show_expenses(list_of_expenses)
        calculate_total(list_of_expenses)         
main()
