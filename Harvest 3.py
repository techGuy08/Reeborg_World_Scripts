row = 1
def turn_right():
     for x in range(0,3):
        turn_left()
def move_straight(n):   
    if n:
      for i in range(n):
        if front_is_clear(): 
          move()
    else:
      while front_is_clear():
        while object_here():
         take()
        move()
def switch_dir(dir):
    if dir == "right":
      turn_left()
      move_straight(1)
      turn_left()
    elif dir == "left":
      turn_right()
      move_straight(1)
      turn_right()
def fix_row(dir):
    if row >= 3 and row <= 8:
      if dir == "right":
        turn_left()
        turn_left()
      else:
        turn_right()
        turn_right()
      move()
      for i in range(6):
        move()
        put()
      move()
      move()
      if dir == "right":
        turn_right()
        turn_right()
      else:
        turn_left()
        turn_left()
      while front_is_clear():
        move()
row = 1
for i in range(4):
  move_straight(0)
  fix_row("right")
  row+=1
  switch_dir("right")
  move_straight(0)
  fix_row("left")
  row+=1
  switch_dir("left")
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
