from estado_yasmin import verificar_estado, limitar_status
from historico_yasmin import mostrar_historico, registrar_acao
from decisoes_anna import buscar_agua, buscar_comida, descansar
from exibicao_anna import mostrar_menu, mostrar_status, mostrar_texto, verificar_final

LIMITE_DIAS = 7 #aqui é uma constante que não vai mudar, por isso tá em maiúsculo
acao_texto = ("Você saiu pra buscar água.", "Você saiu pra buscar comida", "Você tirou o dia pra descansar.")

estado = {
    "saude": 100,
    "energia": 80,
    "comida": 20,
    "agua": 20,
    "sanidade": 60
}

fim_de_jogo = False
historico = []
indice_dias = 0 #Quantos dias já se passaram 
sanidade_zerou = False #se a sanidade zerar alguma vez automaticamente é um final ruim
resultado = ""

#as coisas que tinham aqui eu coloquei dentro do while já q tem q ficar repetindo


while indice_dias < LIMITE_DIAS:
    mostrar_texto(indice_dias)
    if indice_dias > 0:
        mostrar_status(estado)
 
    opcao = mostrar_menu(indice_dias)
 
    if opcao == "1":
        buscar_agua(estado)
        registrar_acao(historico, acao_texto[0])
 
    elif opcao == "2":
        buscar_comida(estado)
        registrar_acao(historico, acao_texto[1])
 
    elif opcao == "3":
        descansar(estado)
        registrar_acao(historico, acao_texto[2])
 
    else:
        print("Opção inválida! Tente novamente.")
        continue  #aqui não vai avançar o dia se o q o player escolher for inválido
 
    limitar_status(estado)
    mostrar_status(estado)
    
    
    resultado = verificar_estado(estado)
    
    if resultado == "insano":
        sanidade_zerou = True  #o jogo continua mas o player entra num estado insano
 
    if not vivo:
        verificar_final(estado, sanidade_zerou, indice_dias)
        mostrar_historico(historico)
        fim_de_jogo = True
        break

    
 
    indice_dias += 1

if fim_de_jogo == False:
 

    #aqui é qnd já for os sete dias e ele estiver vivo
    verificar_final(estado, sanidade_zerou, indice_dias)
    mostrar_historico(historico)


limitar_status(estado)
verificar_estado(estado)
mostrar_status(estado)
mostrar_historico(historico)
buscar_agua(estado)
buscar_comida(estado)
descansar(estado)
mostrar_menu(indice_dias)
mostrar_status(estado)
mostrar_texto(indice_dias)
