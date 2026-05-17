def mostrar_menu(opcoes): #Recebe um número correspondente a uma das escolhas (número dentro da var opcoes)
    print("O que você vai fazer hoje?") #Exibe o texto pro usuário
    print(opcoes)                       #Exibe as opções pro usuário
    escolha = input()                   #Guarda o número escolhido pelo usuário na var escolha
   


def mostrar_status(estado):
    print("Texto genérico sobre o dia ter acabado") #Exibe o texto pro usuário
    print(
        f"Saúde: {estado['saude']}\n"
        f"Energia: {estado['energia']}\n"
        f"Comida: {estado['comida']}\n"
        f"Água: {estado['agua']}\n"
        f"Sanidade: {estado['sanidade']}"  #Exibe cada um dos status atualizados
    )
