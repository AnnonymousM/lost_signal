import random

possibilidades = [0, 10, 20]

def buscar_agua(estado, escolha):
    if escolha == 1:
        estado["agua"] += 20
        estado["energia"] -= 10
        estado["sanidade"] -= random.choice(possibilidades)

def buscar_comida(estado, escolha):
    if escolha == 1:
        estado["comida"] += 20
        estado["energia"] -= 20
        estado["sanidade"] -= random.choice(possibilidades)

def descansar(estado, escolha):
    if escolha == 1:
        estado["comida"] -= 10
        estado["agua"] -= 10
        estado["energia"] += 20
        estado["sanidade"] += 10
    
