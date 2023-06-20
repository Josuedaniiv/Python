import turtle
import random

def dibuja_arbol(longitud, disminucion, angulo, ruido=0):
    if longitud < 10:
        return
    turtle.width(longitud/15)
    turtle.forward(longitud)
    cambio_longitud = longitud*disminucion
    if ruido:
        cambio_longitud *= random.gauss(0, ruido)

    angulo_derecho = angulo + random.gauss(0, ruido)
    angulo_izquierdo = angulo + random.gauss(0, ruido)

    turtle.left(angulo_izquierdo)
    dibuja_arbol(cambio_longitud, disminucion, angulo, ruido)
    turtle.right(angulo_izquierdo)

    turtle.right(angulo_derecho)
    dibuja_arbol(cambio_longitud, disminucion, angulo, ruido)
    turtle.left(angulo_derecho)

    turtle.backward(longitud)

turtle.setup(width=1200, height=800)
turtle.title("Árbol fractal")

turtle.penup()
turtle.goto(0, -300)
turtle.left(90)
turtle.pendown()

dibuja_arbol(200, 0.75, 0, 10)

turtle.mainloop()