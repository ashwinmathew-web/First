import turtle
import math

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(10)

# Function to draw a circle
def draw_circle(radius, color):
    t.begin_fill()
    t.fillcolor(color)
    t.circle(radius)
    t.end_fill()

# Function to draw flower petals
def draw_petal(radius, angle, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(4):
        t.circle(radius, angle)
        t.left(180 - angle)
    t.end_fill()

# Function to draw a flower pattern
def draw_flower(radius, angle, petals, color):
    for _ in range(petals):
        draw_petal(radius, angle, color)
        t.left(360 / petals)

# Function to draw concentric circles for Pookalam
def draw_pookalam():
    colors = ["yellow", "orange", "darkred", "violet", "darkgreen", "purple"]
    radius = 150
    for i in range(6):
        draw_circle(radius, colors[i])
        radius -= 15  # Decrease the radius for the next circle
        t.penup()
        t.sety((t.ycor() + 15))  # Move upward by the radius difference for overlap
        t.pendown()

# Function to add floral designs
def add_flower_patterns():
    t.penup()
    t.goto(0, 150)  # Set position
    t.pendown()
    t.left(90)
    draw_flower(90,90,7, "pink") 
    draw_flower(80,80,7,"purple")
    draw_flower(70,70,7,"white")
    draw_flower(60,60,7,"darkred")
    draw_flower(50,50,7,"darkgreen")
    t.right(180)
      # Outer flower

# Main function to create the Pookalam
def create_pookalam():
    draw_pookalam()
    add_flower_patterns()

# Start drawing
create_pookalam()

# Hide turtle and display the result
t.hideturtle()
turtle.done()