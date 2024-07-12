import pygame
from buttons import *
from game_loop import game_loop
from functions import *
from settings import PANTALLA
pygame.init()

PANTALLA= pygame.display.set_mode((1240, 700))

def menu():
    pygame.mixer.music.pause()
    
    fondo_menu= pygame.image.load("assets/imagenes/bacckground.png").convert()
    logo= pygame.image.load("assets/imagenes/cursed-doors-logo.png")
    main_font= pygame.font.Font("assets/fonts/Jujutsu-Kaisen.ttf", 50)
    
    opacity_layer= pygame.image.load("assets/imagenes/button_images/opacity_layer.png")
    controls= pygame.image.load("assets/imagenes/scrolls_info.png")
    
    pygame.display.set_caption("Cursed Doors")
    
    mostrar_boton_flag= False
    
    running= True
    while running:
        PANTALLA.blit(fondo_menu, (0,0))
        PANTALLA.blit(logo,(350, 0))
        mouse_posicion= pygame.mouse.get_pos()
        
        menu_text= main_font.render("Main menu", True, (43, 0, 9))
        
        
        boton_play= Button(pygame.image.load("assets/imagenes/button_images/play_rect.png"), (600, 300), "Play", main_font,(43, 0, 9), (0,0,0))
        boton_controls= Button(pygame.image.load("assets/imagenes/button_images/options_rect.png"), (600, 400), "Controls", main_font,(43, 0, 9), (0,0,0))
        boton_quit= Button(pygame.image.load("assets/imagenes/button_images/quit_rect.png"), (600, 500), "Quit", main_font,(43, 0, 9), (0,0,0))
        boton_close= Button(pygame.image.load("assets/imagenes/button_images/close_rect.png"), (880, 110), "Close", main_font, (43, 0, 9), (0, 0, 0))
        
        PANTALLA.blit(menu_text, (500, 150))
        
        for boton in [boton_play, boton_controls, boton_quit]:
            boton.cambiar_color(mouse_posicion)
            boton.update(PANTALLA)
        
        if mostrar_boton_flag:
            
            PANTALLA.blit(opacity_layer, (0,0))
            PANTALLA.blit(controls, (350, 25))
            boton_close.cambiar_color(mouse_posicion)
            boton_close.update(PANTALLA)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running= False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_play.check_apretar(mouse_posicion):
                    domain_expansion.play()
                    game_loop()
                if boton_controls.check_apretar(mouse_posicion):
                    scroll_open_sound.play()
                    mostrar_boton_flag= True
                if mostrar_boton_flag and boton_close.check_apretar(mouse_posicion):
                    mostrar_boton_flag= False
                if boton_quit.check_apretar(mouse_posicion):
                    running= False
        
        pygame.display.flip()
    pygame.quit()
        
  
    
    
    
    