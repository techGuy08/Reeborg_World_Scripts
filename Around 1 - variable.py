def turn_right():
     for x in range(0,3):
        turn_left()
put()
Run = True
while Run:
    while front_is_clear():
        move()
        if object_here():
           Run = False
           break;
    turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
