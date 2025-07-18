import pygame
import sys

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana del juego
ANCHO = 800
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Mario Bros 💗")

# Colores por si los necesitas
BLANCO = (255, 255, 255)

# Cargar imágenes y ajustar tamaños
fondo = pygame.image.load("imagenes/fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

mario_img = pygame.image.load("imagenes/mario.png")
mario_img = pygame.transform.scale(mario_img, (40, 50))

enemigo_img = pygame.image.load("imagenes/enemigo.png")
enemigo_img = pygame.transform.scale(enemigo_img, (40, 40))

meta_img = pygame.image.load("imagenes/meta.png")
meta_img = pygame.transform.scale(meta_img, (60, 90))  

piso_img = pygame.image.load("imagenes/piso.png")
piso_img = pygame.transform.scale(piso_img, (ANCHO, 50))

# Posiciones iniciales
mario_x = 50
mario_y = ALTO - 100  # Justo sobre el piso

meta_x = 700
meta_y = ALTO - 140  # Se ajusta por la nueva altura

# Enemigos
enemigos = [
    {"x": 400, "y": ALTO - 90, "vel": 2},
    {"x": 600, "y": ALTO - 90, "vel": -2}
]

# Velocidades
velocidad = 5

# Variables para salto
vel_y = 0          # Velocidad vertical
gravedad = 1       # Fuerza de gravedad
en_el_suelo = True # Verifica si Mario está tocando el suelo

# Reloj para los FPS
reloj = pygame.time.Clock()

# Estados del juego
jugando = True
ganaste = False
perdiste = False

# Bucle principal
while jugando:
    reloj.tick(60)  # Limita a 60 FPS
    #pantalla.blit(fondo, (0, 0))  # Dibuja el fondo
    pantalla.fill((135, 206, 235))  # Azul claro


    # Eventos (como cerrar la ventana)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Teclas presionadas
    teclas = pygame.key.get_pressed()

    # Movimiento lateral
    if teclas[pygame.K_LEFT]:
        mario_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        mario_x += velocidad

    # Salto con espacio (solo si está en el suelo)
    if teclas[pygame.K_SPACE] and en_el_suelo:
        vel_y = -15  # Fuerza del salto
        en_el_suelo = False

    # Aplicar gravedad
    mario_y += vel_y
    vel_y += gravedad

    # Verificar si Mario cae al suelo
    if mario_y >= ALTO - 100:
        mario_y = ALTO - 100
        vel_y = 0
        en_el_suelo = True

    # Limitar a los bordes
    if mario_x < 0:
        mario_x = 0
    if mario_x > ANCHO - 40:
        mario_x = ANCHO - 40

    # Dibujar piso, meta, jugador y enemigos
    pantalla.blit(piso_img, (0, ALTO - 50))
    pantalla.blit(meta_img, (meta_x, meta_y))
    pantalla.blit(mario_img, (mario_x, mario_y))

    # Mover y dibujar enemigos
    for enemigo in enemigos:
        enemigo["x"] += enemigo["vel"]
        if enemigo["x"] <= 0 or enemigo["x"] >= ANCHO - 40:
            enemigo["vel"] *= -1
        pantalla.blit(enemigo_img, (enemigo["x"], enemigo["y"]))

    # Rectángulos para detectar colisiones
    mario_rect = pygame.Rect(mario_x, mario_y, 40, 50)

    # Colisión con enemigos = pierdes
    for enemigo in enemigos:
        enemigo_rect = pygame.Rect(enemigo["x"], enemigo["y"], 40, 40)
        if mario_rect.colliderect(enemigo_rect):
            perdiste = True
            jugando = False

    # Colisión con la meta = ganas
    meta_rect = pygame.Rect(meta_x, meta_y, 60, 90)
    if mario_rect.colliderect(meta_rect):
        ganaste = True
        jugando = False

    # Actualiza pantalla
    pygame.display.update()

# Pantalla final (ganaste o perdiste)
pantalla.fill(BLANCO)
fuente = pygame.font.SysFont("Arial", 40)

if ganaste:
    mensaje = fuente.render("¡Ganaste!", True, (0, 200, 0))
elif perdiste:
    mensaje = fuente.render("¡Perdiste!", True, (200, 0, 0))
else:
    mensaje = fuente.render("Juego cerrado", True, (0, 0, 0))

pantalla.blit(mensaje, (ANCHO // 2 - mensaje.get_width() // 2, ALTO // 2))
pygame.display.update()
pygame.time.wait(3000)

# Cierra el juego
pygame.quit()
sys.exit()
