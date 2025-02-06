print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

side = input(
    "You're at a crossroad. Start your adventure! Where do you want to go? Type \"left\" or \"right\"\n").lower()

if side == "left":
    action = input(
        "You have come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if action == "wait":
        door = input(
            "You arrive at the island safe and unharmed. There is a house with 3 doors. one red, one yellow and one blue. Which color do you choose?\n").lower()
        if door == "yellow":
            print("Congratulations! You found the treasure. You win!!")
        elif door == "red":
            print("You were burned by fire. Game Over!")
        elif door == "blue":
            print("You were eaten by beasts. Game Over!")
        else:
            print("Invalid input. Game Over!")

    elif action == "swim":
        print("You were attacked by trout. Game Over!")

    else:
        print("Invalid input. Game Over!")

elif side == "Right":
    print("You fell into a hole. Game Over!")

else:
    print("Invalid input. Game Over!")