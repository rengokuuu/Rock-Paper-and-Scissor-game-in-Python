import random
choices = ['Rock','Paper','Scissors']
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input('Rock, Paper or Scissor??').capitalize()
    if player == computer:
        print('Tie')
    elif player == 'Rock':
        if computer == 'Paper':
            print("You Lose.")
            cpu_score+=1
        else:
            print("You Win.")
            player_score+=1
    elif player == 'Paper':
        if computer == 'Scissor':
            print('You Lose')
            cpu_score+=1
        else:
            print('You Win.')
            player_score += 1
    elif player == 'Scissor':
        if computer == 'Rock':
            print('You Lose.')
            cpu_score += 1
        else:
            print('You Win.')
            player_score += 1
    elif player == 'End':
        print('Final Scores: ')
        print(f'CPU: {cpu_score}')
        print(f'Player: {player_score}')