import random 
from frases import datos


def frotar(n_frases: int = 1):
    lista = []
    for _ in range(n_frases):
        lista.append(random.choice(datos))
    return lista



