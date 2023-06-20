import turtle

turtle.setup(width=800, height=600)
turtle.title("Dibujo de una luna")

turtle.bgcolor("black")

turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()

turtle.color("white")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.color("black")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

turtle.mainloop()