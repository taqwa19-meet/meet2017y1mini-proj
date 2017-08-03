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
snake.shape("circle")
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
direction= UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
UP_EDGE = 250

def up():
    global direction
    direction= UP
    print("you pressed the up key")

def down():
    global direction
    direction=DOWN
    print("you presed the down key")

def right():
    global direction
    direction= RIGHT
    print("you pressed the right key")

def left():
    global direction
    direction=LEFT
    print("you preesed the left key")
    
#image setup
turtle.register_shape("deathly_hallows.gif")
food = turtle.clone()
food.shape("deathly_hallows.gif")


turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)

turtle.listen()


############################################################

def make_food():

    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1

    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE


    food.goto(food_x,food_y)
    new_food_pos=(food_x,food_y)
    food_pos.append(new_food_pos)


    food_ID=food.stamp()
    food_stamps.append(food_ID)
    
    

############################################################


def move_snake():
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    

    if direction == RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print("you moved right")
    elif direction ==LEFT:
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print("you moved left")
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print("you moved up")
    elif direction ==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print("you moved down")


    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last
    #piece of the tail


    if my_pos in pos_list[0:-1]:
        print("you ate yourself!game over!")
        quit()
        
    if new_x_pos>=RIGHT_EDGE:
        print("you hit the right edge!game over!")
        quit()
    if new_x_pos<=LEFT_EDGE:
        print("you hit the left edge!game over!")
        quit()
    if new_y_pos>=UP_EDGE:
        print("you hit the up edge!game over!")
        quit()
    if new_y_pos<=DOWN_EDGE:
        print("you hit the down edge ")
        quit()

    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind) 
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
        make_food()
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    

    turtle.ontimer(move_snake,TIME_STEP)

make_food()
move_snake()



##food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
##food_stamps = []
##
##for this_food_pos in food_pos:
##    food.goto(this_food_pos)
##    food_ID=food.stamp()
##    food_stamps.append(food_ID)


import turtle

turtle.penup()
turtle.goto(-500,-300)
turtle.pendown()
turtle.goto(-500,250)
turtle.goto(500,250)
turtle.goto(500,-300)
turtle.goto(-500,-300)





    
