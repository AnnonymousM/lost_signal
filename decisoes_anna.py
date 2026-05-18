import random

possibilidades = [0, 10, 20] 

def buscar_agua(estado): #Recebe os valores do dicionário (estado) e o número que corresponde a escolha (escolha) 
        estado["agua"] += 20      #O valor de "agua" aumenta em 20
        estado["energia"] -= 10   #O valor de "energia" diminui em 10
        estado["sanidade"] -= random.choice(possibilidades) # O valor de "sanidade" diminui em um valor aleatório (0, 10 ou 20) 

def buscar_comida(estado):          #Recebe os valores do dicionário (estado) e o número que corresponde a escolha (escolha)               
        estado["comida"] += 20      #O valor de "comida" aumenta em 20
        estado["energia"] -= 20     #O valor de "energia" diminui em 20
        estado["sanidade"] -= random.choice(possibilidades)  # O valor de "sanidade" diminui em um valor aleatório (0, 10 ou 20) 

def descansar(estado): #Recebe os valores do dicionário (estado) e o número que corresponde a escolha (escolha) 
        estado["comida"] -= 10  #O valor de "comida" diminui em 10
        estado["agua"] -= 10    #O valor de "agua" diminui em 10
        estado["energia"] += 20 #O valor de "energia" aumenta em 20
        estado["sanidade"] += 10 #O valor de "sanidade" aumenta em 10
    

    
