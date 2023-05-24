def turn_right():
     for x in range(0,3):
        turn_left()
start = 0
put()
while not object_here() or start == 0:
    start+=1
    while front_is_clear():
        move()
    turn_left()
    if object_here():
        break;