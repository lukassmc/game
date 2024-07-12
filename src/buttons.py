import pygame
class Button():
    def __init__(self, image, pos, texto, fuente, base_color, hovering_color):
        self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.fuente = fuente
        self.base_color, self.hovering_color = base_color, hovering_color
        self.texto = texto
        self.text = self.fuente.render(self.texto, True, self.base_color)
  
        if self.image is None:
            self.image = self.text
   
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
            
        screen.blit(self.text, self.text_rect)
        pygame.draw.rect(screen, self.base_color, self.rect, 3)  

    def check_apretar(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            retorno=True
        else:
            retorno= False
        return retorno

    def cambiar_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.fuente.render(self.texto, True, self.hovering_color)
        else:
            self.text = self.fuente.render(self.texto, True, self.base_color)
