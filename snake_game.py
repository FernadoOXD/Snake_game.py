import turtle
import time
import random


posponer = 0.1

# marcadores
score = 0
high_score = 0

# Configuracion de la ventana
wn = turtle.Screen()
wn.title('juego de la culebrita')
wn.bgcolor('black')
wn.setup( width=600, height=600)
wn.tracer(0)

# cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.color('green')
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = 'stop'

# score
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write('score: 0       High Score: 0', align = 'center', font = ('courier', 24, 'normal'))

# Segmento / cuerpo de la serpiente
segmentos = []

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('red')
comida.penup()
comida.goto(50, 100)



# Funciones
def arriva():
    if cabeza.direction != 'down':
        cabeza.direction = 'up'

def abajo():
    if cabeza.direction != 'up':
        cabeza.direction = 'down'

def izquierda():
    if cabeza.direction != 'right': 
        cabeza.direction = 'left'

def derecha():
    if cabeza.direction != 'left':
        cabeza.direction = 'right'

def mov():
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)


 # Teclado
wn.listen()
wn.onkeypress(arriva, 'Up')
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')

def morir():
    time.sleep(1)
    cabeza.goto(0,0)
    cabeza.direction = "stop"
    [i.hideturtle() for i in segmentos]
    segmentos.clear()
    comida.goto(0,100)

while True:
    wn.update()

    # Colisiones con los bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        morir()

        # Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(10000, 10000)
        
        # limpiar lista de segmentos
        segmentos.clear()

        # Resetear los marcadores
        score = 0
        texto.clear()
        texto.write('score: {}       High Score: {}'.format(score, high_score), align = 'center', font = ('courier', 24, 'normal'))

            

    # colisiones de la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.color('green')
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        # Aumentear el marcador
        score += 10

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write('score: {}       High Score: {}'.format(score, high_score), align = 'center', font = ('courier', 24, 'normal'))
        


    totalseg = len(segmentos)
    for index in range(totalseg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalseg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)
        
    mov()

    # colisiones con el cuerpo
    for segmento in segmentos:   
      if segmento.distance(cabeza) < 20:
        morir()

        # Escoder los segmentos
        for segmento in segmentos:
              segmento.goto(10000, 10000)

        # limpiar los elementos de la lista
        segmentos.clear()
          

        score = 0
        texto.clear()
        texto.write('score: {}       High Score: {}'.format(score, high_score), align = 'center', font = ('courier', 24, 'normal'))
    time.sleep(posponer)