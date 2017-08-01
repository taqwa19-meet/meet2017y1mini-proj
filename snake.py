import turtle
import random

turtle.tracer(1,0)
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()

SQUARE_SIZE=20
START_LEGNTH=6

pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

for i in range(9) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]
#Add SQUARE_SIZE to x_pos. Where does x_pos point to now?
# You're RIGHT!
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)#Store position variables in a tuple
    snake.goto(x_pos,y_pos)#Move snake to new (x,y)
    #Append the new position tuple to pos_list
    my_pos=(x_pos,y_pos)
    pos_list.append(pos_list)
    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.
    x = snake.stamp()
    stamp_list.append(x)

UP_ARROW = "Up"
LEFT_ARROW = "Left" 
DOWN_ARROW = "Down" 
RIGHT_ARROW = "Right" 
TIME_STEP = 100 
SPACEBAR = "space"# Careful, it's not supposed to be capitalized!
UP = 0
DOWN=1
LEFT=2
RIGHT=3

def up():
    global direction
    direction= UP
    move_snake()
    print("you pressed the up key")

def down():
    global direction
    direction=DOWN
    move_snake()
    print("you presed the down key")

def right():
    global direction
    directon= RIGHT
    move_snake()
    print("you pressed the down key")

def left():
    global direction
    direction=LEFT
    move_snake()
    print("you preesed the left key")
    


turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)

    
