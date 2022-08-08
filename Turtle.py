# Michelle Patlan
# 8/6/2022
#create a polygon with turtle
from turtle import Screen, Turtle

#ask questions
sides = int(input("Number of sides in polygon?"))
length = int(input("Length of the sides in polygon?"))
colorname = input("Color of polygon?")
fcolor = input("Fill color of polygon?")

screen = Screen()

alex = Turtle()
alex.color(colorname, fcolor)

#begin coloring
alex.begin_fill()

#making shape
for i in range(sides):
    alex.forward(length)
    alex.left(360 / sides)

alex.end_fill()
#end coloring

screen.mainloop()