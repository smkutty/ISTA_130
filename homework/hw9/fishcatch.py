'''
Author: Sreelakshmi Kutty
Date: 27 November 2023
Class: ISTA 130
Section Leader: Huy Tran

Description:
Homework 9 > Dictionaries with Lists as Values
Part 1 - Fish Dictionary
'''


def fish_dict_from_file(fname):
    '''
    This function reads a given file and sorts data into dictionary

    Parameters---
    fname: (str) name of file to read

    Return: (dict) dictionary
    '''
    #create name key
    fishmap = {1: 'Bream', 2: 'Whitefish', 3: 'Roach', 4: '?', 5: 'Smelt', 6: 'Pike', 7: 'Perch'}

    my_dict = {}
    text = open(fname, 'r')
    for line in text: #traverse file by line
        temp_list = line.split()
        if(temp_list[2] != 'NA'): #skip NAs
            species_num = int(temp_list[1])
            weight = float(temp_list[2])
            name = fishmap[species_num]
            if species_num in fishmap:
                if name not in my_dict:
                    my_dict.update({name: [weight]})
                else:
                    my_dict[name].append(weight)
    text.close()

    return my_dict

def sort_this(mydict):
    '''
    This is a helper function to sort a dictionary by key

    Parameters---
    mydict: (dict) dictionary to sort

    Return: (dict) sorted dictionary
    '''
    sorted_dict = {}
    these_keys = sorted(mydict) #gets list of sorted keys
    for item in these_keys:
        sorted_dict.update({item: mydict[item]}) #adding items in order
    return sorted_dict




def main():
    '''
    This file prints a report of data from given file
    '''
    
    #reading file and sorting
    fishes = fish_dict_from_file('fishcatch.dat')
    fishes = sort_this(fishes)

    x = fishes.keys()
    
    print('#'.rjust(4), 'NAME'.ljust(10), 'MEAN WT'.rjust(10))
    for item in x:
        num = len(fishes.get(item))
        mean = round((sum(fishes.get(item))/num), 1)
        mean_wt = str(mean) + 'g'
        print(str(num).rjust(4), item.ljust(10), mean_wt.rjust(10))


    


if __name__ == '__main__':
    main()

