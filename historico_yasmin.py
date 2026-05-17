#pra mostrar o historico
def mostrar_historico(historico):

    print("\n=== HISTÓRICO ===")

    for acao in historico:
        print("-", acao)


#pra registrar as ações ??
def registrar_acao(historico, acao):

    historico.append(acao)