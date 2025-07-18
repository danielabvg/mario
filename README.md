# Mini Mario Bros

Mini Mario Bros es un sencillo juego de plataforma hecho en Python usando la librería **Pygame**. En este juego controlas a Mario para llegar a la meta evitando enemigos móviles. 

---

## Descripción

El juego presenta:

- Movimiento lateral (izquierda/derecha) de Mario con las flechas del teclado.
- Salto con la tecla espacio, con física básica de gravedad.
- Enemigos que se mueven de un lado a otro y causan que pierdas si los tocas.
- Una meta que debes alcanzar para ganar.
- Pantallas finales que indican si ganaste, perdiste o cerraste el juego.

---

## Requisitos

- Python 3.x
- Pygame (puedes instalarlo con `pip install pygame`)

---

## Archivos necesarios

- `mario.py` — el archivo principal del juego.
- Carpeta `imagenes/` que contenga:
  - `mario.png` (imagen de Mario)
  - `enemigo.png` (imagen del enemigo)
  - `meta.png` (imagen de la meta)
  - `piso.png` (imagen del piso)

Las imágenes deben tener el tamaño adecuado o serán redimensionadas automáticamente.

---

## Cómo jugar

1. Ejecuta el archivo `mario.py` con Python.
2. Usa las flechas izquierda y derecha para mover a Mario.
3. Presiona la barra espaciadora para saltar.
4. Evita tocar a los enemigos.
5. Llega hasta la meta para ganar.
6. Si tocas un enemigo, pierdes.

---

## Controles

- **Flecha Izquierda:** Mover a Mario hacia la izquierda
- **Flecha Derecha:** Mover a Mario hacia la derecha
- **Barra Espaciadora:** Saltar

---

## Funcionamiento interno (breve)

- Se controla el movimiento con velocidad fija y salto con velocidad vertical afectada por gravedad.
- Los enemigos se mueven automáticamente de izquierda a derecha y rebotan en los bordes.
- Las colisiones entre Mario y enemigos o la meta se detectan con rectángulos (`pygame.Rect`).
- El juego corre a 60 FPS con un bucle principal controlado por `pygame.time.Clock`.

---


¡Diviértete jugando y modificando tu propio Mini Mario Bros!

---

## Autor

Daniela Bravo

## Licencia

Este proyecto es de uso libre y abierto para fines educativos.

