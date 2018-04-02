import pygame
import math

pygame.init()

j = pygame.joystick.Joystick(0)

j.init()
print 'Initialized Joystick : %s' % j.get_name()

def get():
    out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#1-> Primera rueda(RADIANEs)
#2-> Primera rueda(RADIANES)
#3-> LT
#4-> Segunda rueda(RADIANES)
#5-> Segunda rueda(RADIANES)
#6-> RT
#7-> A
#8-> B
#9-> X
#10-> Y
#11-> LB
#12-> RB
#13-> Back
#14-> Start
#15-> LOGITECH(Centro)
#16-> press primera Rueda
#17-> press segunda Rueda

    it = 0 #iterator
    pygame.event.pump()
    #Read input from the two joysticks    
    for i in range(0, j.get_numaxes()):
        #print it
        out[it] = j.get_axis(i)
        it+=1
    #Read input from buttons
    for i in range(0, j.get_numbuttons()):
        out[it] = j.get_button(i)
        it+=1
    return out

fuera = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def detectRueda(x,y,z):
	fuera = get()
	primerDato = fuera[x]
	segundoDato = fuera[y]
	print "El angulo de la "
	print z," es:"
#Mando en posicion NULA
	if(primerDato == 0 and segundoDato == 0):
		anguloR = 1000
		print anguloR
		angulo = 1000
#Divisiones entre 0
	elif(primerDato > 0 and segundoDato == 0):
		print 0
		angulo = 0
	elif(primerDato == 0 and segundoDato < 0):
		print 90
		angulo = 90
	elif(primerDato == 0 and segundoDato > 0):
		print 270
		angulo = 270
	elif(primerDato < 0 and segundoDato == 0):
		print 180
		angulo = 180
#Primer cuadrante
	elif(primerDato > 0 and segundoDato < 0):
		anguloR = math.atan(segundoDato/primerDato)
		angulo = math.degrees(anguloR)
		angulo = angulo * -1
		print angulo
#Segundo cuadrante
	elif(primerDato < 0 and segundoDato < 0):
		anguloR = math.atan(segundoDato/primerDato)
		angulo = math.degrees(anguloR)
		angulo = 180 - angulo
		print angulo
#Tercer cuadrante
	elif(primerDato < 0 and segundoDato > 0):
		anguloR = math.atan(segundoDato/primerDato)
		angulo = math.degrees(anguloR)
		angulo = angulo * -1
		angulo = angulo + 180
		print angulo
#Cuarto cuadrante
	elif(primerDato > 0 and segundoDato > 0):
		anguloR = math.atan(segundoDato/primerDato)
		angulo = math.degrees(anguloR)
		angulo = 360 - angulo
		print angulo
	return angulo

while True:
	primeraRueda = detectRueda(0,1,1)
	segundaRueda = detectRueda(3,4,2)
	archivo = open("comandos.txt","a+")
	primerElemento = str(primeraRueda)
	segundoElemento = str(segundaRueda)
	archivo.write(primerElemento)
	archivo.write("  "+segundoElemento)
	archivo.write("\n")
	archivo.close()

