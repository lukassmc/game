from settings import *
import sys
from main import *


def recargarpantalla():
        
        
    global x
    global cuentapasos
        
        
    if cuentapasos + 1 > 5:
            cuentapasos= 0
            
    if izquierda:
            PANTALLA.blit(correr_izquierda[cuentapasos // 1], (int(px), int(py)))
            cuentapasos += 1
            
    elif derecha:
            PANTALLA.blit(corre_derecha[cuentapasos // 1], (int(px), int(py)))
            cuentapasos += 1    
        
    elif salto:
            cuentapasos += 1 
            PANTALLA.blit(saltar[cuentapasos // 1], (int(px), int(py)))
            print("entra")
            
    else:
            PANTALLA.blit(quieto[indice_imagen], (int(px), int(py))) 
            cuentapasos += 1
    pygame.display.update() #actualiza la pantalla para que el jugador se muestre



           
