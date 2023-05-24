import math
def turn_right():
     for x in range(0,3):
        turn_left()
Run = True
x = 0
while Run:
    while front_is_clear():
        x+=1
        move()
    turn_left()
    turn_left()
    for i in range(math.ceil(x/2)):
        move()
    put()
    Run = False    
        
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
