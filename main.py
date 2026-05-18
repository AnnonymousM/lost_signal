from estado_yasmin import verificar_estado, limitar_status
from historico_yasmin import mostrar_historico, registrar_acao
from decisoes_anna import buscar_agua, buscar_comida, descansar
from exibicao_anna import mostrar_menu, mostrar_status, mostrar_texto

estado = {
    "saude": 100,
    "energia": 80,
    "comida": 20,
    "agua": 20,
    "sanidade": 60
}
historico = []

indice_dias = 0 #Quantos dias já se passaram 

mostrar_texto(indice_dias)

opcao = mostrar_menu(indice_dias)



if opcao == "1":
    buscar_agua(estado) #aí toda vez que vc colocar sua função tem q usar a minha de registrar
    registrar_acao(historico, "Buscou água")

elif opcao == "2":
    buscar_comida(estado)
    registrar_acao(historico, "Buscou comida")

elif opcao == "3":
    descansar(estado)
    registrar_acao(historico, "Descansou")

else:
    print("Opção inválida!")

mostrar_texto(indice_dias)
mostrar_status(estado)



#aí aqui tem q ser tipo aquela parte q mostra as coisas lá, as suas funções são hipotéticas mas as minhas tão aí
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
