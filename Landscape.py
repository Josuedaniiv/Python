import turtle

turtle.setup(width=800, height=600)
turtle.title("Dibujo de un paisaje")

# Cambiar el fondo de la ventana de la tortuga
turtle.bgcolor("#87ceeb")

turtle.penup()
turtle.goto(-400, -200)
turtle.pendown()

# Dibujar el suelo
turtle.color("green")
turtle.begin_fill()
turtle.forward(800)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(800)
turtle.end_fill()

# Dibujar el sol
turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# Dibujar la montaña
turtle.penup()
turtle.goto(-200, -100)
turtle.pendown()
turtle.color("#a9a9a9") 
turtle.begin_fill()
turtle.goto(0, 100)
turtle.goto(200, -100)
turtle.goto(-200, -100)
turtle.end_fill()

# Dibujar la casa
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.goto(100, 0)
turtle.goto(150, 50)
turtle.goto(200, 0)
turtle.goto(200, -100)
turtle.goto(100, -100)
turtle.end_fill()

# Dibujar la puerta
turtle.penup()
turtle.goto(120, -100)
turtle.pendown()
turtle.color("#8b4513") 
turtle.begin_fill()
turtle.goto(120, -50)
turtle.goto(180, -50)
turtle.goto(180, -100)
turtle.goto(120, -100)
turtle.end_fill()

# Dibujar la ventana
turtle.penup()
turtle.goto(150, -30)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.mainloop()