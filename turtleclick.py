# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import time
import random

#-----game configuration----
torterracolor = "Green"
torterrasize = 3
torterrashape = "turtle"

#-----initialize turtle-----
torterra = t.Turtle()
torterra.shape(torterrashape)
torterra.color(torterracolor)
torterra.shapesize(torterrasize)
torterra.speed(0)

#-----game functions--------
def torterraClicked (x,y):
    torterra.write("You clicked this", font=("Caliri", 15, "normal"))
    torterra.penup()
    torterra.goto(random.randrange(-400, 400), random.randrange(-300, 300))
torterra.onclick(torterraClicked)

#-----events----------------
wn = t.Screen()
wn.mainloop()
