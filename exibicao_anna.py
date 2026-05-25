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


    fim_do_dia = "Está escurecendo e parece que isso é tudo que você vai fazer por hoje."


    if indice_dias == 0:
        print(lore)
        print(tutorial)

    else:
        print(fim_do_dia)


def verificar_final(estado,sanidade_zerou):

    textos = {

        "morte por saúde":
        "Você se sente muito mal durante a noite; sua barriga dói muito e você está suando frio.\n"
        "De repente, tudo fica escuro e você perde os sentidos. Dessa vez, você não acorda.\n"
        "GAME OVER - Final: Doença letal",

        "morte por desidratação":
        "Você sente sua boca ressecar ao extremo, seus órgãos estão clamando por água, mas você não tem nenhuma.\n"
        "Uma dor crescente se irradia por toda a sua cabeça, e você desmaia. Dessa vez, você não acorda.\n"
        "GAME OVER - Final: desidratação",

        "morte por fome":
        "Você sente uma dor lancinante percorrendo seu estômago, quase como se ele tentasse se autodigerir.\n"
        "A dor deixa seus pensamentos confusos e você aos poucos perde a noção do tempo e dos seus arredores.\n"
        "Seus sentidos se esvaem e dessa vez, você não acorda.\n"
        "GAME OVER - Final: inanição",

        "final bom":
        "Depois de colocar em prática todos os seus instintos de sobrevivência por 7 dias, a ajuda finalmente chega.\n"
        "Você sobreviveu!\n"
        "FINAL BOM - A esperança é a última que morre",

        "final ruim":
        "Seus dias nessa floresta cheia de horrores e perigos fazem com que você enlouqueça completamente.\n"
        "A realidade se disfaz diante dos seus olhos.\n"
        "Algumas pessoas te tiram daqui e resgatam o que sobrou de você.\n"
        "FINAL RUIM - Eles não vão acreditar em você"
    }

    if estado["comida"] == 0:
        print(textos["morte por fome"])

    if estado["agua"] == 0:
        print(textos["morte por desidratação"])

    if estado["saude"] == 0:
        print(textos["morte por saúde"])

    if sanidade_zerou == True and indice_dias >= 7:
        print(textos["final ruim"])
    else:
        print(textos["final bom"])



    
    

