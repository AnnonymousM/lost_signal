#pra verificar as derrotas
def verificar_estado(estado):

    if estado["saude"] <= 0:
        print("\nVocê morreu.")

    elif estado["energia"] <= 0:
        print("\nVocê ficou sem energia.")

    elif estado["sanidade"] <= 0:
        print("\nVocê enlouqueceu.")

#limitando os estados pra n dar erro por enquanto (sem numero negativo)
#e tbm pra eles n ficarem mais de 100 (vai q né)
def limitar_status(estado):

    if estado["energia"] > 100:
        estado["energia"] = 100

    if estado["energia"] < 0:
        estado["energia"] = 0

    if estado["comida"] > 100:
        estado["comida"] = 100

    if estado["comida"] < 0:
        estado["comida"] = 0

    if estado["agua"] > 100:
        estado["agua"] = 100

    if estado["agua"] < 0:
        estado["agua"] = 0