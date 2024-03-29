import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

#setup the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("Black")
wn.setup(width=1000, height=1000)
wn.tracer(0) #this turns off the screen updates

#setup snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("purple")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0,100)

segments = []

#pens
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align ="center", font=("Courier", 24, "normal"))




# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

#Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")



def move():
    y = head.ycor()
    x = head.xcor()
    if head.direction == "up":
        head.sety(y + 20)

    elif head.direction == "left":
        head.setx(x - 20)

    elif head.direction == "down":
        head.sety(y - 20)

    elif head.direction == "right":
        head.setx(x + 20)


#Main Game Loop
while True:
    wn.update()
    #Check for collision with border
    if head.xcor() > 475 or head.xcor() < -475 or head.ycor() > 325 or head.ycor() < -325:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

    #check for collision with the segment
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()


            #Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    #check for collision with the food
    if head.distance(food) < 20:
        #Move the food to a random spot on the screen
        x = random.randint(-325,325,)
        y = random.randint(-325,325)
        food.goto(y, x)

        #Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay -= 0.001

        #increase the score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))

    #Move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x, y)

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    time.sleep(delay)




wn.mainloop()