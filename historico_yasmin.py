#pra mostrar o historico pro player
def mostrar_historico(historico):

    print("\n=== HISTÓRICO ===")

    for acao in historico:
        print("-", acao)


#pra registrar as ações e ir guardando o que o player foi escolhendo dentro de historico
def registrar_acao(historico, acao):

    historico.append(acao)