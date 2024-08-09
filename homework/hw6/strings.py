'''
Author: Sreelakshmi Kutty
Date: 1 November 2023
Class: ISTA 130
Section Leader: Huy Tran

Description:
Homework 6 > Strings and File I/O
This file shows the use of string and file functions
'''

# Import packages
import math

# My 8 functions

def US_to_EU(US_date):
    '''
    This function converts a US date to EU date format

    Parameters---
    date: (string) date in US format

    Return: (string) date in EU format
    '''
    num_lst = US_date.split('/')
    EU_date = num_lst[1] + '.' + num_lst[0] + '.' + num_lst[2]
    return EU_date

def is_phone_num(phone):
    '''
    This function checks phone number format

    Parameters---
    date: (string) phone number

    Return: (bool) if number is in correct format
    '''
    final = False
    lst = phone.split('-') #split by -
    if(len(lst) == 3):
        if(lst[0].isdigit() and len(lst[0]) == 3):
            if(lst[1].isdigit() and len(lst[1]) == 3):
                if(lst[2].isdigit() and len(lst[2]) == 4):
                    final = True
    return final

def redact_line(str):
    '''
    This function redacts phone numbers

    Parameters: (string) a line of text

    Return: (string) text with redacted number

    **THIS FUNCTION IS NOT MY OWN. IT WAS TAKEN FROM ISTA 130
    HW6 INSTRUCTION GUIDE PAGE 3**
    '''
    for i in range(len(str) - 12): #just lots of conditionals
        if(((i == 0) or (str[i-1] == ' ')) and (str[i+12] in ' \n') and (is_phone_num(str[i:i + 12]))):
            str = str[:i] + str[i:].replace(str[i:i + 12], "XXX-XXX-XXXX", 1)
    return str

def redact_file(original):
    '''
    This function redacts phone numbers in a given file

    Parameters: (string) original file name

    Return: (string) new file name
    '''
    file_lst = original.split('.') #open original file and create new name
    new_name = file_lst[0] + '_redacted.txt'
    text_file = open(original, 'r')
    text_redacted = open(new_name, 'w') #create new file for redacted
    for line in text_file:
        text_redacted.write(redact_line(line)) #use redact_line method
    text_file.close()
    text_redacted.close()
    return new_name

def plagiarism(file1, file2):
    '''
    This function checks for plagiarism

    Parameters---
    file1: (string) file 1 name
    file2: (string) file 2 name

    Return: (bool) if plagiarism is found
    '''
    text1 = open(file1, 'r')
    for line1 in text1: #going through each line file1
        text2 = open(file2, 'r')
        for line2 in text2:
            if(line1 == line2): #comparing lines
                return True
        text2.close()
    return False

def count_word(file_name, key_word):
    '''
    This function conuts the frequency of word in a file

    Parameters---
    file_name: (string) name of file to look through
    key_word: (string) word to find

    Return: (num) frequency of word
    '''
    count = 0
    text_file = open(file_name, 'r')
    for line in text_file:
        if key_word in line:
            new_line = line.split() #splitting line into a list
            for i in range(len(new_line)): #traverse each item in list
                if(new_line[i].find(key_word) > -1): #only looking if word is in item, doesn't matter where
                    count += 1
    return count



def main():
    '''
    This file calls the above functions to test and troubleshoot
    '''

    #Testing my functions
    #Testing US_to_EU
    print(US_to_EU('3/13/18'))
    print(US_to_EU('03/13/2018'))

    #Testing is_phone_num
    print(is_phone_num('123-456-7890'))
    print(is_phone_num('123-4556-7890'))
    print(is_phone_num('(123)4556-7890'))

    #Testing Redact_Line
    print(redact_line('123-456-7890 is the numeber'))
    print(redact_line('hello 123-456-7890 '))

    print(count_word('highlight_in.txt', 'Rocket'))




if __name__ == '__main__':
    main()

