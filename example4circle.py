from turtle import *
t= Turtle()
t.speed("fastest")
s=getscreen()

for i in range(10):
    t.fd(100)
    t.lt(360//10)
    t.circle(20)
    t.dot(5)
    t.circle(50,180)
mainloop()    