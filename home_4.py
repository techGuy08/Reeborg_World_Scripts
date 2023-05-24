def turn_right():
     for x in range(0,3):
        turn_left()
while not at_goal():
  while front_is_clear():
    move()
  turn_left()
  while front_is_clear():
    move()
  turn_right()
  while front_is_clear():
    move()
  turn_right()