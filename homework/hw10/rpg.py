'''
Author: Sreelakshmi Kutty
Date: 3 December 2023
Class: ISTA 130
Section Leader: Huy Tran

Description:
Homework 10 > Classes
Final python assignment - create class and objects
'''
import random


class Fighter:
    def __init__(self, name):
        self.name = name
        self.hit_points = 10
    
    def __repr__(self):
        mystr = self.name + " (HP: " + str(self.hit_points) + ")"
        return mystr
    
    def take_damage(self, damage_amount):
        '''
        This method gives damage to player

        Parameters---
        damage_amount: (int) hit points to deduct

        Return: none
        '''
        self.hit_points = self.hit_points - damage_amount
        if (self.hit_points <= 0):
            print("\tAlas, " + self.name + " has fallen!")
        else:
            print("\t" + self.name + " has " + str(self.hit_points) + " hit points remaining.")
        return None
    
    def attack(self, other):
        '''
        This method creates an attack roll for player

        Parameters---
        other: (Fighter) player to attack

        Return: none
        '''
        print(self.name + " attacks " + other.name + "!")
        attack = random.randrange(1, 21)
        if(attack >= 12):
            damage = random.randrange(1, 7)
            print("\tHits for " + str(damage) + " hit points!")
            other.take_damage(damage)
        else:
            print('\tMisses!')
        return None
    
    def is_alive(self):
        '''
        This method checks if player is alive

        Return: (bool) true if alive
        '''
        if (self.hit_points > 0):
            response = True
        else:
            response = False
        return response

def combat_round(player1, player2):
    '''
    This function creates a round for two Fighter players

    Parameters---
    player1: (Fighter) first player
    player2: (Fighter) second player

    Return: none
    '''
    p1 = random.randrange(0,6)
    p2 = random.randrange(0,6)
    if(p1 == p2):
        print("Simultaneous!")
        player1.attack(player2)
        player2.attack(player1)
    elif(p1 > p2):
        player1.attack(player2)
        if(player2.is_alive()):
            player2.attack(player1)
    else:
        player2.attack(player1)
        if(player1.is_alive()):
            player1.attack(player2)
    return None


def main():
    '''
    This creates combat rounds until the death
    '''
    player1 = Fighter('Death_Mongrel')
    player2 = Fighter('Hurt_then_Pain')

    i = 1 #counter
    play = True
    while(play): #start loop for combat rounds
        print('\n' + '='*19 + ' ROUND ' + str(i) + ' ' + '='*19)
        i += 1
        print(player1)
        print(player2)
        response = input('Enter to Fight!')
        combat_round(player1, player2)
        if((not player1.is_alive()) or (not player2.is_alive())): #check if players alive
            play = False #stop if a player is dead
    
    print('The battle is over!')
    print(player1)
    print(player2)




    


if __name__ == '__main__':
    main()

