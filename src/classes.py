import pygame
from settings import *
from sounds import *


class Puerta(pygame.sprite.Sprite):
    def __init__(self, posicion):
        
        super().__init__()
        
        self.puerta = pygame.image.load("assets/imagenes/puerta.png")
        self.puerta_damaged= pygame.image.load("assets/imagenes/puerta_damage.png")
        self.image= self.puerta
        self.rect= self.image.get_rect(topleft= posicion)
        

        self.damaged_frames= 0
        self.vida= 100
    
    def recibir_dmg(self, dmg):
        self.vida -= dmg
        self.image= self.puerta_damaged
        self.damaged_frames= 15
        if self.vida <= 0:
            self.kill()
        
    def update(self):
        if self.damaged_frames > 0:
            self.damaged_frames -= 1
            
        if self.damaged_frames == 0:
            self.image= self.puerta
    
class Player(pygame.sprite.Sprite):
    
    
    def __init__(self, posicion) -> None:
        
        super().__init__()#herede las funciones de Sprites
        
        self.quieto_animacion =[ pygame.image.load("assets/personaje/idle.png"),
                            pygame.image.load("assets/personaje/idle2.png")
    ]
        self.izquierda_animacion=[ pygame.image.load("assets/personaje/fly_izq.png"),
                      pygame.image.load("assets/personaje/fly2_izq.png")
    ]
        self.derecha_animacion=[ pygame.image.load("assets/personaje/fly1.png"),
                                pygame.image.load("assets/personaje/fly2.png")
    ]
        
        self.rojo_animacion= [ pygame.image.load("assets/personaje/rojo1.png"),
                            pygame.image.load("assets/personaje/rojo2.png"),
                            pygame.image.load("assets/personaje/rojo3.png"),
                            pygame.image.load("assets/personaje/rojo4.png"),
                            pygame.image.load("assets/personaje/rojo5.png"),
                            pygame.image.load("assets/personaje/rojo6.png"),
                            pygame.image.load("assets/personaje/rojo7.png"),
                            pygame.image.load("assets/personaje/rojo8.png"),
                            pygame.image.load("assets/personaje/rojo9.png"),
                            pygame.image.load("assets/personaje/rojo10.png"),
                            pygame.image.load("assets/personaje/rojo11.png")
        ]
        self.azul_animacion= [ pygame.image.load("assets/personaje/azul1.png"),
                              
                            pygame.image.load("assets/personaje/azul2.png"),
                            pygame.image.load("assets/personaje/azul3.png"),
                            pygame.image.load("assets/personaje/azul4.png"),
                            pygame.image.load("assets/personaje/azul5.png"),
                            pygame.image.load("assets/personaje/azul6.png"),
                            pygame.image.load("assets/personaje/azul7.png"),
                            pygame.image.load("assets/personaje/azul8.png"),
                            pygame.image.load("assets/personaje/azul9.png")  
                            
                              ]
        self.purple_animacion= [ pygame.image.load("assets/personaje/purple1.png"),
                            pygame.image.load("assets/personaje/purple2.png"),
                            pygame.image.load("assets/personaje/purple3.png"),
                            pygame.image.load("assets/personaje/purple4.png"),
                            pygame.image.load("assets/personaje/purple5.png"),
                            pygame.image.load("assets/personaje/purple6.png"),
                            pygame.image.load("assets/personaje/purple7.png"),
                            pygame.image.load("assets/personaje/purple8.png"),
                            pygame.image.load("assets/personaje/purple9.png"),
                            pygame.image.load("assets/personaje/purple10.png"),
                            
        ]
        
        self.frame_indice= 0
        self.image= self.quieto_animacion[self.frame_indice]
        self.rect= self.image.get_rect(topleft= posicion)
        
        self.damage= 25
        self.speed= 7
        self.max_cursed_energy= 100
        self.current_cursed_energy= 0
        
        self.attack_speed= 250
        self.tiempo_atacar= pygame.time.get_ticks()
     
    indice_imagen= 0
    def obtener_frame(self, contador_frame)-> int:
        global indice_imagen
        contador_frame += 0.20
    
        if contador_frame // 1 == 1:
            
            indice_imagen += 1
            contador_frame= 0
        
        if indice_imagen >= 1:
            indice_imagen = 0
        
        return indice_imagen
        
    def update(self) -> None:
        global izquierda
        global derecha
        global cuentapasos
        
        tecla= pygame.key.get_pressed() #obtiene la tecla presionada
    
        if tecla[pygame.K_1]:
            self.rect.y= PLATAFORMA_1Y - self.rect.height
           
        if tecla[pygame.K_2]:
            self.rect.y= PLATAFORMA_2Y - self.rect.height
            
        if tecla[pygame.K_3]:
            self.rect.y= PLATAFORMA_3Y - self.rect.height
            
            
            
            
        if tecla[pygame.K_a] and self.rect.x > 65:
            self.rect.x -= self.speed
            izquierda= True
            derecha= False
            
            
            
        elif tecla[pygame.K_d] and self.rect.x < 400 - self.speed - ancho:
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
            
        frame_animacion=  int(self.obtener_frame(cuentapasos)) 
          
        if cuentapasos + 1 > 5:
                cuentapasos= 0
                
        if izquierda:
                PANTALLA.blit(self.izquierda_animacion[frame_animacion], (int(self.rect.x), int(self.rect.y)))
                cuentapasos += 1
                
        elif derecha:
                PANTALLA.blit(self.derecha_animacion[frame_animacion], (int(self.rect.x), int(self.rect.y)))
                cuentapasos += 1    
            
                
        else:
                PANTALLA.blit(self.quieto_animacion[frame_animacion], (int(self.rect.x), int(self.rect.y))) 
                cuentapasos += 1
        pygame.display.update() #actualiza la pantalla para que el jugador se muestre
        
        
        
    def disparar(self, sprite_group, tipo):
        tiempo= pygame.time.get_ticks()
        
        if tiempo - self.tiempo_atacar > self.attack_speed:
            match tipo:
                case "Rojo":
                    shoot= Disparo(self.rect.centerx, self.rect.centery, 80, f"{tipo}", 10)
                    reversal_red.play()
                    self.current_cursed_energy -= 50
                    
                case "Azul":
                    shoot= Disparo(self.rect.centerx, self.rect.centery, 100, f"{tipo}", 10)
                    lapse_blue.play()
                    self.current_cursed_energy -= 50
                    
                case "Violeta":
                    shoot= Disparo(self.rect.centerx, self.rect.centery, 10000, f"{tipo}", 2)
                    hollow_purple_long.play()
                    self.current_cursed_energy -= 100
                    
                case _:
                    shoot= Disparo(self.rect.centerx, self.rect.centery, self.damage, "bala", 15)
                    shoot_sound.play()
                      
               
                
            sprite_group.add(shoot)
            self.tiempo_atacar = tiempo
            
            
        
class Disparo(pygame.sprite.Sprite):
    def __init__(self, current_x, current_y, damage, type, projectile_speed):
        super().__init__()
        if type == "Rojo":
            self.image = pygame.image.load("assets/personaje/rojo_proyectil.png")
            
        elif type == "Azul":
            self.image = pygame.image.load("assets/personaje/azul_proyectil.png")
            
        elif type == "Violeta":
            self.image = pygame.image.load("assets/personaje/purple_projectile.png")
            
        else:
            self.image = pygame.transform.scale(pygame.image.load("assets/personaje/bala.png").convert(), (20, 10))

        self.current_x = current_x
        self.current_y = current_y
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=(current_x, current_y))
        self.type = type
        self.projectile_speed = projectile_speed
        self.damage = damage

    def update(self):
        self.rect.x += self.projectile_speed
        if self.rect.left > WIDTH:
            self.kill()



class Enemigo(pygame.sprite.Sprite):
    
    def __init__(self, posicion, damage, vida, speed):
        
        super().__init__()
        
       
        
        self.caminar_animacion= [ pygame.image.load("assets/enemy/caminar_enemigo.png"),
                                pygame.image.load("assets/enemy/caminar_enemigo2.png"),
                                pygame.image.load("assets/enemy/caminar_enemigo3.png"),
                                pygame.image.load("assets/enemy/caminar_enemigo4.png"),
                                pygame.image.load("assets/enemy/caminar_enemigo5.png"),
                                pygame.image.load("assets/enemy/caminar_enemigo6.png"),
                                pygame.image.load("assets/enemy/caminar_enemigo7.png"),
                                pygame.image.load("assets/enemy/caminar_enemigo8.png"),
                                pygame.image.load("assets/enemy/caminar_enemigo9.png"),
                                pygame.image.load("assets/enemy/caminar_enemigo10.png"),
                                pygame.image.load("assets/enemy/caminar_enemigo11.png"),

        ]
        
        self.muerte_animacion= [ pygame.image.load("assets/enemy/enemy_dead1.png"),
                                pygame.image.load("assets/enemy/enemy_dead2.png"),
                                pygame.image.load("assets/enemy/enemy_dead3.png"),
                                pygame.image.load("assets/enemy/enemy_dead4.png"),
                                pygame.image.load("assets/enemy/enemy_dead5.png"),
                                pygame.image.load("assets/enemy/enemy_dead6.png"),
                                pygame.image.load("assets/enemy/enemy_dead7.png"),
                                pygame.image.load("assets/enemy/enemy_dead8.png"),
                                pygame.image.load("assets/enemy/enemy_dead9.png"),
                                
                                
            
        ]
        self.get_hit_img = pygame.image.load("assets/enemy/enemy_dead1.png")
        
        self.frame_indice = 0
        self.image = self.caminar_animacion[self.frame_indice]
        self.rect = self.image.get_rect(topleft=posicion)
        self.contador_frame = 0
        self.damage = damage
        self.vida = vida
        self.speed = speed
        self.muriendo = False

    def obtener_frame(self, animacion):
        self.contador_frame += 0.25
        if self.contador_frame >= 1:
            self.frame_indice += 1
            self.contador_frame = 0

        # Asegúrate de que el frame_indice esté dentro del rango de la animación
        if self.frame_indice >= len(animacion):
            if self.muriendo:
                self.frame_indice = len(animacion) - 1
            else:
                self.frame_indice = 0
        
        return self.frame_indice

    def update(self):
        
        if self.vida > 0:
            
            if self.rect.x > 65:
                self.rect.x -= self.speed
                
            frame = self.obtener_frame(self.caminar_animacion)
            self.image = self.caminar_animacion[frame]
            
        else:
            if not self.muriendo:
                self.muriendo = True
                self.frame_indice = 0  # Reiniciar índice de frame para la animación de muerte
            frame = self.obtener_frame(self.muerte_animacion)
            
            if frame < len(self.muerte_animacion):  # Verificación adicional
                self.image = self.muerte_animacion[frame]
            else:
                print(f"Error: Frame indice {frame} fuera de rango para la animacion de muerte.")
                
            if self.frame_indice == len(self.muerte_animacion) - 1:
                self.kill()
            
    def recibir_dmg(self, cantidad):
        self.vida -= cantidad
        self.image= self.get_hit_img

        
    
