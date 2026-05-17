import random 
possibilidades = [0,10,20]


def consequencia(saude: int, energia: int, comida: int, agua: int, sanidade:int) -> int: # 1 = agua 2 = comida 3 = dormir
  if escolha == 1:
    status[agua] += 20
    status[energia] -= 10
    status[energia] -= possibilidades.choice()
    
