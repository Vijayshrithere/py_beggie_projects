#snake , water = snake will drink water
# water , gun = gun will be sink in water
# snake , gun = gun will fire snake

import random
rounds = 0
mypoints = 0
computerpoints = 0
while rounds < 10:
    my_list = ["snake", "water", "gun"]
    computer = random.choice(my_list)
    me = input("enter any among (s for snake , w for water & g for gun):\n")

    if me == "s" and computer == "water" :
        mypoints+=1
        computerpoints += 0
        rounds+=1

    elif me == "s" and computer == "gun":
        mypoints += 0
        computerpoints += 1
        rounds += 1

    elif me == "s" and computer == "snake":
        mypoints += 0
        computerpoints += 0
        rounds += 1

    elif  me == "w" and computer == "water":
        mypoints += 0
        computerpoints += 0
        rounds += 1

    elif me == "w" and computer == "gun":
        mypoints += 1
        computerpoints += 0
        rounds += 1

    elif  me == "w" and computer == "snake":
        mypoints += 0
        computerpoints += 1
        rounds += 1

    elif  me == "g" and computer == "water":
        mypoints += 0
        computerpoints += 1
        rounds += 1

    elif  me == "g" and computer == "snake":
        mypoints += 1
        computerpoints += 0
        rounds += 1

    else:
        mypoints += 0
        computerpoints += 0
        rounds += 1

if mypoints > computerpoints:
    print("you won")
elif mypoints == computerpoints:
    print("match is draw,play again!")
else:
    print("sorry you lost")
