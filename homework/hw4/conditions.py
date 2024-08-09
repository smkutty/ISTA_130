'''
Author: Sreelakshmi Kutty
Date: 26 September 2023
Class: ISTA 130
Section Leader: Huy Tran

Description:
Homework 4 > Returning Values and Simple Conditions
'''

# Import packages
import math

# My 8 functions

def word_length(str, num):
    '''
    This function compares a word length to a number

    Parameters---
    str: word to compare (string)
    num: length to compare (int)

    Return: None
    '''
    if(num < len(str)):
        print('Longer than', num, 'characters:', str)
    elif(num > len(str)):
        print('Shorter than', num, 'characters:', str)
    else:
        print('Exactly', num, 'characters:', str)
    return None

def stop_light(light, num):
    '''
    This function deteremines a traffic light color

    Parameters---
    light: color light (string)
    num: how long it's been that color (int)

    Return: color of light (string)
    '''
    result = light
    if((light == 'green') & (num > 60)):
        result = 'yellow'
    elif((light == 'yellow') & (num > 5)):
        result = 'red'
    elif((light == 'red') & (num > 55)):
        result = 'green'
    else: result = light
    return result

def is_normal_blood_pressure(sys, dias):
    '''
    This function determines if a blood pressure is high

    Parameters---
    sys: systolic pressure (int)
    dias: diastolic pressure (int)

    Return: true if high (boolean)
    '''
    return ((sys < 120) & (dias < 80))

def doctor():
    '''
    This function takes your blood pressure reading

    Parameters: none

    Return: none
    '''
    sys = int(input('Enter your systolic reading: '))
    dias = int(input('Enter your diastolic reading: '))
    result = is_normal_blood_pressure(sys, dias)
    if (result):
        print('Your blood pressure is normal.')
    else: print('Your blood pressure is high.')
    return None

def pants_size(size):
    '''
    This function determines your pant size

    Parameters---
    size: waist size in inches (int)

    Return: pant size (string)
    '''
    result = ''
    if(size >= 34):
        result = 'large'
    elif(size >= 30):
        result = 'medium'
    else:
        result = 'small'
    return result

def pants_fitter():
    '''
    This function helps you buy pants

    Parameters: none

    Return: none
    '''
    #print('Enter your name:')
    name = input('Enter your name: ')
    print('Greetings', name, 'welcome to Pants-R-Us')
    #print('Enter your waist size in inches:')
    waist = int(input('Enter your waist size in inches: '))
    size = pants_size(waist)
    #print('How many pairs of pants would you like:')
    many = int(input('How many pairs of pants would you like: '))
    #print('Would you like regular or fancy pants?')
    style = input('Would you like regular or fancy pants? ')
    if(style == 'regular'):
        cost = many * 40
    else:
        cost = many * 100
    print(many, 'pairs of', size, style, 'pants: $', cost)

    return None

def digdug(num):
    '''
    This function prints a list of numbers divisible by
    3 and 5 based on given number

    Parameters---
    num: number to check (int)

    Return: none
    '''
    for i in range(1, num+1):
        if((i%3 == 0) & (i%5 == 0)):
            print(i,': digdug')
        elif(i%3 == 0):
            print(i, ': dig')
        elif(i%5 == 0):
            print(i, ': dug')
    return None

def beef_type(percent_lean):
    '''
    This function determines beef type based on
    percent lean

    Parameters---
    percent_lean: percentage in decimal (float)

    Return: type of beef (string)
    '''
    if(percent_lean < 78):
        result = 'Hamburger'
    elif((percent_lean < 85) & (percent_lean >= 78)):
        result = 'Chuck'
    elif((percent_lean < 90) & (percent_lean >= 80)):
        result = 'Round'
    elif((percent_lean <= 95) & (percent_lean >= 90)):
        result = 'Sirloin'
    else: result = 'Unknown'
    return result

def species_height(str, height):
    '''
    This function determines how tall you are
    compared to others in your species

    Parameters---
    str: species (string)
    height: height in inches (float)

    Return: none
    '''
    if(str == 'Human'):
        if(height > 67.0):
            print('Above Average')
        elif(height < 67.0):
            print('Below Average')
        else:
            print('Average')
    else:
        if(height > 71.0):
            print('Above Average')
        elif(height < 71.0):
            print('Below Average')
        else:
            print('Average')
    return None

def sooner_date(m1, d1, m2, d2):
    '''
    This function prints out the date that comes first

    Parameters---
    m1: number of first month (int)
    d1: number of first day (int)
    m2: number of second month (int)
    d2: number of second day (int)

    Return: none
    '''
    if(m1 < m2):
        print(m1, '/', d1)
    elif(m1 > m2):
        print(m2, '/', d2)
    else:
        if(d1 < d2):
            print(m1, '/', d1)
        else:
            print(m2, '/', d2)
    return None


def main():
    '''
    This file calls the above functions to test and troubleshoot
    '''

    #Testing my functions
    #testing word_length
    '''word_length('liversnaps', 7)
    word_length('earwax', 5)
    word_length('chickenfat',10)
    word_length('Gross!', 13)'''

    #testing stop_light
    '''print(stop_light('green', 61))
    print(stop_light('yellow', 5))
    print(stop_light('yellow', 6))
    print(stop_light('red', 12))
    print(stop_light('red', 56))'''

    #testing is_normal_blood_pressure
    '''print(is_normal_blood_pressure(120,80))
    print(is_normal_blood_pressure(119,80))
    print(is_normal_blood_pressure(119,79))
    print(is_normal_blood_pressure(120,79))'''

    #testing doctor
    '''doctor()'''

    #testing pants_size
    '''print(pants_size(38))
    print(pants_size(34))
    print(pants_size(33))
    print(pants_size(29))
    print(pants_size(-20))
    print(pants_size(2000))'''

    #testing pants_fitter
    '''pants_fitter()'''

    #testing dig_dug
    '''digdug(2)
    digdug(3)
    digdug(5)
    digdug(15)'''

    #testing beef_type
    '''print(beef_type(91.2))
    print(beef_type(78))
    print(beef_type(87))
    print(beef_type(95.1))'''

    #testing species_height
    '''species_height('Human', 62.1)
    species_height('Klingon', 73)
    species_height('Klingon', 71)
    species_height('Human', 67)'''

    #testing sooner_date
    '''sooner_date(1, 1, 1, 2)
    sooner_date(2, 5, 1, 3)
    sooner_date(8, 25, 7, 30)'''



if __name__ == '__main__':
    main()

