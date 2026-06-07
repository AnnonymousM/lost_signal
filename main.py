from estado_yasmin import verificar_estado, limitar_status
from historico_yasmin import mostrar_historico, registrar_acao
from decisoes_anna import buscar_agua, buscar_comida, descansar, exausto
from exibicao_anna import mostrar_menu, mostrar_status, mostrar_texto, verificar_final, fim_do_dia, exausto_texto

LIMITE_DIAS = 7 #aqui é uma constante que não vai mudar, por isso tá em maiúsculo
acao_texto = ("Você saiu pra buscar água.", "Você saiu pra buscar comida", "Você tirou o dia pra descansar.") #Texto que vai ser armazenado no histórico

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
resultado = "" #Guarda o resultado da função que verifica se está vivo/insano/etc

#Aqui começa o loop


while indice_dias < LIMITE_DIAS:
 
    mostrar_texto(indice_dias)
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
    fim_do_dia(indice_dias)
    
    if resultado == "exausto":
        exausto(estado)
        exausto_texto(resultado)

    elif resultado == "insano":
        sanidade_zerou = True  #o jogo continua mas o player entra num estado insano
 
    elif resultado == "morto":
        verificar_final(estado, sanidade_zerou, indice_dias, estado)
        mostrar_historico(historico)
        fim_de_jogo = True
        break

    
 
    indice_dias += 1

if fim_de_jogo == False:   #aqui é qnd já for os sete dias e ele estiver vivo
 

    verificar_final(estado, sanidade_zerou, indice_dias)
    mostrar_historico(historico)
