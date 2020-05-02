import pygame, sys
from  pygame.locals import *

import random
import math
import time 



def tiempoEnQueSeDesocupaLaEstacion(estacion):
    return estacion[1]


t_minimo = int(raw_input("TIEMPO MINIMO EN CORTE:    "))
t_maximo = int(raw_input("TIEMPO MAXIMO EN CORTE:    "))
t_entre_llegada = int(raw_input("TIEMPO ENTRE LLEGADA:    "))
total_de_clientes = int(raw_input("TOTAL DE CLIENTES:     "))
barbeross = int(raw_input("NO. DE BARBERROS:    "))

t_llegada_total = 0
t_salida_anterior = 0
espera_total_1 = 0
t_corte_1 = 0

tiempo_llegada = []
tiempo_corte = []
cli = []
sali = []
espe = []
tiempo_llegada_entero = []
sali_entero = []

estaciones = []
barbero = []
birbero = []
for e in range(0, barbeross):
    estaciones.append([e+1, 0])

for i in range(total_de_clientes):
	R = random.random()
	t_llegada = abs((((-1)*(t_entre_llegada))*((math.log(R)))))
	t_llegada_total = t_llegada + t_llegada_total 
	tiempo_llegada.append(t_llegada_total) 
	tiempo_llegada_entero.append(int(t_llegada_total))
	t_corte = ((t_minimo + ((t_maximo - t_minimo) * (R)))) 
	tiempo_corte.append(t_corte)
	cli.append(i) 
	t_salida = t_llegada_total + t_corte 
	sali.append(t_salida)
	sali_entero.append(int(t_salida))
	espera_total = (t_salida_anterior - t_llegada_total)
	estaciones.sort(key=tiempoEnQueSeDesocupaLaEstacion)
	
	espera_total = estaciones[0][1] - t_llegada_total
	espe.append(espera_total)
	
	if espera_total < 0:
		espera_total = 0
	t_salida += espera_total
	estaciones[0][1] = t_salida

	barbero.append([i+1, t_llegada_total, t_salida, estaciones[0][0], espera_total])

	
	t_salida_anterior = t_salida
	
	espera_total_1 = espera_total + espera_total_1
	t_corte_1 = (t_corte) + (t_corte_1)
	


sep = '|{}|{}|{}|{}|{}|'.format('-'*10, '-'*16, '-'*16, '-'*16, '-'*16)
print('{0}\n| CLIENTE  |    LLEGADA     |   SALIDA       |     BARBERO    |     ESPERA     |\n{0}'.format(sep))
for b in barbero:
	n_cliente = b[0]
	t_llegada = b[1]
	tiempo = b[2]
	barb = b[3]
	espera = b[4]
	print('| {:>8.2f} | {:>14.2f} | {:>14.2f} | {:>14.2f} | {:>14.2f} |'.format(n_cliente, t_llegada,tiempo,barb, espera,sep))
	birbero.append(barb)


estaciones.sort(key=tiempoEnQueSeDesocupaLaEstacion)
t_salida_ultimo = estaciones[-1][1]
n_estaciones_ocupadas = 0
n_clientes_en_espera = 0

long_de_fila = (espera_total_1) / (t_salida_anterior) 
t_espera_promedio = (espera_total_1) / (total_de_clientes)
uso_instalacion = (t_corte_1) / (t_salida_anterior) 

print ("LONGITUD PROMEDIO DE FILA   %.2f" %(long_de_fila))
print ("TIEMPO DE ESPERA PROMEDIO     %.2f" %(t_espera_promedio))
print ("USO PROMEDIO DE LA INSTALACION      %.2f" %(uso_instalacion))



pygame.init()

FPS = 5
fpsClock = pygame.time.Clock()


screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('LA MAMALONA')

imageImg  = pygame.image.load("fondo.png")
barbero1  = pygame.image.load('barbero.png')
barbero2  = pygame.image.load('barbero.png')
cliente  = pygame.image.load('cliente.png')
clientes_en_pantalla = []
t=1
fps_contador = 0
posy = 100
# the main game loop
while True:
   
	if t == int(t_salida_anterior):
		pygame.quit()
        	sys.exit()

	screen.fill((0,0,0))
    	screen.blit(imageImg, (0, 0))
	screen.blit(barbero1, (50, 50))  #105 X 140
	screen.blit(barbero1, (200, 50))

	# mostrar clientes en pantalla
	for c in clientes_en_pantalla:
		if c[5] == True:
			screen.blit(cliente, (c[1], c[2]))

			if c[3] == 1:
				limite = 75

			else:
				limite = 200

			if c[1] < limite and c[4] <= 0:
				c[1]+= 10
				c[4]-= 1

	fps_contador += 1
	if fps_contador == 5:
		print ("LOS SEGUNDOS SON:" , t)
		for b in barbero:
			if int (b[1]) == t:
			    clientes_en_pantalla.append([b[0], 0, posy, b[3], b[4], True])
			    posy += 15
			    if n_estaciones_ocupadas < barbeross:#cambiar n_estaciones por barberos 
				n_estaciones_ocupadas += 1

			    if b[4] > 0:
				n_clientes_en_espera += 1

			elif int(b[2]) == t:
			    for c in clientes_en_pantalla:
				if c[0] == b[0]:
					c[5] = False

			    if n_estaciones_ocupadas > 0 and n_clientes_en_espera == 0:
				n_estaciones_ocupadas -= 1

			    if n_clientes_en_espera > 0:
				n_clientes_en_espera -= 1

		t += 1
		fps_contador = 0

	for event in pygame.event.get():
    		if event.type == QUIT:
        		pygame.quit()
        		sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)
