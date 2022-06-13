from turtle import *
t= Turtle()
t.speed("fast")
s=getscreen()
bgcolor("black")
t.color("White")
pensize(2)

for i in range(1,101,3):
    t.fd(i)
    t.lt(60)
    t.dot(20)
mainloop()    