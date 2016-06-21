
#draw squre, circle and triangle
"""
import turtle

def initiate_turtle():


	brad.shape("turtle")
	brad.color("blue")
	brad.speed("normal")	

def draw_square():


	for x in xrange(0,4):
		brad.forward(100)
		brad.right(90)
	#window.exitonclick()


def draw_circle():
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("yellow")
	angie.circle(100)

	#window.exitonclick()


def draw_triangle():

	
	for x in range(0,3):
		brad.forward(100)
		brad.right(120)

	#window.exitonclick()	

background = turtle.Screen()
background.bgcolor("red")

brad = turtle.Turtle()
initiate_turtle()
draw_square()
draw_circle()
draw_triangle()

background.exitonclick()
"""
"""
#example
import turtle

def draw_squre(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("white")
	#create the turtle Brad - 
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)
	
	for i in range(0,36):
		draw_squre(brad)
		brad.right(10)

	window.exitonclick()


draw_art()

"""

#example2
import turtle
def draw_rhombus(flower1_turtle, flower_length, flower_angle):
	for i in range (1,3):
		flower1_turtle.forward(flower_length)
		flower1_turtle.left(180 - flower_angle)
		flower1_turtle.forward(flower_length)
		flower1_turtle.left(flower_angle)

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("white")

	flower = turtle.Turtle()
	flower.shape("turtle")
	flower.color("blue")
	flower.speed(10)

	for i in range(1,73):
	    draw_rhombus(flower, 100, 140)
	    flower.right(5)	

	flower.right(90)
	flower.forward(300)	

	flower.right(150)
	draw_rhombus(flower, 150, 140)	

	flower.right(60)
	draw_rhombus(flower, 150, 140)	

	flower.hideturtle()	

	window.exitonclick()

draw_shapes()