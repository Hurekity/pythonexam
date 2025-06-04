from turtle import *
tracer(0) #instadraw
screensize(2500,2500) # necessary
k = 30 # переменная масштаба рисунка
for i in range(9):
    forward(22 * k)
    right(90)
    forward(6 * k)
    right(90)
up() # tail up
forward(1 * k)
right(90)
forward(5 * k)
left(90)
down() # tail down
for i in range(9):
    forward(52 * k)
    right(90)
    forward(75 * k)
    right(90)

up()
for x in range(-25,25):
    for y in range(-25,25):
        goto(x * k,y * k)
        dot(3, 'blue')
# херня с координатами

update() # necessary
exitonclick() # necessary
#t.circle() - круг, параметр является радиусом