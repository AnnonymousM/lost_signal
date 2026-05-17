import estado_yasmin
import historico_yasmin
import anna_ritter
import anna_ritter2

#dicionário aí né
estado = {
    "saude": 100,
    "energia": 80,
    "comida": 20,
    "agua": 20,
    "sanidade": 60
}

#acho que tem um negócio de armazenar o histórico tbm, qualquer coisa se n precisar e for alucinação minha a gnt tira
historico = []

#aí tem q mostrar a sua funçao de mostrar o estado 
#msm coisa com outra função de mostrar o menu sla

#pedir pro jogador
opcao = input("Escolha uma opção: ")


#exemplo aqui de funções suas hipotéticas
#buscar_agua, buscar_comida, descansar

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

#aí aqui tem q ser tipo aquela parte q mostra as coisas lá, as suas funções são hipotéticas mas as minhas tão aí
limitar_status(estado)
verificar_estado(estado)
mostrar_status(estado)
mostrar_historico(historico)
buscar_agua(estado)
buscar_comida(estado)
descansar(estado)
mostrar_menu(opcoes)
mostrar_status(estado)

