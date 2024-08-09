'''
Name: Sreelakshmi Kutty
Date: 14 Septmember 2023
Class: ISTA 130
Section Leader: Huy Tran

Homework 2 > Functions
Create 6 functions and use test_functions file to test
Answers for powershell portion below
'''

""" 
    *********************************
    Answers to questions:
    1) 11,112,142
    2) 81%
    3) 14%
    4) 1.571
    5) 3.142
    6) 2.293
    7) 3.902
    8) 9.626
    ********************************* 
"""

# Import packages
import math, random

# Six functions defined with specified parameters and output

def chases(predator, prey):
    '''
    This function prints out a sentence about predator and prey

    Parameters---
    predator: string of predator name
    prey: string of prey name

    Returns: None
    '''
    print('The', predator, 'chases the', prey)
    return None

def sum3(x, y, z):
    '''
    This function prints out a sentence with a calculated sum

    Parameters---
    x: first int to sum
    y: second int to sum
    z: third int to sum

    Returns: None
    '''
    sum = x + y + z
    print('The sum of the arguments is:', sum)
    return None

def forecast():
    '''
    This function prints out a random forecast as a percent

    Parameters: None

    Returns: None
    '''
    chance = random.randrange(101)
    print('Chance of rain today:', chance, '%')
    return None

def radians(degrees):
    '''
    This function prints degrees to radians conversion

    Parameters---
    degrees: int of the degrees to convert

    Returns: None
    '''
    rad = round(((degrees * math.pi) / 180), 3)
    print('The angle in radians is:', rad)
    return None

def decimal(num):
    '''
    This function prints the decimal portion of a number

    Parameters---
    num: (float) decimal to cut

    Returns: None
    '''
    ans = round((num - (math.floor(num))), 3)
    print('Decimal part:', ans)
    return None

def erf_plus_gamma(num):
    '''
    This function prints out a gamma/erf conversion

    Parameters---
    num: (int) number to convert

    Returns: None
    '''
    ans = round((math.erf(num) + math.gamma(num)), 3)
    print('Result:', ans)
    return None


def main():
    '''
    This file calls the above functions to test and troubleshoot
    '''

    #Testing my functions
    print('Testing chases')
    chases('dragon', 'human')
    
    print('Testing sum3')
    sum3(1, 2, 3)

    print('Testing forecast')
    forecast()

    print('Testing radians')
    radians(30)

    print('Testing decimal')
    decimal(5.98391)

    print('Testing erf_plus_gamma')
    erf_plus_gamma(0.6)
    erf_plus_gamma(0.22)

if __name__ == '__main__':
    main()


