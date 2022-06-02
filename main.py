import random

def play():
    possible_action = ['R', 'P', 'S']
    computer = random.choice(possible_action)
    player = input('''Pick a weapon:'R' for rock, 'P' for Paper, 'S' for scissors  ''').capitalize()

    while player not in possible_action:
        player = input('''Invalid Input, Try again!: Pick a weapon: 'R' for rock, 'P' for Paper, 'S' for scissors  ''').capitalize()

    if player == computer:
        print(f'player ({player}) : CPU ({computer})') 
        print('It\'s a tie')
        return play()
    # r > s, s > p, p > r
    elif player == "R":
        if computer == "P":
            print(f'player ({player}) : CPU ({computer})')
            print("You lose!")
        if computer == "S":
            print(f'player ({player}) : CPU ({computer})')
            print("You win!")

    elif player == "S":
        if computer == "R":
            print(f'player ({player}) : CPU ({computer})')
            print("You lose!")
        if computer == "P":
            print(f'player ({player}) : CPU ({computer})')
            print("You win!")

    elif player == "P":
        if computer == "S":
            print(f'player ({player}) : CPU ({computer})')
            print("You lose!")
        if computer == "R":
            print(f'player ({player}) : CPU ({computer})')
            print("You win!")
play()