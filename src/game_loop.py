import pygame
import time
import random
from classes import *
from settings import *
from sprites import *
from functions import *
from sounds import *
from paused import paused_overlay

def reset_game_state():
    """Resetea todos los elementos del juego.
    """
    global player, puertas, enemigos, balas, fondo, tiempo_inicial, tiempo_final, tiempos_creacion1, tiempos_creacion2, tiempos_creacion3, enemigos_creados, puerta1, puerta2, puerta3, score, last_score_time
    
    px, py = 65, 490
    player = Player((px, py))
    enemigos = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    
    puerta1 = Puerta((0, 24))
    puerta2 = Puerta((0, 249))
    puerta3 = Puerta((0, 465)) 
    puerta1.vida = 100
    puerta2.vida = 100
    puerta3.vida = 100
   
    puertas = pygame.sprite.Group()
    puertas.add(puerta1, puerta2, puerta3)
    
    # Fondo del juego
    fondo = pygame.image.load("assets/imagenes/fondolvl1.png").convert()
    
    # Tiempo
    duracion = 120
    tiempo_inicial = time.time()
    tiempo_final = tiempo_inicial + duracion
    
    # Creación de enemigos
    cantidad_enemigos =60
    tiempos_creacion1 = [random.randrange(int(tiempo_final - time.time())) for _ in range(cantidad_enemigos)]
    tiempos_creacion2 = [random.randrange(int(tiempo_final - time.time())) for _ in range(cantidad_enemigos)]
    tiempos_creacion3 = [random.randrange(int(tiempo_final - time.time())) for _ in range(cantidad_enemigos)]
    enemigos_creados = set()
    
    
    score= 0
    last_score_time= tiempo_inicial


def game_loop():
    """Bucle principal del juego.
    """
    pygame.init() 
    pygame.display.set_caption("Cursed Doors")
    reset_game_state()  
    
    
    
    # Fondo del juego
    fondo = pygame.image.load("assets/imagenes/fondolvl1.png")
    pygame.mixer.music.play()
    PANTALLA.blit(fondo, (0, 0))
    # Fuente del juego
    font = "assets/fonts/Jujutsu-Kaisen.ttf"
    
    
    
    score= 0
    last_score_time= tiempo_inicial

    # Bucle del juego
    flag_paused = False
    game_over = False
    music_muted= False
    while not game_over:
        clock.tick(60)
        
        PANTALLA.blit(fondo, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    flag_paused = True
                    pygame.mixer.music.pause()
                    paused_overlay()
                    flag_paused = False
                    pygame.mixer.music.play()
                if event.key == pygame.K_8:
                    pygame.mixer.music.set_volume(0)
                    music_muted= True
                if event.key == pygame.K_9:
                    pygame.mixer.music.set_volume(0.2)
                    music_muted= False
                    
                    
                if event.key == pygame.K_m:
                    player.disparar(balas, "bala")
                if event.key == pygame.K_l:
                    if player.current_cursed_energy == 100:
                        player.disparar(balas, "Violeta")
                    else:
                        no_energy.play()
                        muestra_avisos(PANTALLA, None, "No tienes energia suficiente.", (0, 180, 255), 30, 1090, 70, 5)
                if event.key == pygame.K_j:
                    if player.current_cursed_energy >= 30:
                        player.disparar(balas, "Rojo")
                    else:
                        no_energy.play()
                        muestra_avisos(PANTALLA, None, "No tienes energia suficiente.", (0, 180, 255), 30, 1090, 70, 5)
                if event.key == pygame.K_k:
                    if player.current_cursed_energy >= 60:
                        player.disparar(balas, "Azul")
                    else:
                        no_energy.play()
                        muestra_avisos(PANTALLA, None, "No tienes energia suficiente.", (0, 180, 255), 30, 1090, 70, 5)
        
        if not flag_paused:
            if time.time() - last_score_time >= 5:
                score += 10
                last_score_time= time.time()
            barra_hp(PANTALLA, 0, 3, puerta1.vida)
            barra_hp(PANTALLA, 0, 220, puerta2.vida)
            barra_hp(PANTALLA, 0, 443, puerta3.vida)
            
            cursed_energy_bar(PANTALLA, 900, 0, player.current_cursed_energy, player.max_cursed_energy)
            
            tiempo_restante = mostrar_tiempo_restante(PANTALLA, font, NEGRO, 50, 600, 0 + 20, tiempo_final)
            
            muestra_texto(PANTALLA,font, "Cursed Energy", NEGRO, 26, 1000, 10)
            
            if music_muted:
                texto= "Music: Muted"
            else:
                texto= "Music: On"    
            
            muestra_texto(PANTALLA, font, texto, NEGRO, 25, 60, 680)
            
            mostrar_puntuacion(PANTALLA, font, NEGRO, 30, 1150, 13, score)
            
            crear_enemigos_random(tiempo_final, enemigos, posicion_plataforma1, tiempos_creacion1, enemigos_creados)
            crear_enemigos_random(tiempo_final, enemigos, posicion_plataforma2, tiempos_creacion2, enemigos_creados)
            crear_enemigos_random(tiempo_final, enemigos, posicion_plataforma3, tiempos_creacion3, enemigos_creados)
            
            colision = pygame.sprite.groupcollide(enemigos, balas, False, False)
            colision_puerta = pygame.sprite.groupcollide(puertas, enemigos, False, False)
            
            for enemigo, balas_impactadas in colision.items():
                for bala in balas_impactadas:
                    enemigo.recibir_dmg(bala.damage)
                    hit_sound.play()
                    if bala.type != "Violeta":
                        bala.kill()
                    if enemigo.vida <= 0:
                        score += 5
                        enemigo.muriendo = True
                        player.current_cursed_energy += 12.5
                        if player.current_cursed_energy > player.max_cursed_energy:
                            player.current_cursed_energy = player.max_cursed_energy
                barra_hp_enemigos(PANTALLA, enemigo.rect.x, enemigo.rect.y, enemigo.vida)
            
            for puerta in colision_puerta:
                for enemigo in colision_puerta[puerta]:
                    puerta.recibir_dmg(0.10)
                    
                    
                if puerta.vida <= 0:
                    todo_clap.play()
                    tiempo_supervivencia= int(time.time()- tiempo_inicial)
                    game_over_screen(PANTALLA, font, score, tiempo_supervivencia)
                    game_over = True
                    reset_game_state()
            
            if tiempo_restante <= 0:
                win_screen(PANTALLA, font, score)
                game_over = True
            
            enemigos.update()
            player.update()
            puertas.update()
            balas.update()
            
            puertas.draw(PANTALLA)
            enemigos.draw(PANTALLA)
            balas.draw(PANTALLA)
            player.animar()
        
        pygame.display.flip()
    
    pygame.mixer_music.pause()