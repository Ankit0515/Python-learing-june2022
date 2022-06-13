from turtle import *

fillcolor("red")
begin_fill() #place this code before you wish to color
for i in range(5):
    fd(100)
    lt(72)
end_fill() # place were you wish to end color
fillcolor("yellow")
begin_fill()
circle(50)
end_fill()
mainloop()
