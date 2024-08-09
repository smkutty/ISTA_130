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
    print('Enter your systolic reading:')
    sys = int(input())
    print('Enter your diastolic reading:')
    dias = int(input())
    result = is_normal_blood_pressure(sys, dias)
    if (result):
        print('Your blood presure is normal.')
    else: print('Your blood pressure is high')
    return None

def pants_size(size):
    result = ''
    if(size >= 34):
        result = 'large'
    elif(size >= 30):
        result = 'medium'
    else:
        result = 'small'
    return result

def pants_fitter():
    print('Enter your name:')
    name = input()
    print('Greetings', name, 'welcome to Pants-R-Us')
    print('Enter your waist size in inches:')
    waist = int(input())
    size = pants_size(waist)
    print('How many pairs of pants would you like:')
    many = int(input())
    print('Would you like regular or fancy pants?')
    style = input()
    if(style == 'regular'):
        cost = many * 40
    else:
        cost = many * 100
    print(many, 'pairs of', size, style, 'pants: $', cost)

    return None

def dig_dug(num):
    for i in range(1, num+1):
        if((i%3 == 0) & (i%5 == 0)):
            print(num,': digdug')
        elif(i%3 == 0):
            print(num, ': dig')
        elif(i%5 == 0):
            print(num, ': dug')
    return None

def beef_type(percent_lean):
    if(percent_lean < 78):
        result = 'Hamburger'
    elif((percent_lean < 85) & (percent_lean >= 78)):
        result = 'Chuck'
    elif((percent_lean < 90) & (percent_lean >= 80)):
        result = 'Round'
    elif((percent_lean < 95) & (percent_lean >= 90)):
        result = 'Sirloin'
    else: result = 'Unknown'
    return result

def species_height(str, height):
    if(str == 'human'):
        if(height > 67):
            print('Above Average')
        elif(height < 67):
            print('Below Average')
        else:
            print('Average')
    else:
        if(height > 71):
            print('Above Average')
        elif(height < 71):
            print('Below Average')
        else:
            print('Average')
    return None

def sooner_date(m1, d1, m2, d2):
    if(m1 < m2):
        print(m1, '/', d1)
    elif(m2 > m2):
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
    print('testing word_length')
    word_length('liversnaps', 7)
    word_length('earwax', 5)
    word_length('chickenfat',10)
    word_length('Gross!', 13)

    '''print('testing stop_light')
    print(stop_light('green', 61))
    print(stop_light('yellow', 5))
    print(stop_light('yellow', 6))
    print(stop_light('red', 12))
    print(stop_light('red', 56))'''

    '''print('testing is_normal_blood_pressure')
    print(is_normal_blood_pressure(120,80))
    print(is_normal_blood_pressure(119,80))
    print(is_normal_blood_pressure(119,79))
    print(is_normal_blood_pressure(120,79))'''

    '''print('testing doctor')
    doctor()'''

    '''print('testing pants_size')
    print(pants_size(38))
    print(pants_size(34))
    print(pants_size(33))
    print(pants_size(29))
    print(pants_size(-20))
    print(pants_size(2000))'''



if __name__ == '__main__':
    main()

