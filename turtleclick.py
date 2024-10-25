# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random
import tkinter

#-----game configuration----
torterracolor = "Green"
global torterrasize
torterrasize = 3
torterrashape = "turtle"
global score
score = 0
global time_left
time_left = 30
global playagain
playagain = ""
global color_list
color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

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

timer_up = False

def torterraClicked(x, y):
    global torterrasize, torterracolor
    torterra.penup()
    torterra.stamp()
    torterra.color(color_list[random.randrange(0,6)])
    torterra.goto(random.randrange(-300, 300), random.randrange(-300, 300))
    update_score()
    torterrasize *= 0.8
    if timer_up:
        timer.write("Game Over", font=("Calibri", 15, "normal"))
        torterra.hideturtle()

def countdown():
  global time_left, timer_up, playagain, score
  timer.clear()
  if time_left <= 0:
    timer.write("Time's Up", font=("Calibri", 15, "normal"))
    timer_up = True
    playagain = tkinter.messagebox.showinfo("Final Score", f"Your Final Score is {score}")
    exit()
  else:
    timer.write("Timer: " + str(time_left), font=("Calibri", 15, "normal"))
    time_left -= 1
    timer.getscreen().ontimer(countdown, 1000) 

#-----events----------------
wn = t.Screen()
wn.bgcolor("light gray")
root = tkinter.Tk()
def start_game():
    torterra.onclick(torterraClicked)
    countdown()
wn.mainloop()
