

import pygame
from pygame.locals import *
import sys
import math



WIDTH = 640
HEIGHT = 480

G = int(input("INTRODUZCA LA GRAVEDAD"))
R = int(input("INTRODUZCA LA MASA DEL PROYECTIL(2-15)"))



class Proyectil(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        self.angulo = 45
        self.veloc = 50
        self.tiempo = 0
        self.x = x
        self.y = y
        self.disparar = False
        self.xreal = x
        self.yreal = HEIGHT - self.y

    def update(self):
        self.velocx = self.veloc * math.cos(math.radians(self.angulo))
        self.velocy = self.veloc * math.sin(math.radians(self.angulo))

        if self.disparar == True:
            self.xreal = (0 + self.velocx * self.tiempo)
            self.yreal = (0 + self.velocy * self.tiempo +
                ((-G )* (self.tiempo ** 2)) / 2)
            self.x = self.xreal
            self.y = HEIGHT - self.yreal
        else:
            pass

        if (self.y > HEIGHT) or (self.x > WIDTH):
            self.x = 0
            self.y = HEIGHT
            self.tiempo = 0
            self.disparar = False




def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SIMULACION PROYECTIl JUAN EDUARTE")
    background = pygame.image.load("FIN.png")
    Blanco = pygame.image.load('blanco.png')
    PX = 70
    PY = 620

    fuente = pygame.font.Font(None, 20)

    bala = Proyectil(0, HEIGHT)

    pygame.key.set_repeat(1, 80)
    clock = pygame.time.Clock()

    while True:
        tick = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    PX = PX - 1
                elif event.key == K_d:
                    PX = PX + 1
                if event.key == K_UP:
                    if bala.angulo < 90 and bala.disparar == False:
                        bala.angulo = bala.angulo + 1
                elif event.key == K_DOWN:
                    if bala.angulo > 0 and bala.disparar == False:
                        bala.angulo = bala.angulo - 1
                elif event.key == K_RIGHT:
                    if bala.veloc < 100 and bala.disparar == False:
                        bala.veloc = bala.veloc + 1
                elif event.key == K_LEFT:
                    if bala.veloc > 10 and bala.disparar == False:
                        bala.veloc = bala.veloc - 1
                elif event.key == K_SPACE:
                    bala.disparar = True
                elif event.key == K_ESCAPE:
                    sys.exit()

        if bala.disparar == True:
            bala.tiempo = bala.tiempo + (tick / 1000.0)

        bala.update()
        text = "Velocidad: %3d (m/s)   Angulo: %d   x=%d m   y=%d m" % (
            bala.veloc, bala.angulo, bala.xreal, bala.yreal)
        mensaje = fuente.render(text, 1, (255, 255, 255))

        screen.blit(Blanco, (PX,PY))       
        screen.blit(background, (0, 0))
        screen.blit(mensaje, (15, 5))
        pygame.draw.line(screen, (255, 255, 255), (0, 25), (640, 25), 2)
        pygame.draw.circle(screen, (0, 0, 0), (int(bala.x), int(bala.y)), R)
        pygame.draw.circle(screen, (203, 50, 52),((PX),(PY)),20)

        pygame.display.flip()


if __name__ == "__main__":
    main()
