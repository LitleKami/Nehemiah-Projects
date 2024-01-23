import random
player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n")
player = int(player)
if player >= 0 and player <= 2:
    me = random.randint(0, 2)
    if player == 0:
        if me == 1:
            print("You chose rock, i chose paper, you lose!!")
        elif me == 0:
            print("You chose rock, i chose rock, Draw!!")
        else:
            print("You chose rock, i chose scissors, You win!!")
    elif player == 1:
        if me == 0:
            print("You chose paper, i chose rock, You win!!")
        elif me == 1:
            print("You chose paper, i chose paper, Draw!!")
        else:
            print("You chose paper, i chose scissors, You lose!!")
    elif player == 2:
        if me == 0:
            print("You chose scissors, i chose rock, You lose!!")
        elif me == 1:
            print("You chose scissors, i chose paper, You win!!")
        else:
            print("You chose scissors, i chose scissors, Draw!!")    
else:
    print("Wrong input. You lose!!")



