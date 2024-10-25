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
global time_left
time_left = 60

#-----initialize turtle-----
torterra = t.Turtle()
torterra.shape(torterrashape)
torterra.color(torterracolor)
torterra.shapesize(torterrasize)
torterra.speed(0)

scoreboard = t.Turtle()
scoreboard.shapesize(0.00001)
scoreboard.penup()
scoreboard.goto(-300,300)
scoreboard.pendown()

timer = t.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(300,300)
timer.pendown()

#-----game functions--------
score = 10
def update_score():
    global score
    scoreboard.clear()
    score += 10
    scoreboard.write(f"Score: {score}", font=("Calibri", 15, "normal"))

game_over = False
def time_up():
    global game_over
    game_over = True

def torterraClicked(x, y):
    global torterrasize
    torterra.penup()
    torterra.goto(random.randrange(-400, 400), random.randrange(-300, 300))
    update_score()
    if game_over:
        timer.write("Game Over", font=("Calibri", 15, "normal"))
        torterra.hideturtle()

def countdown():
  global time_left, timer_up
  timer.clear()
  if time_left <= 0:
    timer.write("Time's Up", font=("Calibri", 15, "normal"))
    timer_up = True
  else:
    timer.write("Timer: " + str(time_left), font=("Calibri", 15, "normal"))
    time_left -= 1
    timer.getscreen().ontimer(countdown, 1000) 

torterra.onclick(torterraClicked)

#-----events----------------
wn = t.Screen()
wn.bgcolor("light gray")
countdown()
wn.mainloop()
