import random

possibilidades = [0, 10, 20] 

def buscar_agua(estado, escolha): #Recebe os valores do dicionário (estado) e o número que corresponde a escolha (escolha) 
    if escolha == 1:              #Se a escolha for 1 (buscar água) executa o bloco de código abaixo
        estado["agua"] += 20      #O valor de "agua" aumenta em 20
        estado["energia"] -= 10   #O valor de "energia" diminui em 10
        estado["sanidade"] -= random.choice(possibilidades) # O valor de "sanidade" diminui em um valor aleatório (0, 10 ou 20) 

def buscar_comida(estado, escolha): #Recebe os valores do dicionário (estado) e o número que corresponde a escolha (escolha) 
    if escolha == 2:                #Se a escolha for 2 (buscar comida) executa o bloco de código abaixo
        estado["comida"] += 20      #O valor de "comida" aumenta em 20
        estado["energia"] -= 20     #O valor de "energia" diminui em 20
        estado["sanidade"] -= random.choice(possibilidades)  # O valor de "sanidade" diminui em um valor aleatório (0, 10 ou 20) 

def descansar(estado, escolha): #Recebe os valores do dicionário (estado) e o número que corresponde a escolha (escolha) 
    if escolha == 3:            #Se a escolha for 3 (descansar) executa o bloco de código abaixo
        estado["comida"] -= 10  #O valor de "comida" diminui em 10
        estado["agua"] -= 10    #O valor de "agua" diminui em 10
        estado["energia"] += 20 #O valor de "energia" aumenta em 20
        estado["sanidade"] += 10 #O valor de "sanidade" aumenta em 10
    
