print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')
print("Welcome to treasure hunting quest")
print("Your quest is to find the treasure")
cross_road = input('You\'re at a cross road. Where do you want to go? Type "left" or "right".\n ')
cross_road = cross_road.lower()
if cross_road == "right":
    boat = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n ')
    boat = boat.lower()
    if boat == "wait":
        door = input('You arrive at the island unharmed. There are three paths in front of you. a "cave", a "forest" and a "ruin" on the island. Which place do you choose to search?\n ')
        door = door.lower()
        if door == "ruins":
            print("you died to traps. GAME OVER hehe!")
        elif door == "forest":
            print("You got eaten by a beast. Game over hehe!")
        elif door == "cave":
            print("WINNER WINNER, CHICKEN DINNER. You got the treasure, congratulations sighs! ")
        else:
            print("Your choice doesnt exist. GAME OVER!!")
    else:
        print("You got eaten by mami water and co. GAME OVER hehe!")
else:
    print("You got shot by a stray bullet, IDIOT GAME OVER HAHAHA!!!")