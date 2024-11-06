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

options = [rock, paper, scissors]
play_again = True
while play_again == True:
    user_choice_int = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor "))

    computer_choice_int = random.randint(0, 2)
    computer_choice = options[computer_choice_int]

    if user_choice_int >= 0 and user_choice_int <= 2:
        print("Your choice: ")
        print(options[user_choice_int])

    print("Computer choice: ")
    print(computer_choice)

    if user_choice_int >= 3 or user_choice_int < 0:
        print("Invalid number")
    elif user_choice_int == 0 and computer_choice_int == 2:
        print("You win")
    elif user_choice_int == 2 and computer_choice_int == 0:
        print("You lose")
    elif user_choice_int < computer_choice_int:
        print("You lose")
    elif user_choice_int > computer_choice_int:
        print("You win")
    elif user_choice_int == computer_choice_int:
        print("It's a draw")

    play_again = input("Do you want to play again? Type 'Y' for continue: ")
    if play_again == "Y":
        play_again = True
    else:
        print("Bye!!")
        play_again = False
