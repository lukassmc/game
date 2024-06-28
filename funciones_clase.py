from random import randrange, randint




# funcion que reciba lista y retorne un elemento de la misma de manera aleatoria

def get_random_element(lista:list)->any:
    return lista[randrange(len(lista))]


def get_random_color(colors: list):
    return get_random_element(colors)


def random_color()->tuple[int,int,int]:
    
    color_random= (randint(0,255),randint(0,255),randint(0,255))
    
    return color_random


print(random_color())