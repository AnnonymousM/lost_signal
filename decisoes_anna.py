import random

possibilidades = [0, 10, 20, 30] 

def buscar_agua(estado): #Recebe os valores do dicionário (estado) e o número que corresponde a escolha (escolha) 
        estado["agua"] += 20      #O valor de "agua" aumenta em 20
        estado["energia"] -= 25   #O valor de "energia" diminui em 25
        estado["sanidade"] -= random.choice(possibilidades) # O valor de "sanidade" diminui em um valor aleatório (0, 10, 20 ou 30) 

def buscar_comida(estado):          #Recebe os valores do dicionário (estado) e o número que corresponde a escolha (escolha)               
        estado["comida"] += 20      #O valor de "comida" aumenta em 20
        estado["energia"] -= 35     #O valor de "energia" diminui em 35
        estado["sanidade"] -= random.choice(possibilidades)  # O valor de "sanidade" diminui em um valor aleatório (0, 10, 20 ou 30) 

def descansar(estado): #Recebe os valores do dicionário (estado) e o número que corresponde a escolha (escolha) 
        estado["comida"] -= 20  #O valor de "comida" diminui em 20
        estado["agua"] -= 20    #O valor de "agua" diminui em 20
        estado["energia"] += 25 #O valor de "energia" aumenta em 25
        estado["sanidade"] += 15 #O valor de "sanidade" aumenta em 15
    

    
