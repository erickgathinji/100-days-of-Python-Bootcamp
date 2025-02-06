import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
comp = int(random.randint(0, 2))

if choice >= 3 or choice < 0:
    print("Invalid input! You loose")
else:
    print(images[choice])
    print("Computer chose:")
    print(images[comp])

    if choice == 0 and comp == 2:
        print("Congratulations! You win.")
    elif choice > comp:
        print("Congratulations! You win.")
    elif comp == 0 and choice == 2:
        print("You loose")
    elif comp > choice:  # except 0 and 2
        print("You loose")
    elif choice == comp:
        print("It's a tie!")
