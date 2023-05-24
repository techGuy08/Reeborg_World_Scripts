def turn_right():
     for x in range(0,3):
        turn_left()
def move_straight():   
      while front_is_clear():
        move()
def jump():
    turn_left()
    for x in range(2):
      move()
      turn_right()
    move()
    turn_left()
while not at_goal():
    move_straight()
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
