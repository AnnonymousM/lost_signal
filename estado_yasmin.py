def verificar_estado(estado): #A função recebe o dicionário dos estados como arg
 
    if estado["saude"] <= 0:  #Se o valor das chaves comida, água ou saúde for igual a 0, retorna "morto"
        return "morto"

    elif estado["agua"] <= 0:
        return "morto"
    
    elif estado["comida"] <= 0:
        return "morto"
 
    elif estado["energia"] <= 0:  #Se o valor da chave energia for igual a 0, retorna "exausto"
        return "exausto"
 
    elif estado["sanidade"] <= 0: #Se o valor da chave sanidade for igual a 0, retorna "insano"
        return "insano"
 
    return "vivo"
#não deixa os status passarem de 100 ou ficarem menos que 0
def limitar_status(estado):
 
    for chave in ["energia", "comida", "agua", "saude", "sanidade"]:
        if chave in estado:
            if estado[chave] > 100:
                estado[chave] = 100
            if estado[chave] < 0:
                estado[chave] = 0
