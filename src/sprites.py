import pygame
from settings import *
from classes import Player, Puerta, Disparo, Enemigo



'---------------------------------------------- BALAS --------------------------------------'
balas= pygame.sprite.Group()

'---------------------------------------------- PUERTAS --------------------------------------'
px, py= 65, 490
puerta1= Puerta((0,24))
puerta2= Puerta((0,249))
puerta3= Puerta((0,465)) 
puertas= pygame.sprite.Group()
puertas.add(puerta1, puerta2, puerta3)

'---------------------------------------------- JUGADOR --------------------------------------'
player= Player((px, py))
sprites= pygame.sprite.Group()
sprites.add(player)

'---------------------------------------------- ENEMIGO --------------------------------------'
posicion_plataforma1=PLATAFORMA_1Y - 70
posicion_plataforma2=PLATAFORMA_2Y - 70
posicion_plataforma3=PLATAFORMA_3Y - 70

enemigos= pygame.sprite.Group()
enemigo1 = Enemigo((WIDTH - 84, posicion_plataforma1), 15, 100, 2)
enemigo2 = Enemigo((WIDTH - 84, posicion_plataforma2), 15, 100, 2)
enemigo3 = Enemigo((WIDTH - 84, posicion_plataforma3), 15, 100, 2)
enemigos.add(enemigo1, enemigo2, enemigo3)

