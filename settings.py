WIDTH= 1240
HEIGHT= 700
SCREEN_SIZE= (WIDTH, HEIGHT)
SCREEN_CENTER= (WIDTH//2, HEIGHT//2)


#COLORES
COLORES = [(255, 0, 0),       # Rojo
    (255, 20, 0),      # Rojo brillante
    (255, 40, 0),      # Rojo intenso
    (255, 60, 0),      # Rojo anaranjado
    (255, 80, 0),      # Naranja rojizo
    (255, 100, 0),     # Naranja oscuro
    (255, 120, 0),     # Naranja
    (255, 140, 0),     # Naranja claro
    (255, 160, 0),     # Amarillo anaranjado
    (255, 180, 0),     # Amarillo oscuro
    (255, 200, 0),     # Amarillo
    (255, 220, 0),     # Amarillo brillante
    (255, 240, 0),     # Amarillo claro
    (240, 255, 0),     # Verde amarillo claro
    (220, 255, 0),     # Verde amarillo
    (200, 255, 0),     # Verde lima claro
    (180, 255, 0),     # Verde lima
    (160, 255, 0),     # Verde lima oscuro
    (140, 255, 0),     # Verde claro
    (120, 255, 0),     # Verde brillante
    (100, 255, 0),     # Verde
    (80, 255, 0),      # Verde oscuro
    (60, 255, 0),      # Verde esmeralda
    (40, 255, 0),      # Verde bosque
    (20, 255, 0),      # Verde oscuro intenso
    (0, 255, 0),       # Verde puro
    (0, 255, 20),      # Verde azulado claro
    (0, 255, 40),      # Verde azulado
    (0, 255, 60),      # Verde marino claro
    (0, 255, 80),      # Verde marino
    (0, 255, 100),     # Cian claro
    (0, 255, 120),     # Cian
    (0, 255, 140),     # Cian oscuro
    (0, 255, 160),     # Azul claro
    (0, 255, 180),     # Azul brillante
    (0, 255, 200),     # Azul
    (0, 255, 220),     # Azul oscuro
    (0, 255, 240),     # Azul intenso
    (0, 240, 255),     # Índigo claro
    (0, 220, 255),     # Índigo
    (0, 200, 255),     # Índigo oscuro
    (0, 180, 255),     # Violeta claro
    (0, 160, 255),     # Violeta
    (0, 140, 255),     # Violeta oscuro
    (0, 120, 255),     # Magenta claro
    (0, 100, 255),     # Magenta
    (0, 80, 255),      # Magenta oscuro
    (0, 60, 255),      # Rosa claro
    (0, 40, 255),      # Rosa
    (0, 20, 255),      # Rosa oscuro
    (0, 0, 255),       # Azul puro
    (20, 0, 255),      # Azul intenso
    (40, 0, 255),      # Azul oscuro
    (60, 0, 255),      # Índigo claro
    (80, 0, 255),      # Índigo
    (100, 0, 255),     # Índigo oscuro
    (120, 0, 255),     # Violeta claro
    (140, 0, 255),     # Violeta
    (160, 0, 255),     # Violeta oscuro
    (180, 0, 255),     # Magenta claro
    (200, 0, 255),     # Magenta
    (220, 0, 255),     # Magenta oscuro
    (240, 0, 255),     # Rosa claro
    (255, 0, 255),     # Rosa
    (255, 0, 240),     # Rosa oscuro
    (255, 0, 220),     # Rojo-rosa claro
    (255, 0, 200),     # Rojo-rosa
    (255, 0, 180),     # Rojo-rosa oscuro
    (255, 0, 160),     # Rojo intenso claro
    (255, 0, 140),     # Rojo intenso
    (255, 0, 120),     # Rojo intenso oscuro
    (255, 0, 100),     # Rojo oscuro
    (255, 0, 80),      # Rojo anaranjado
    (255, 0, 60),      # Naranja rojizo
    (255, 0, 40),      # Naranja oscuro
    (255, 0, 20),      # Naranja
    (255, 0, 0)        # Rojo
    
]

BLANCO = (255, 255, 255)
NEGRO= (0,0,0)
ROJO= (255, 0, 0)
VERDE= (0, 255, 0)
AZUL= (0,0, 255)

CARMESI= 	(165, 28, 48)

#contadores y variables necesarias
x= 0
px= 50
py= 200
ancho= 40
velocidad= 10
    
indice_imagen= 0    
contador_quieto= 0
cuentasalto= 10 #contador saltar
cuentapasos= 0 #contador pasos

#banderas  
salto= False
izquierda= False
derecha= False

PLATAFORMA_3Y= 155
PLATAFORMA_2Y= 379
PLATAFORMA_1Y= 594
  
