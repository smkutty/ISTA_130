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

    hold = this_list.copy()
    hold.append(mammal)
    hold.sort()
    position = hold(mammal)

    return position

def populate_lists(names, body_weights, brains):
    text = open('BrainBodyWeightKilos.csv', 'r')
    mylist = []
    for line in text:
        hold = [line.split(',')]
        mylist.append(hold)
    for i in range(len(mylist)):
        names.append(mylist[i][0])
        body_weights.append(mylist[i][1])
        brains.append(mylist[i][2])
    text.close()
    return None

def write_converted_csv(fname, mammals, weights_kg, brains_g):
    text = open(fname, 'w')
    for i in range (len(mammals)):
        weight_lbs = round(weights_kg[i] * 2.205, 2)
        brains_lbs = round(brains_g[i] * 0.0022, 2)
        myline = mammals[i].upper() + ', ' + weight_lbs + ', ' + brains_lbs
        text.write(myline)
    text.close()
    return None



def main():
    '''
    This file calls the above methods to create a madlib
    '''

    #Set up for user
    my_names = []
    my_bw = []
    my_brains = []
   



if __name__ == '__main__':
    main()

