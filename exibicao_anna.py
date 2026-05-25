def mostrar_menu(indice_dias): #Recebe um número correspondente a
    if indice_dias < 7:
        print("O que você vai fazer hoje? Digite 1 pra buscar água, 2 pra buscar comida e 3 pra descansar: ")                    
        escolha = input() 
        return escolha                
   


def mostrar_status(estado):
    print(f"Resultados de hoje: \n"
        f"Saúde: {estado['saude']}\n"
        f"Energia: {estado['energia']}\n"
        f"Comida: {estado['comida']}\n"
        f"Água: {estado['agua']}\n"
        f"Sanidade: {estado['sanidade']}"  #Exibe cada um dos status atualizados
    )

def mostrar_texto(indice_dias):
    lore = "Você ficou preso em uma exploração em uma floresta isolada após perder contato com sua equipe. " \
    "Você tem apenas um rádio quebrado e alguns mantimentos em sua mochila, e pela área ser muito isolada da civilização," \
    " a equipe de resgate irá demorar para chegar. Tome decisões, planeje e administre seus recursos, " \
    "e tente sair da floresta vivo."

    tutorial = tutorial = """
Você vai começar com:
----------------------------------
Energia: 80
Comida: 20
Água: 20
Sanidade: 60
Saúde: 100

A cada dia, existem 3 opções para passar o seu tempo na floresta:
buscar comida, buscar água e descansar.

Mas cuidado! se você zerar energia, você desmaia e perde água e comida.
Zerar água ou comida leva à morte.
Zerar saúde, obviamente, leva à morte e sanidade... bem, quem sabe?
"""

    fim_do_dia = "Está escurecendo e parece que isso é tudo que você vai fazer."


    if indice_dias == 0:
        print(lore)
        print(tutorial)

    else:
        print(fim_do_dia)

