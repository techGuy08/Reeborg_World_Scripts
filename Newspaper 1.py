def turn_right():
     for x in range(0,3):
        turn_left()
def move_straight():
  x=1
  while front_is_clear():
    move()
    x+=1
    if y == 4 and x == 3:
        put()
        while object_here("token"):
            take("token")
       
y = 1
take()
for i in range(3):
  turn_left()
  move_straight()
  turn_right()
  y+=1
  move_straight()
turn_left()
turn_left()
for i in range(3):
  y-=1
  move_straight()
  turn_left()
  move_straight()
  turn_right()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
