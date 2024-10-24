# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import time
import random
from tkinter import Tk

#-----game configuration----
torterracolor = "Green"
global torterrasize
torterrasize = 3
torterrashape = "turtle"
global score
score = 0

#-----initialize turtle-----
torterra = t.Turtle()
torterra.shape(torterrashape)
torterra.color(torterracolor)
torterra.shapesize(torterrasize)
torterra.speed(0)

scoreboard = t.Turtle()
scoreboard.shapesize(0.00001)
scoreboard.teleport(-350,300)

timer = t.Turtle()
timer.hideturtle()
timer.teleport(350,300)

#-----game functions--------
score = 10
def update_score():
    global score
    scoreboard.clear()
    score += 10
    scoreboard.write(f"Score: {score}", font=("Calibri", 15, "normal"))

def time_up():
    global game_over
    game_over = True

def torterraClicked(x, y):
    global torterrasize
    torterra.penup()
    torterra.goto(random.randrange(-400, 400), random.randrange(-300, 300))
torterra.onclick(torterraClicked)

if game_over:
    timer.write("Game Over", font=("Calibri", 15, "normal"))

clock.schedule(time_up, 60)
#-----events----------------
wn = t.Screen()
wn.bgcolor("light gray")
wn.mainloop()
