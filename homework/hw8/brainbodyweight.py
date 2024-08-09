'''
Author: Sreelakshmi Kutty
Date: 15 November 2023
Class: ISTA 130
Section Leader: Huy Tran

Description:
Homework 8 > Lists and File I/O
Read and write files with lists
'''


# My 3 functions

def find_insert_position(mammal, this_list):
    '''
    This function finds the alphabetic order position
    of a word to insert in a list

    Parameters---
    mammal: (str) name of mammal
    this_list: (list) list to insert into

    Return: (int) position of would be insertion
    '''
    hold = this_list.copy()
    hold.append(mammal)
    hold.sort()
    position = hold.index(mammal)

    return position

def populate_lists(names, body_weights, brains):
    '''
    This function populates given lists with data from file

    Parameters---
    names: (list) list of mammal names
    body_weights: (list) list of body weights
    brains: (list) list of brains

    Return: none
    '''
    text = open('BrainBodyWeightKilos.csv', 'r')
    mylist = []
    for line in text:
        hold = line.split(',')
        mylist.append(hold)
    for i in range(len(mylist)):
        names.append(mylist[i][0].title())
        body_weights.append(float(mylist[i][1]))
        reform = float(mylist[i][2].strip())
        brains.append(reform)
    text.close()
    return None

def write_converted_csv(fname, mammals, weights_kg, brains_g):
    '''
    This function converts a given csv into lists

    Parameters---
    fname: (str) name of file
    mammals: (list) list of mammal names
    weights_kg: (list) list of weights in kg
    brains_g: (list) list of brain weights in g

    Return: none
    '''
    text = open(fname, 'w')
    for i in range (len(mammals)):
        weight_lbs = str(round(float(weights_kg[i]) * 2.205, 2))
        brains_lbs = str(round(float(brains_g[i]) * 0.0022, 2))
        myline = mammals[i].title() + ',' + weight_lbs + ',' + brains_lbs
        text.write(myline)
        text.write('\n')
    text.close()
    return None



def main():
    '''
    This file creates a file from user input
    '''

    #Set up for user
    my_names = []
    my_bw = []
    my_brains = []
    
    populate_lists(my_names, my_bw, my_brains)

    # For my own testing
    #my_names = ['Lion', 'Badger', 'Eagle', 'Snake']
    #my_bw = [200.0, 50.89, 48.4, 15.8]
    #my_brains = [30.1, 21.3, 10.5, 2.5]

    while(True):
        animal = input('\nEnter animal name (or "q" to quit): ')
        animal = animal.title()
        if(animal not in my_names):
            if(animal == 'q' or animal == 'Q'):
                write_converted_csv('BrainBodyWeightPounds.csv', my_names, my_bw, my_brains)
                break
            print('File does not contain "' + animal + '".')
            response = input('Add "' + animal + '" to file? (y|n) ')
            if(response == 'y'):
                weight = input('Enter body weight for "' + animal + '" in kilograms: ')
                brain = input('Enter brain weight for "' + animal + '" in grams: ')
                my_names.append(animal)
                my_names.sort()
                position = my_names.index(animal)
                my_bw.insert(position, weight)
                my_brains.insert(position, brain)
        else:
            pos = my_names.index(animal)
            this_bw = str(my_bw[pos])
            this_brain = str(my_brains[pos])
            print(animal + ': body = ' + this_bw + ', brain =', this_brain)
            delete = input('Delete "' + animal + '"? (y|n) ')
            if(delete == 'y'):
                pos = my_names.index(animal)
                my_names.pop(pos)
                my_bw.pop(pos)
                my_brains.pop(pos)


if __name__ == '__main__':
    main()

