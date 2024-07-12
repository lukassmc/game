import pygame
from functions import *
from buttons import *
from settings import PANTALLA

def paused_overlay():
    main_font = pygame.font.Font("assets/fonts/Jujutsu-Kaisen.ttf", 50)
    paused_text = main_font.render("Game Paused", True, NEGRO)
    continue_text = main_font.render('Press "P" to continue.', True, NEGRO)
    
    
    paused = True
    while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False
            
            
            PANTALLA.fill(NAVY_BLUE)
            PANTALLA.blit(paused_text, (500, 150))
            PANTALLA.blit(continue_text, (430, 250))
            
            
            
            pygame.display.flip()
    