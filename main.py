import random

def guess():
    global game_attempts
    if game_difficulty == "easy":
        game_attempts = 10
    elif game_difficulty == "hard":
        game_attempts = 5

def play_game():
    global game_attempts
    while game_attempts != 0:
        enter = int(input('Make a guess: '))
        game_attempts -= 1
        if enter > computer_choice:
            print('too high')
            print(f"You have {game_attempts} left")
        elif enter < computer_choice:
            print('too low')
            print(f'You have {game_attempts} left')
        elif enter == computer_choice:
            print("YOU WINNNN")
            break


computer_choice = random.randint(1, 100)
print('WELCOME TO THE NUMBER GUESIING GAME')
print('Im thinking of a number between 1 and 100')
game_difficulty = input("Game difficulty 'easy' or 'hard'>> ")
game_attempts = 0


guess()
play_game()
