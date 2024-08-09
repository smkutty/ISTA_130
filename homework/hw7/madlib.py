'''
Author: Sreelakshmi Kutty
Date: 7 November 2023
Class: ISTA 130
Section Leader: Huy Tran

Description:
Homework 7 > String Manipulation, File Reading, and Writing
Creating a Mad Lib using string functions
'''

# Import packages
import math

# My 3 functions

def print_report(file_name):
    '''
    This method prints a report of a text file's character summary

    Parameters---
    file_name: (string) name of file

    Return: none
    '''
    v, cons, blanks, puncs, total = 0, 0, 0, 0, 0 #initialize variables
    vowels = 'aeiouAEIOU'
    consonants = 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ'

    f = open(file_name, 'r') #open file
    for line in f:
        for ch in line:
            total += 1
            if(ch in vowels): #conditions to check
                v+=1
            elif(ch in consonants):
                cons+=1
            elif(ch.isspace() or ch == '\t' or ch == '\n'):
                blanks+=1
            else: puncs+=1
    f.close()  #close file

    v_per = round((v/total)*100, 1) #calculate percentages
    cons_per = round((cons/total)*100, 1)
    blanks_per = round((blanks/total)*100, 1)
    puncs_per = round((puncs/total)*100, 1)

    #printing table of informatino ---------------------------
    print('\n' + file_name.center(25, '-'))
    print('Vowels: '.ljust(24-len(str(v))), v)
    print('Consonants: '.ljust(24-len(str(cons))), cons)
    print('Whitespace: '.ljust(24-len(str(blanks))), blanks)
    print('Punctuation: '.ljust(24-len(str(puncs))), puncs)
    print('-'*25)
    print('Total: '.ljust(24-len(str(total))), total, '\n')
    print('Percent vowels: '.ljust(24-len(str(v_per))), v_per)
    print('Percent consonants: '.ljust(24-len(str(cons_per))), cons_per)
    print('Percent spaces: '.ljust(24-len(str(blanks_per))), blanks_per)
    print('Percent punctuation: '.ljust(24-len(str(puncs_per))), puncs_per)
    print('='*25)
    #-----------------------------------------------------------

    return None

def replace_parts_of_speech(line_name, part):
    '''
    This method replaces a word(s) based on given part of speech--
    takes user input to replace word

    Parameters---
    line_name: (string) line to parse and replace
    part: (string) part of speech

    Return: (string) line with repalced word(s)
    '''
    count = line_name.count(part)
    for i in range(count):
        entry = input('Enter ' + part.lower() + ': ') #get user input
        line_name = line_name.replace(part, entry, 1)
    return line_name

def complete_mad_lib(filename):
    '''
    This method complete a given madlib-- opens specified file,
    asks for user input, replaces lines, writes to a new file with
    completed text

    Parameters---
    filename: (string) name of file to open

    Return: none
    '''
    all_parts = ['PLURAL NOUN', 'VERB PAST', 'VERB', 'NOUN', 'ADJECTIVE'] #create a list of parts of speech
    text = open(filename, 'r') #open file to read and create new file
    new_name = 'MAD_' + filename 
    mad_text = open(new_name, 'w')
    for line in text: #parse through each line and part of speech
        for item in all_parts:
            line = replace_parts_of_speech(line, item) #use previous method to replace words
        mad_text.write(line) #write to new file
    text.close()
    mad_text.close()
    return None



def main():
    '''
    This file calls the above methods to create a madlib
    '''

    #Set up for user
    story = input("Enter file name: ")
    print_report(story)
    complete_mad_lib(story)
    




if __name__ == '__main__':
    main()

