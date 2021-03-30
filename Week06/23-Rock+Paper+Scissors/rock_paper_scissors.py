###############################################################################
# Author: Jacob Kutcka
# Date: Mar 18, 2021
# This program will play rock, paper, scissors at random with the user
###############################################################################

import random
c = ['rock', 'paper', 'scissors']

def main():
    # Write your mainline logic here ------------------------------------------
    # Find choices
    comp_choice = get_computer_choice()
    player_choice = get_player_choice()

    # Determine winner
    winner = get_winner(comp_choice, player_choice)

    # Show each side
    print('  The computer chose ' + comp_choice + ', and you chose ' + player_choice + '.')
    # If player wins, print 'win'
    if winner == 'player':
        print('  ' + player_choice + ' beats ' + comp_choice)
        print('  You won the game!')
    # If computer wins, print 'lost'
    else:
        print('  ' + comp_choice + ' beats ' + player_choice)
        print('  You lost.  Better luck next time.')
    print('Thanks for playing.')
def get_computer_choice():
    return random.choice(c)

def get_player_choice():
    while 1:
        player = input('Choose rock, paper, or scissors: ')
        if player == 'rock' or player == 'paper' or player == 'scissors':
            return player
        else:
            print('You made an invalid choice. Please try again.')

def get_winner(com, meat_bag):
        if meat_bag == com:
            return 'tie'
        elif meat_bag == 'rock':
            if com == 'paper':
                return 'computer'
            else:
                return 'player'
        elif meat_bag == 'paper':
            if com == 'rock':
                return 'player'
            else:
                return 'computer'
        else:
            if com == 'rock':
                return 'computer'
            else:
                return 'player'

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
