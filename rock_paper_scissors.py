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
welcome_message = '''
. ____ ____ ____ _  _      ___  ____ ___  ____ ____      ____ ____ _ ____ ____ ____ ____ ____ . 
' |__/ |  | |    |_/       |__] |__| |__] |___ |__/      [__  |    | [__  [__  |  | |__/ [__  ' 
  |  \ |__| |___ | \_ .    |    |  | |    |___ |  \ .    ___] |___ | ___] ___] |__| |  \ ___]   
                      '                             '                                           
                                    ____ ____ _  _ ____                                         
                                    | __ |__| |\/| |___                                         
                                    |__] |  | |  | |___                                         
'''
win_message = '''
_   _ ____ _  _    _ _ _ _ _  _   /
 \_/  |  | |  |    | | | | |\ |  / 
  |   |__| |__|    |_|_| | | \| .  
                                   
'''
lose_message = '''
_   _ ____ _  _    _    ____ ____ ____   /
 \_/  |  | |  |    |    |  | [__  |___  / 
  |   |__| |__|    |___ |__| ___] |___ .  
                                          
'''
draw_message = '''
_ ___ . ____    ____    ___  ____ ____ _ _ _   /
|  |  ' [__     |__|    |  \ |__/ |__| | | |  / 
|  |    ___]    |  |    |__/ |  \ |  | |_|_| .  
                                                
'''

print(welcome_message)
drawings = [rock, paper, scissors]


def game_loop():
    flag = False
    draw_flag = False
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
            draw_flag = True

        if player_choice == 0 and computer_choice == 2:
            flag = True
        elif player_choice == 1 and computer_choice == 0:
            flag = True
        elif player_choice == 2 and computer_choice == 1:
            flag = True

        if flag:
            print(win_message)
        elif draw_flag:
            print(draw_message)
        else:
            print(lose_message)

        print("Do you want another game?")
        new_game = input("Choose Y or N\n").upper()

        if new_game == "Y":
            game_loop()
        else:
            print("Thanks for playing!")
        break


game_loop()
