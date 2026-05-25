from estado_yasmin import verificar_estado, limitar_status
from historico_yasmin import mostrar_historico, registrar_acao
from decisoes_anna import buscar_agua, buscar_comida, descansar
from exibicao_anna import mostrar_menu, mostrar_status, mostrar_texto

LIMITE_DIAS = 7 #aqui é uma constante que não vai mudar, por isso tá em maiúsculo

estado = {
    "saude": 100,
    "energia": 80,
    "comida": 20,
    "agua": 20,
    "sanidade": 60
}

historico = []
indice_dias = 0 #Quantos dias já se passaram 
sanidade_zerou = False #se a sanidade zerar alguma vez automaticamente é um final ruim

#as coisas que tinham aqui eu coloquei dentro do while já q tem q ficar repetindo


while indice_dias < LIMITE_DIAS:
    mostrar_texto(indice_dias)
    mostrar_status(estado)
 
    opcao = mostrar_menu(indice_dias)
 
    if opcao == "1":
        buscar_agua(estado)
        registrar_acao(historico, "Você decide sair para buscar água e felizmente encontra um  riacho.")
 
    elif opcao == "2":
        buscar_comida(estado)
        registrar_acao(historico, "Você decide sair pra buscar comida e felizmente encontra algumas frutas")
 
    elif opcao == "3":
        descansar(estado)
        registrar_acao(historico, "Você está exausto e tira o dia para descansar.")
 
    else:
        print("Opção inválida! Tente novamente.")
        continue  #aqui não vai avançar o dia se o q o player escolher for inválido
 
    limitar_status(estado)
 
    vivo = verificar_estado(estado)  #True se vivo, False se morreu
 
    mostrar_historico(historico)
 
    if not vivo:
        verificar_final(estado, sanidade_zerou)
        break

    if resultado == "insano":
        sanidade_zerou = True  #o jogo continua mas o player entra num estado insano
 
    indice_dias += 1
 
else:
    #aqui é qnd já for os sete dias e ele estiver vivo
    verificar_final(estado, sanidade_zerou)


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
