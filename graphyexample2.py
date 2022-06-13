from turtle import *

pencolor("red")
pensize(3)
fillcolor("blue")
speed("fastest") #determines speed of turle
for i in range (10,0,-1): #loop 
    begin_fill()
    circle(i*10)
    rt(25)
    end_fill()
goto(150,-2) #sends turtle to coodinate location as mentioned
mainloop()   