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


print("Welcome to the game 'Rock, Paper, Scissors'")
flag = False
drawings = [rock, paper, scissors]
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

while not player_choice.isdigit():
    print("Wrong input! Try again.")

    player_choice = input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

while True:
    if player_choice in ["0", "1", "2"]:
        player_choice = int(player_choice)
        player_drawing = drawings[player_choice]
        print(f"You choose:")
        print(player_drawing)
    else:
        print("Wrong input! Try again.")
        player_choice = input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
        continue

    computer_choice = random.randint(0, len(drawings) - 1)
    computer_drawing = drawings[computer_choice]
    print(f"Computer choose:")
    print(computer_drawing)

    if player_choice == computer_choice:
        print("It's a draw!")
        break

    if player_choice == 0 and computer_choice == 2:
        flag = True
    elif player_choice == 1 and computer_choice == 0:
        flag = True
    elif player_choice == 2 and computer_choice == 1:
        flag = True

    if flag:
        print("You win!")
    else:
        print("You lose!")

    break
