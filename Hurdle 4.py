def turn_right():
     for x in range(0,3):
        turn_left()
def move_straight():   
      while front_is_clear() and not at_goal():
        move()
def jump():
    if at_goal():
      return
    turn_left()
    while not right_is_clear():
      move()
    turn_right()
    move()
    turn_right()
    move_straight()
    turn_left()
while not at_goal():
    move_straight()
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
