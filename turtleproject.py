from turtle import Turtle, Screen

jinny = Turtle()
jinny.shape("turtle")
jinny.color("red")

for i in range(15):    
    jinny.fd(10)
    jinny.penup()
    jinny.fd(i)
    jinny.pendown()

  



jinny.fd(50)
jinny.penup()
jinny.pendown()
jinny.fd(5)

"""" 
jinny.forward(100)
jinny.setheading(90)
jinny.forward(100)
jinny.setheading(180)
jinny.forward(100)
jinny.setheading(270)
jinny.forward(100)
"""

screen = Screen()
screen.exitonclick()


""" 
jinny.forward(100)
jinny.setheading(180)
jinny.forward(100)
jinny.setheading(270)


"""