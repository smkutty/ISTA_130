'''
Author: Sreelakshmi Kutty
Date: 26 September 2023
Class: ISTA 130
Section Leader: Huy Tran

Description:
Homework 4 > Returning Values and Simple Conditions
'''

# Import packages
import math, random

# My functions

def print_scores(name_1, score_1, name_2, score_2):
    '''
    This function prints the players scores

    Parameters---
    name_1: name of player one (str)
    score_1: score of player 1 (int)
    name_2: name of player two (str)
    score_2: score of player 2 (int)

    Return: None
    '''
    print('\n--- SCORES\t' + name_1 + ': ' + str(score_1) + '\t' + name_2 +': ' + str(score_2) + ' ---')
    return None

def check_for_winner(name, score):
    '''
    This function checks if the player won

    Parameters---
    name: player's name (str)
    score: player's score (int)

    Returns: true if won (bool)
    '''
    result = True
    if(score >= 50):
        print('THE WINNER IS: ' + name + '!!!!!')
    else:
        result = False
    return result

def roll_again(name):
    '''
    This function asks and checks if player wants to roll again

    Parameters---
    name: player's name (str)

    Return: true if wants to roll again (bool)
    '''
    result = False
    doit = True
    while(doit):
        response = input('Roll again, ' + name + '? (Y/N) ')
        if(is_N_Y(response) == -1):
            print("I don't understand: " + '"' + response + '". Please enter either "Y" or "N".')
        else:
            doit = False
    return bool(is_N_Y(response))

def is_N_Y(str):
    '''
    This is a helper function for roll_again to check what input
    player gave and if valid

    Parameters---
    str: player's response from roll_again (str)

    Return: correspinding number for response (int)
    '''
    result = -1
    if((str == 'Y') | (str == 'y')):
        result = 1
    elif((str == 'N') | (str == 'n')):
        result = 0
    return result

def play_turn(name):
    '''
    This function plays a turn and adds dice score

    Parameters---
    name: player name (str)

    Return: total score after turns (int)
    '''
    print('---------- ' + name + "'s turn ----------")
    total = 0
    doit = True
    while(doit):
        score = random.randint(1, 6)
        print('\t<<< ' + name + ' rolls a ' + str(score) + ' >>>')
        if(score == 1):
            total = 0
            print('\t!!! PIG! No points earned, sorry ' + name + ' !!!')
            input('(enter to continue)')
            doit = False
        else:
            total += score
            print('\tPoints:', total)
            doit = roll_again(name)
    return total



def main():
    '''
    This file uses the above function to play a game called Pig Dice
    Two players can enter their names and roll dice to reach 50 points
    '''

    # Setting up game and asking for user input
    print('\n \nPig Dice')
    player_1 = input('Enter name for player 1: ')
    player_2 = input('Enter name for player 2: ')
    print('\tHello ' + player_1 + ' and ' + player_2 + ', welcome to Pig Dice!')

    # Initializing scores
    player_1_score = 0
    player_2_score = 0
    print_scores(player_1, player_1_score, player_2, player_2_score)

    # Loop through players until winner
    doit = True
    while(doit):
        player_1_score += play_turn(player_1)
        print_scores(player_1, player_1_score, player_2, player_2_score)
        if(check_for_winner(player_1, player_1_score)):
            doit = False
        else:
            player_2_score += play_turn(player_2)
            print_scores(player_1, player_1_score, player_2, player_2_score)
            if(check_for_winner(player_2, player_2_score)):
                doit = False 


if __name__ == '__main__':
    main()

