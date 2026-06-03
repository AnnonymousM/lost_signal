#pra verificar as derrotas, qualquer coisa abaixo de 0 é igual derrota (por enquanto como não tem looping, não tem como morrer de sede ou fome, 
#e nem a questão da sanidade não ser tecnicamente derrota, e sim um final ruim, mas é pra ter uma função pra isso, e aí a gnt pode ir ajustando depois)
def verificar_estado(estado):
 
    if estado["saude"] <= 0:
        return "morto"
 
    elif estado["energia"] <= 0:
        return "morto"
 
    elif estado["sanidade"] <= 0:
        return "insano"
 
    return "vivo"
#mudei aqui pq eu descobri que desse jeito funciona igual só q fica menos verboso :)
def limitar_status(estado):
 
    for chave in ["energia", "comida", "agua", "saude", "sanidade"]:
        if chave in estado:
            if estado[chave] > 100:
                estado[chave] = 100
            if estado[chave] < 0:
                estado[chave] = 0
