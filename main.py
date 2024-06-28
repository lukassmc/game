import pygame

from settings import *


class Puerta(pygame.sprite.Sprite):
    def __init__(self, posicion):
        
        super().__init__()
        
        self.puerta = pygame.image.load("imagenes/puerta.png")
        self.puerta_damaged= pygame.image.load("imagenes/puerta_damage.png")
        self.image= self.puerta
        self.rect= self.image.get_rect(topleft= posicion)
        

        self.damaged_frames= 0
        self.vida= 20
    
    def recibir_dmg(self, dmg):
        self.vida -= dmg
        self.image= self.puerta_damaged
        self.damaged_frames= 15
        if self.vida == 0:
            self.kill()
        
    def update(self):
        if self.damaged_frames > 0:
            self.damaged_frames -= 1
            print(self.damaged_frames)
        if self.damaged_frames == 0:
            self.image= self.puerta
    
        



class Player(pygame.sprite.Sprite):
    
    
    def __init__(self, posicion) -> None:
        
        super().__init__()#herede las funciones de Sprites
        
        self.quieto_animacion =[ pygame.image.load("personaje/idle.png"),
            pygame.image.load("personaje/idle2.png"),
            pygame.image.load("personaje/idle3.png"),
            pygame.image.load("personaje/idle4.png")
    ]
        self.izquierda_animacion=[ pygame.image.load("personaje/run1_izq.png"),
                    pygame.image.load("personaje/run2_izq.png"),
                    pygame.image.load("personaje/run3_izq.png"),
                    pygame.image.load("personaje/run4_izq.png"),
                    pygame.image.load("personaje/run5_izq.png"),
                    pygame.image.load("personaje/run6_izq.png")   
    ]
        self.derecha_animacion=[ pygame.image.load("personaje/run1.png"),   
                    pygame.image.load("personaje/run2.png"),
                    pygame.image.load("personaje/run3.png"),
                    pygame.image.load("personaje/run4.png"),
                    pygame.image.load("personaje/run5.png"),
                    pygame.image.load("personaje/run6.png")    
         ]
       
        self.frame_indice= 0
        self.image= self.quieto_animacion[self.frame_indice]
        self.rect= self.image.get_rect()
        self.topleft= posicion
        
        self.damage= 3
        self.speed= 7
        self.attack_speed= 2
     
    indice_imagen= 0
    def obtener_frame(self, contador_frame)-> int:
        global indice_imagen
        contador_frame += 0.20
    
        if contador_frame // 1 == 1:
            
            indice_imagen += 1
            contador_frame= 0
        
        if indice_imagen >= 4:
            indice_imagen = 0
        
        return indice_imagen
        
    def update(self) -> None:
        global izquierda
        global derecha
        global cuentapasos
        
        tecla= pygame.key.get_pressed() #obtiene la tecla presionada
    
        if tecla[pygame.K_1]:
            self.rect.y= PLATAFORMA_1Y - 65
        if tecla[pygame.K_2]:
            self.rect.y= PLATAFORMA_2Y - 65
        if tecla[pygame.K_3]:
            self.rect.y= PLATAFORMA_3Y - 65
            
            
        if tecla[pygame.K_a] and self.rect.x > 10 :
            self.rect.x -= self.speed
            izquierda= True
            derecha= False
            
            
            
        elif tecla[pygame.K_d] and self.rect.x < 1240 - self.speed - ancho:
            self.rect.x += self.speed
            izquierda= False
            derecha= True
            
        else:
            cuentapasos= 0
            derecha= False
            izquierda= False  
            
    def animar(self):
            
            
        global x
        global cuentapasos
            
        frame=  int(player.obtener_frame(cuentapasos)) 
          
        if cuentapasos + 1 > 5:
                cuentapasos= 0
                
        if izquierda:
                PANTALLA.blit(player.izquierda_animacion[frame], (int(self.rect.x), int(self.rect.y)))
                cuentapasos += 1
                
        elif derecha:
                PANTALLA.blit(player.derecha_animacion[frame], (int(self.rect.x), int(self.rect.y)))
                cuentapasos += 1    
            
                
        else:
                PANTALLA.blit(player.quieto_animacion[frame], (int(self.rect.x), int(self.rect.y))) 
                cuentapasos += 1
        pygame.display.update() #actualiza la pantalla para que el jugador se muestre
        
        
        
        
        
def barra_hp(pantalla, x, y, vida):
    largo= 200
    ancho= 15
    calculo_largo_barra= int((vida / 100) * largo)
    borde= pygame.Rect(x,y, largo, ancho)
    
    rectangulo= pygame.Rect(x, y, calculo_largo_barra, ancho)
    pygame.draw.rect(PANTALLA, (160, 255, 0), borde, 3)
    pygame.draw.rect(PANTALLA, (80, 255, 0), rectangulo)
    
    

        
pygame.init() 
PANTALLA= pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Juego")


reloj= pygame.time.Clock()



#Fondo del juego
fondo= pygame.image.load("imagenes/fondolvl1.png")
PANTALLA.blit(fondo, (0,0))



    
  





px, py= 67, 594 
puerta1= Puerta((0,24))
puerta2= Puerta((0,249))
puerta3= Puerta((0,465))

puertas= pygame.sprite.Group()
puertas.add(puerta1)
puertas.add(puerta2)
puertas.add(puerta3)




player= Player((px,py))
sprites= pygame.sprite.Group()
sprites.add(player)


game_over= False
while game_over == False:
    reloj.tick(60)
    
      #Refresca la pantalla al color negro
    fondo= pygame.image.load("imagenes/fondolvl1.png")
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over= True 
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Simular golpe a la puerta con la barra espaciadora
                        puerta1.recibir_dmg(10)
                        puerta2.recibir_dmg(5)
                        puerta3.recibir_dmg(5)
                        
    
    
    
    
    
    
    player.update()
    puerta1.update()
    puerta2.update()
    puerta3.update()
   
       
    
        
 
    
    #se le da una orden de movimiento segun la tecla presionada
    pygame.display.update()
    PANTALLA.blit(fondo, (0,0))
    puertas.draw(PANTALLA)
    player.animar()

pygame.quit()
# <> \ 215, 378