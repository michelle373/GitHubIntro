# Michelle Patlan
# 8/6/2022
#draw some kind of picture with turtle

from turtle import Screen, Turtle

screen = Screen()

alex = Turtle()

#face circle
alex.fillcolor('yellow')
alex.begin_fill()
alex.circle(100)
alex.end_fill()
alex.up()

#eyes
alex.goto(-40, 120)
alex.dot(15, 'white')
alex.goto(-40, 120)
alex.dot(7, 'black')
alex.goto(40, 120)
alex.dot(15, 'white')
alex.goto(40, 120)
alex.dot(7, 'black')

#smile
alex.goto(-40, 85)
alex.down()
alex.right(90)
alex.circle(40, 180)
alex.up()
screen.mainloop()