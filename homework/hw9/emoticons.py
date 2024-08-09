'''
Author: Sreelakshmi Kutty
Date: 27 November 2023
Class: ISTA 130
Section Leader: Huy Tran

Description:
Homework 9 > Dictionaries with Lists as Values
Part 2 - Emoticon Dictionary
'''


def load_twitter_dicts_from_file(filename, emoticons_to_ids, ids_to_emoticons):
    '''
    This function reads a file and sorts data into the appropriate
    given dictionaries

    Parameters---
    filename: (str) name of file to read
    emoticons_to_ids: (dict) where to sort data by emoticon as key
    ids_to_emoticons: (dict) where to sort data by id as key

    Return: none
    '''
    text = open(filename, 'r')
    for line in text:
        hold = line.split()
        emote = hold[0].replace('"', '') #remove quotes
        user = hold[2].replace('"', '')
        #check if emoticon already in dictionary
        if emote not in emoticons_to_ids:
            emoticons_to_ids.update({emote: [user]})
        else:
            emoticons_to_ids[emote].append(user)
        #check if id already in dictionary
        if user not in ids_to_emoticons:
            ids_to_emoticons.update({user: [emote]})
        else:
            ids_to_emoticons[user].append(emote)
    text.close()
    return None



def find_most_common(this_dict):
    '''
    This function finds the most common emoticon

    Parameters---
    this_dict: (dict) dictionary to parse

    Return: (key) emoticon
    '''
    length = 0
    emo_key = ''
    for item in this_dict: #traverse dictionary
        if len(this_dict[item]) > length:  #item is the list
            length = len(this_dict[item])
            emo_key = item
    emo_key = emo_key.replace('"', '') #remove quotes

    print(emo_key.ljust(20), 'occurs', str(length).rjust(8), 'times')
    return emo_key




def main():
    '''
    This file analyses the given file using the above functions
    '''
    
    #set up empty dictionaries
    emoticons_to_ids = {}
    ids_to_emoticons = {}

    #use functions to analyse
    load_twitter_dicts_from_file('twitter_emoticons.dat', emoticons_to_ids, ids_to_emoticons)
    total_emos = len(emoticons_to_ids)
    print('Emoticons:', total_emos)
    total_users = len(ids_to_emoticons)
    print('UserIDs:  ', total_users, '\n')

    for i in range(5):
        temp = find_most_common(emoticons_to_ids)
        emoticons_to_ids.pop(temp)

    


if __name__ == '__main__':
    main()

