import pygame






#efectos disparos
pygame.mixer.init()
domain_expansion= pygame.mixer.Sound("assets/sounds/domain_expansion.wav")
todo_clap= pygame.mixer.Sound("assets/sounds/todo_clap_game_over.wav")
skyfall= pygame.mixer.Sound("assets/sounds/skyfall.wav")
bleach= pygame.mixer.Sound("assets/sounds/bleach.wav")

reversal_red= pygame.mixer.Sound("assets/sounds/reversal-red.wav")
lapse_blue= pygame.mixer.Sound("assets/sounds/lapse-blue.wav")
hollow_purple= pygame.mixer.Sound("assets/sounds/hollowpurple.wav")
hollow_purple_long= pygame.mixer.Sound("assets/sounds/hollowpurple_long.wav")

no_energy= pygame.mixer.Sound("assets/sounds/no_energysound.wav")
shoot_sound= pygame.mixer.Sound("assets/sounds/shoot_sound.wav")
blink_sound= pygame.mixer.Sound("assets/sounds/blink_sound.wav")
hit_sound= pygame.mixer.Sound("assets/sounds/hit_sound.wav")

scroll_open_sound= pygame.mixer.Sound("assets/sounds/scroll_open.wav")
play_sound= pygame.mixer.Sound("assets/sounds/play.wav")
play2_sound= pygame.mixer.Sound("assets/sounds/play2.wav")

pygame.mixer.music.load("assets/sounds/devils crush.wav")# se carga la musica
pygame.mixer.music.play(1) # se pone la musica
pygame.mixer.music.set_volume(0.2)