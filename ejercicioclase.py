import pygame
import sys
from settings import *

pygame.init()



color_indice = 0

SCREEN = pygame.display.set_mode((800, 600))  
pygame.display.set_caption('rectangulo')  
reloj= pygame.time.Clock()
FPS= 60

#direcciones
DR= 3
DL= 7
UR= 6
UL= 5


block= {"rectangulo":pygame.Rect(300,250,200, 100), "color": BLANCO, "direccion": DL}

rect= 0
color= 1
dir= 2

# rect_1.center = SCREEN_CENTER
gravedad_x= True
gravedad_y= True
running = True


speed= 4

while running:
    reloj.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    SCREEN.fill((0,0,0))
    
    
    if block["direccion"] >= WIDTH:
        if block["direccion"] == DR:
            block["direccion"] = DL
        else:
            block["direccion"]= UL 
    elif block["direccion"] <= 0:
        if block["direccion"] == DL:
            block["direccion"] = DR
        else:
            block["direccion"]= UR
    elif block["direccion"] >= HEIGHT:
        if block["direccion"] == DR:
            block["direccion"] = UR
        else:
            block["direccion"]= UL
    elif block["direccion"] <= 0:
        if block["direccion"] == UR:
            block["direccion"] = DR
        else:
            block["direccion"]= DL
    
    
    
    
    
    if block["direccion"] == DR:
        
        block["rectangulo"].x += speed
        block["rectangulo"].y += speed
        
    elif block["direccion"]== DL:
        
        block["rectangulo"].x -= speed
        block["rectangulo"].y += speed
        
    elif block["direccion"] == UR:
        
        block["rectangulo"].x += speed
        block["rectangulo"].y -= speed
    else:
        
        block["rectangulo"].x -= speed
        block["rectangulo"].y -= speed
    # if gravedad_x:    
    #     if rect_1.right <= WIDTH:
    #         rect_1.x += speed
    #     else:
    #         gravedad_x= False
    # else:
    #     if rect_1.left >= 0:
    #         rect_1.x -= speed
    #     else:
    #         gravedad_x= True
    # if gravedad_y:    
    #     if rect_1.bottom <= HEIGHT:
    #         rect_1.y += speed
    #     else:
    #         gravedad_y= False
    # else:
    #     if rect_1.top >= 0:
    #         rect_1.y -= speed
    #     else:
    #         gravedad_y= True
    
       
        
    
    color_indice = (color_indice + 1) % len(COLORES)
    color_actual = COLORES[color_indice]

    pygame.draw.rect(SCREEN, color_actual, block)

    pygame.display.flip()

pygame.quit()
sys.exit()