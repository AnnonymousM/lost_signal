import random

possibilidades = [0, 10, 20, 30] 

def buscar_agua(estado): #Recebe os valores do dicionário (estado) 
        estado["agua"] += 20      #O valor de "agua" aumenta em 20
        estado["energia"] -= 25   #O valor de "energia" diminui em 25
        estado["sanidade"] -= random.choice(possibilidades) # O valor de "sanidade" diminui em um valor aleatório (0, 10, 20 ou 30) 

def buscar_comida(estado):          #Recebe os valores do dicionário (estado)               
        estado["comida"] += 20      #O valor de "comida" aumenta em 20
        estado["energia"] -= 35     #O valor de "energia" diminui em 35
        estado["sanidade"] -= random.choice(possibilidades)  # O valor de "sanidade" diminui em um valor aleatório (0, 10, 20 ou 30) 

def descansar(estado): #Recebe os valores do dicionário (estado) 
        estado["comida"] -= 20  #O valor de "comida" diminui em 20
        estado["agua"] -= 20    #O valor de "agua" diminui em 20
        estado["energia"] += 25 #O valor de "energia" aumenta em 25
        estado["sanidade"] += 15 #O valor de "sanidade" aumenta em 15
    

def exausto(estado): #Recebe os valores do dicionário (estado) 
        estado["comida"] -= 30  #O valor de "comida" diminui em 30
        estado["agua"] -= 30    #O valor de "agua" diminui em 30
        estado["energia"] += 35 #O valor de "energia" aumenta em 35
        estado["sanidade"] += 5 #O valor de "sanidade" aumenta em 5
        estado["saude"] -= 50 #O valor de "saude" diminui em 50
    
    
    

    
