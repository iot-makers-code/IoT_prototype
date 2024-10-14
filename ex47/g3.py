from turtle import *
speed(0)
bgcolor('black')
pencolor('white')
x=0
up();rt(45);fd(50);rt(135);down()
colors=['white', 'purple', 'blue', 
        'green', 'yellow', 'orange']
while x<120:
   for i in range(6):
      fd(150);rt(62);pencolor(colors[i])
   rt(11.111)
   x = x+1
exitonclick()