from turtle import *
s=getscreen()
s.setup(1020,720)
colors= ["purple","blue"]
pencolor("green")
pensize(5)
for i in range (6,0,-1):
    penup()
    setpos(0,-20*1)
    pendown()
    fillcolor(colors[i%2])
    begin_fill()
    circle(20*i)
    end_fill()
mainloop()