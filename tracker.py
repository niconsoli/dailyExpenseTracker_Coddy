# print("Welcome to the Daily Expense Tracker!")

# def menu():
#     print("""
# Menu:
# 1. Add a new expense
# 2. View all expenses
# 3. Calculate total and average expense
# 4. Clear all expenses
# 5. Exit""")

print("Este projeto foi feito com base no projeto de mesmo nome, mencionado na Seção 1, Capítulo 14 das lições de Python, no site Coddy.")
print("Estarei traduzindo livremente a fim de reforçar o aprendizado exercitado na realização deste projeto!")

def menu():
    print("""
Bem-vindo ao Rastreador de Despesas Diárias!
Menu de opções:
1. Adicione uma nova despesa
2. Verifique todas as despesas
3. Calcule o total e a média das despesas
4. Apagar o histórico de despesas
5. Sair""")

menuBool = True
despesas = []

while menuBool:
    menu()
    opc = input("Selecione a opção desejada: ")

    match opc:
        case "1":
            n = int(input("Quantas despesas serão adicionadas? "))
            for i in range(n):
                despesas.append(float(input(f"Informe o valor da despesa número {i + 1}: ")))

        case "2":
            if len(despesas) == 0:
                print("Não há despesas registradas no momento.")
            else:
                print("As despesas registradas até o momento são:")
                for i, despesa in enumerate(despesas):
                    print(f"{i + 1}. {despesa}")

        case "3":
            if len(despesas) == 0:
                print("Não há despesas registradas no momento.")
            else:
                soma = 0
                for i, despesa, in enumerate(despesas):
                    soma += despesa
                media = soma / len(despesas)
                print(f"Soma total das despesas: {soma}")
                print(f"Media total das despesas: {media}")

        case "4":
            despesas = []
            print("Despesas apagadas com sucesso.")

        case "5":
            print("Muito obrigado por acessar o Rastreador de Despesas Diárias")
            print("Encerrando o sistema...")
            menuBool = False

        case _:
            print("Opção inválida. Por favor, selecione uma opção válida do menu.")