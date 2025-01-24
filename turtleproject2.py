from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()



screen.exitonclick()



""" 
def move_forward():
    jim.forward(10)

def move_backwards():
    jim.backward(10)
    
def move_counterclockwise():
    jim.left(45)

def move_clockwise():
    jim.right(45)
   

def clear():
    jim.clear()
    jim.setpos(0,0)
    
    
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

"""