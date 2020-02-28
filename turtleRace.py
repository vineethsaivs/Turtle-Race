from turtle import *
from random import randint
speed(10)
penup()
goto(-140, 140)
for step in range (21):
    write (step, align= 'center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
    
atkin = Turtle()
atkin.color('red')
atkin.shape('turtle')

atkin.penup()
atkin.goto(-160,90)
atkin.pendown()


bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,60 )
bob.pendown()

cact = Turtle()
cact.color('yellow')
cact.shape('turtle')

cact.penup()
cact.goto(-160,30)
cact.pendown()


for turn in range(100):
    atkin.forward(randint(1,7))
    bob.forward(randint(1,7))
    cact.forward(randint(1,7))
done()
        
