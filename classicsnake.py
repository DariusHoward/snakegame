#Resources used:
#https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900
#https://www.youtube.com/watch?v=Vi0AhyUCCkE&list=PL_h86oT7YqVVZ6d4j1yEryCmNkEkQyJwJ&index=16&t=0s

#i did not create this project on my own I used the resources above to create this work
#I plan to add more comments in the furture


#this project still has soem changes I need to make


# need these imports to use certain features in the program 
import turtle
import time
import random

delay = 0.1

#scoring 
score = 0
highscore = 0

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

snakehead = turtle.Turtle()
snakehead.speed(0)
snakehead.shape("circle")
snakehead.color("green")
snakehead.penup()
snakehead.goto(0,0)
snakehead.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("green")
food.penup()
food.goto(0,100)


sections = []

#using the pen to draw
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Times New Roman", 24, "normal"))

def go_up():
    if snakehead.direction != "down":
        snakehead.direction = "up"

def go_down():
    if snakehead.direction != "up":
        snakehead.direction = "down"

def go_left():
    if snakehead.direction != "right":
        snakehead.direction = "left"

def go_right():
    if snakehead.direction != "left":
        snakehead.direction = "right"

def move():
    if snakehead.direction == "up":
        y = snakehead.ycor()
        snakehead.sety(y + 20)

    if snakehead.direction == "down":
        y = snakehead.ycor()
        snakehead.sety(y - 20)

    if snakehead.direction == "left":
        x = snakehead.xcor()
        snakehead.setx(x - 20)

    if snakehead.direction == "right":
        x = snakehead.xcor()
        snakehead.setx(x + 20)

# Keyboard bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")



while True:
    window.update()

    # Check for a collision with the border
    if snakehead.xcor()>290 or snakehead.xcor()<-290 or snakehead.ycor()>290 or snakehead.ycor()<-290:
        time.sleep(1)
        snakehead.goto(0,0)
        snakehead.direction = "stop"

        # Hide the sections
        for section in sections:
            section.goto(1000, 1000)
        
        # Clear the sections list
        sections.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("Courier", 24, "normal")) 



    if snakehead.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)
    
            # Add a section
            new_section = turtle.Turtle()
            new_section.speed(0)
            new_section.shape("circle")
            new_section.color("green")
            new_section.penup()
            sections.append(new_section)
    
            # Shorten the delay
            delay -= 0.001
    
            # Increase the score
            score += 10

            if score > highscore:
                highscore = score
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("Courier", 24, "normal")) 

    for index in range(len(sections)-1, 0, -1):
            x = sections[index-1].xcor()
            y = sections[index-1].ycor()
            sections[index].goto(x, y)
            
    if len(sections) > 0:
        x = snakehead.xcor()
        y = snakehead.ycor()
        sections[0].goto(x,y)

    move()    
    
    for section in sections:
        if section.distance(snakehead) < 20:
            time.sleep(1)
            snakehead.goto(0,0)
            snakehead.direction = "stop"
        
            # Hide the sections
            for section in sections:
                section.goto(1000, 1000)
        
            # Clear the sections list
            sections.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

window.mainloop()

    
       
    
