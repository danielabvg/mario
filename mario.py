import pygame
import sys

# Iniciar Pygame
pygame.init()

# Tamaño de la ventana del juego
ANCHO = 800
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Mario Bros")

# Color que se va a usar
BLANCO = (255, 255, 255)

# Cargar imágenes y ajustarlas a tamaño
mario_img = pygame.image.load("imagenes/mario.png")  # Imagen de Mario
mario_img = pygame.transform.scale(mario_img, (55, 70))  # Ajuste de tamaño

enemigo_img = pygame.image.load("imagenes/enemigo.png")  # Imagen del enemigo
enemigo_img = pygame.transform.scale(enemigo_img, (40, 40))  # Ajuste de tamaño

meta_img = pygame.image.load("imagenes/meta.png")  # Imagen de la meta
meta_img = pygame.transform.scale(meta_img, (60, 90))  # Ajuste del tamaño

piso_img = pygame.image.load("imagenes/piso.png")  # Imagen del piso
piso_img = pygame.transform.scale(piso_img, (ANCHO, 50))  # A lo largo de toda la pantalla

# Posiciones iniciales de Mario y la meta
mario_x = 50  # Posición horizontal de Mario (inicio a la izquierda)
mario_y = ALTO - 110  # Posición vertical de Mario (sobre el piso)

meta_x = 700  # La meta está a la derecha
meta_y = ALTO - 140  # Un poco más arriba del suelo para que no esté pegada

# Enemigos: posición inicial y velocidad (uno va a la derecha, otro a la izquierda)
enemigos = [
    {"x": 400, "y": ALTO - 90, "vel": 2},
    {"x": 600, "y": ALTO - 90, "vel": -2}
]

# Velocidad de movimiento lateral de Mario
velocidad = 5 # pixeles

# 🕴 Variables del salto
vel_y = 0          # Velocidad salto (empieza en 0)
gravedad = 1       # Hace que Mario caiga
en_el_suelo = True # Para que no pueda saltar en el aire

# Reloj para controlar los FPS (frames por segundo)
reloj = pygame.time.Clock() # controla que juego corra a 60 cuadros por segundo

# Variables de los Estados del juego
jugando = True     # Mientras sea True, el juego corre
ganaste = False    # Se activa si Mario toca la meta
perdiste = False   # Se activa si Mario toca un enemigo

# Bucle principal del juego
while jugando:
    reloj.tick(60)  # El bucle se repite máx 60 veces por segundo
    
    pantalla.fill((135, 206, 235))  # Color azul cielo de fondo

    # Eventos ( cerrar la ventana)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Detecta si se están presionando teclas 
    teclas = pygame.key.get_pressed()

    # Mover a la izquierda
    if teclas[pygame.K_LEFT]:
        mario_x -= velocidad
    # ➡ Mover a la derecha
    if teclas[pygame.K_RIGHT]:
        mario_x += velocidad

    # Saltar (solo si está en el suelo)
    if teclas[pygame.K_SPACE] and en_el_suelo:
        vel_y = -15      # Valor negativo para subir
        en_el_suelo = False  # Ya no está tocando el suelo

    # Aplicar la gravedad (caída)
    mario_y += vel_y      # Mario sube o baja dependiendo de vel_y
    vel_y += gravedad     # La gravedad hace que vuelva a caer

    # Verificar si Mario ya tocó el suelo
    if mario_y >= ALTO - 110:
        mario_y = ALTO - 110  # Que no pase el piso
        vel_y = 0             # Detener caída
        en_el_suelo = True    # Está en el suelo

    # Limitar a Mario dentro de la pantalla
    if mario_x < 0:
        mario_x = 0
    if mario_x > ANCHO - 40:
        mario_x = ANCHO - 40

    # Pegar elementos visuales
    pantalla.blit(piso_img, (0, ALTO - 50))           # Piso
    pantalla.blit(meta_img, (meta_x, meta_y))         # Meta
    pantalla.blit(mario_img, (mario_x, mario_y))      # Mario

    # Mover y pegar enemigos
    for enemigo in enemigos:
        enemigo["x"] += enemigo["vel"]  # Se mueven a izquierda o derecha
        if enemigo["x"] <= 0 or enemigo["x"] >= ANCHO - 40:
            enemigo["vel"] *= -1        # Rebotan al llegar al borde
        pantalla.blit(enemigo_img, (enemigo["x"], enemigo["y"]))  # Se dibujan

    # Crear rectángulos para detectar choques con enemigos
    mario_rect = pygame.Rect(mario_x, mario_y, 55, 70)

    # Si choca con un enemigo, pierdes
    for enemigo in enemigos:
        enemigo_rect = pygame.Rect(enemigo["x"], enemigo["y"], 40, 40)
        if mario_rect.colliderect(enemigo_rect):
            perdiste = True
            jugando = False

    # Si toca la meta, ganas
    meta_rect = pygame.Rect(meta_x, meta_y, 60, 90)
    if mario_rect.colliderect(meta_rect):
        ganaste = True
        jugando = False

    # Actualizar la pantalla
    pygame.display.update()

# Pantalla final según si ganaste o perdiste
pantalla.fill(BLANCO)
fuente = pygame.font.SysFont("Arial", 40)

if ganaste:
    mensaje = fuente.render("¡Ganaste!", True, (0, 200, 0))  # Verde
elif perdiste:
    mensaje = fuente.render("¡Perdiste!", True, (200, 0, 0))  # Rojo
else:
    mensaje = fuente.render("Juego cerrado", True, (0, 0, 0))  # Negro

pantalla.blit(mensaje, (ANCHO // 2 - mensaje.get_width() // 2, ALTO // 2))  # Centrar texto
pygame.display.update()
pygame.time.wait(3000)  # Espera 3 segundos

# Cerrar el juego completamente
pygame.quit()
sys.exit()
