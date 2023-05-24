def turn_right():
     for x in range(0,3):
        turn_left()
def center():
  x = 0  
  while front_is_clear():
    x+=1
    move() 
  turn_left()
  turn_left()
  for i in range(int(x/2)):
    move()
center() 
turn_right()
center()
put()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
