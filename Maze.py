def turn_right():
     for x in range(0,3):
        turn_left()

right_moves = 0
while not at_goal():    
   if right_is_clear() and right_moves < 4:
    turn_right()
    move()
    right_moves += 1
   elif front_is_clear():
     move()
     right_moves = 0
   else:
    while not front_is_clear():
     turn_right()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
