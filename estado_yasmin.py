#pra verificar as derrotas
def verificar_estado(estado):

    if estado["saude"] <= 0:
        print("\nVocê morreu.")

    elif estado["energia"] <= 0:
        print("\nVocê ficou sem energia.")

    elif estado["sanidade"] <= 0:
        print("\nVocê enlouqueceu.")

