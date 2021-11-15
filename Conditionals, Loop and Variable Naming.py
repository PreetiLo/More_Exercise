# from random import randint
# def win():
#     print ('You win!')
# def lose():
#     print ('You lose!')
# while False:
#     player_choice = input('What do you pick? (rock, paper, scissors)')
#     player_choice.strip()
#     random_move = randint(0, 2)
#     moves = ['rock', 'paper', 'scissors']
#     computer_choice = option[random_move]
#     if player_choice = computer_choice:
#         print ('Draw!')
#     elif  == 'rock' and coMp == 'scissors':
#         win()
#     elif  == 'paper' and comp == 'scissors':
#         lose()
#     elif playe == 'scissors' and comp == 'paper':
#         win()
#     elif player == 'scissors' and Comp == 'rock':
#         lose()
#     elif payer == 'paper' and computer == 'rock':
#         win()
#     elif player ==  and comp == :
#         lose()
#     aGain = input('Do you want to play again? (y or n)').strip()
#     if again == 'n':
#         break


import random

while True:
    u = input("Enter a choice (rock, paper, scissors): ")
    p = ["rock", "paper", "scissors"]
    c = random.choice(p)
    print(f"\nYou chose {u}, computer chose {c}.\n")

    if u== c:
        print(f"Both players selected {u}. It's a tie!")
    elif u== "rock":
        if c == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif u == "paper":
        if c == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif u == "scissors":
        if c == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
