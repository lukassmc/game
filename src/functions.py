from settings import *
import time
from classes import *

    


def barra_hp(surface, x, y, vida)-> None:
    largo= 200
    ancho= 15
    calculo_largo_barra= int((vida / 100) * largo) # se calcula la longitud del largo de la barra como porcentaje
    borde= pygame.Rect(x,y, calculo_largo_barra, ancho)
    rectangulo= pygame.Rect(x, y, calculo_largo_barra, ancho)
    
    pygame.draw.rect(surface, (80, 100, 55), rectangulo)
    pygame.draw.rect(surface, NEGRO, borde, 3)
    
    if vida <= 30:
        pygame.draw.rect(surface, (255, 160, 0), rectangulo)
        pygame.draw.rect(surface, NEGRO, borde, 3)
    if vida <= 10:
        pygame.draw.rect(surface, (255, 40, 0), rectangulo)
        pygame.draw.rect(surface, NEGRO, borde, 3)
        
        
        
        
        
def barra_hp_enemigos(surface, x, y, vida)-> None:
    largo= 100
    ancho= 10
    calculo_largo_barra= int((vida / 100) * largo) 
    borde= pygame.Rect(x,y, calculo_largo_barra, ancho)
    rectangulo= pygame.Rect(x, y, calculo_largo_barra, ancho)
    
    pygame.draw.rect(surface, (80, 100, 55), rectangulo)
    pygame.draw.rect(surface, NEGRO, borde, 3)
    
    if vida <= 30:
        pygame.draw.rect(surface, (255, 160, 0), rectangulo)
        pygame.draw.rect(surface, NEGRO, borde, 3)
    if vida <= 10:
        pygame.draw.rect(surface, (255, 40, 0), rectangulo)
        pygame.draw.rect(surface, NEGRO, borde, 3)

def cursed_energy_bar(surface, x, y, actual_cursed_energy,cursed_energy_max)-> None:
    largo_barra = 200
    ancho_barra = 25
    fill = (actual_cursed_energy / cursed_energy_max) * largo_barra
    borde = pygame.Rect(x, y, largo_barra, ancho_barra)
    fill_rect = pygame.Rect(x, y, fill, ancho_barra)
    pygame.draw.rect(surface, NAVY_BLUE, fill_rect)
    pygame.draw.rect(surface, NEGRO, borde, 3)  # Color del borde de la barra (negro)
    
  
        
       
        
def muestra_texto(pantalla, fuente, texto,color, dimensiones,x, y):
        tipo_letra = pygame. font.Font(fuente,dimensiones)
        superficie = tipo_letra.render(texto, True, color)
        rectangulo = superficie.get_rect()
        rectangulo.center= (x, y)
        pantalla.blit(superficie, rectangulo)
 
        
def muestra_avisos(pantalla, fuente, texto, color, dimensiones,x, y, duracion):
        duracion= duracion * 100
        
        tipo_letra = pygame.font.Font(fuente,dimensiones)
        superficie = tipo_letra.render(texto, True, color)
        
        rectangulo = superficie.get_rect()
        rectangulo.center= (x, y)
        
        
        while duracion > 0:
            pantalla.blit(superficie, rectangulo)
            duracion -= 1
            
            
        
        
        
def mostrar_tiempo_restante(pantalla, fuente, color, dimensiones, x, y, tiempo_final):
       
    
    if time.time() <= tiempo_final:
            tiempo_restante= int(tiempo_final - time.time())
            texto= f"Tiempo restante:"
            muestra_texto(pantalla, fuente, texto + str(tiempo_restante), color, dimensiones, x, y)
        
    return tiempo_restante
                
                
                
def mostrar_puntuacion(pantalla, fuente, color, dimensiones, x, y, score):
    texto = f"Score: {score}"
    muestra_texto(pantalla, fuente, texto, color, dimensiones, x, y)







def guardar_puntuacion(nombre, score, texto,archivo="high_scores.csv"):
    with open(archivo, mode='a', newline='') as file:
        file.write(f"{nombre},{score}, {texto}\n")

def crear_enemigos_random(tiempo_final, spritegroup, plataforma, tiempos_creacion, enemigos_creados):
    
    
    tiempo_restante = int(tiempo_final - time.time())
    
    for segundo_a_crear_enemigo in tiempos_creacion:
        if tiempo_restante == segundo_a_crear_enemigo and segundo_a_crear_enemigo not in enemigos_creados:
            enemigo_nuevo = Enemigo((WIDTH - 84, plataforma), 10, 100, 2)
            spritegroup.add(enemigo_nuevo)
            enemigos_creados.add(segundo_a_crear_enemigo)
            

            
def game_over_screen(pantalla, fuente, score, tiempo_supervivencia):
    """Muestra una pantalla blanca con un texto "Game over.", su puntuacion, el tiempo que sobrevivio,y para ingresar su nombre, y guarda esta info en un archivo csv

    Args:
        pantalla (_type_): Superficie a dibujar
        fuente (_type_): fuente a utilizar
        score (_type_): Puntuacion
        tiempo_supervivencia (_type_): Tiempo sobrevivido
    """
    pygame.mixer.music.pause()
    bleach.play()
    pantalla.fill(NEGRO)
    
    muestra_texto(pantalla, fuente, "Game Over", (255, 0, 0), 50, 400, 100)
    muestra_texto(pantalla, fuente, f"Tiempo sobrevivido: {tiempo_supervivencia} segundos", BLANCO, 40, 350, 200)
    muestra_texto(pantalla, fuente, f"Score: {score}", BLANCO, 40, 400, 300)
    muestra_texto(pantalla, fuente, "Ingrese su nombre: ", BLANCO, 40, 300, 400)
    
    pygame.display.flip()
    
    name = ""
    input_activado = True
    while input_activado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    guardar_puntuacion(name, score, f"Murio, aguanto {tiempo_supervivencia} segundos.")
                    input_activado = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
        
        
        pantalla.fill(NEGRO)    
        muestra_texto(pantalla, fuente, "Game Over", (255, 0, 0), 50, 400, 100)
        muestra_texto(pantalla, fuente, f"Tiempo sobrevivido: {tiempo_supervivencia} segundos", BLANCO, 40, 350, 200)
        muestra_texto(pantalla, fuente, f"Score: {score}", BLANCO, 40, 400, 300)
        muestra_texto(pantalla, fuente, "Ingrese su nombre: ", BLANCO, 40, 300, 400)
        muestra_texto(pantalla, fuente, name, BLANCO, 40, 550, 400)
        
        pygame.display.flip()    
              
def win_screen(pantalla, fuente, score):
    """Muestra una pantalla blanca con un texto "Ganaste!", su puntuacion, y para ingresar su nombre, y guarda esta info en un archivo csv.

    Args:
        pantalla (_type_): Superficie a dibujar
        fuente (_type_): fuente a utilizar
        score (_type_): Puntuacion
    """
    pygame.mixer.music.pause()
    skyfall.play()
    pantalla.fill(BLANCO)
    
    muestra_texto(pantalla, fuente, "Ganaste!", (255, 220, 0), 50, 400, 100)
    muestra_texto(pantalla, fuente, f"Sobreviviste!", NEGRO, 40, 350, 200)
    muestra_texto(pantalla, fuente, f"Score: {score}", NEGRO, 40, 400, 300)
    muestra_texto(pantalla, fuente, "Ingrese su nombre: ", NEGRO, 40, 300, 400)
    
    pygame.display.flip()
    
    name = ""
    input_activado = True
    while input_activado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    guardar_puntuacion(name, score, "Ha ganado!")
                    input_activado = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
        
        pantalla.fill(BLANCO)
        muestra_texto(pantalla, fuente, "Ganaste!", (255, 220, 0), 50, 400, 100)
        muestra_texto(pantalla, fuente, f"Sobreviviste!", NEGRO, 40, 350, 200)
        muestra_texto(pantalla, fuente, f"Score: {score}", NEGRO, 40, 400, 300)
        muestra_texto(pantalla, fuente, "Ingrese su nombre: ", NEGRO, 40, 300, 400)
        muestra_texto(pantalla, fuente, name, NEGRO, 40, 550, 400)
        
        pygame.display.flip()          
            
    

        
        
        
        
        

