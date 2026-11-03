# Esta versão é a original que enviei no Coddy, sem alterações, em prol de solucionar o capítulo de criação de projeto
# Cheque tracker.py para a versão alterada e traduzida que fiz depois de concluir o projeto no Coddy!

print("Welcome to the Daily Expense Tracker!")

def menu():
    print("""
Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit""")

menu()
menuChoice = True
despesas = []
while menuChoice:
    opc = input()
    match opc:
        case "1":
            despesas.append(float(input()))
            print("Expense added successfully!")
        case "2":
            if len(despesas) == 0:
                print("No expenses recorded yet.")
            else:
                print("Your expenses:")
                for i, expense in enumerate(despesas):
                    print(f"{i + 1}. {expense}")
        case "3":
            if len(despesas) == 0:
                print("No expenses recorded yet.")
            else:
                soma = 0
                for i, despesa in enumerate(despesas):
                    soma += despesa
                media = soma / len(despesas)
                print(f"Total expense: {soma}")
                print(f"Average expense: {media}")
        case "4":
            despesas = []
            print("All expenses cleared.")
        case "5":
            print("Exiting the Daily Expense Tracker. Goodbye!")
            menuChoice = False
        case _:
            print("Invalid choice. Please try again.")