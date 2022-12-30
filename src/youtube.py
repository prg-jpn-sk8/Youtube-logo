from turtle import *

title("Youtube")

hideturtle()

pencolor("red")

penup()
goto(-200, -150)
pendown()
begin_fill()
for x in range(2):
    fillcolor("red")
    fd(400)
    circle(100, 90)
    fd(200)
    circle(100, 90)
end_fill()

pencolor("white")

penup()
goto(-30, 0)
pendown()
begin_fill()
right(90)
for i in range(3):
    fillcolor("white")
    fd(-100)
    right(120)
end_fill()

pencolor("black")

penup()
goto(-185, -285)
pendown()

write("Youtube", font=("Verdana", 70))

done()