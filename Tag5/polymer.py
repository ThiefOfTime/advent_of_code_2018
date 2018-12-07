"""
@created: 6.12.2018
@author: Jan Lenk

@py_version: 3.6
"""

from os.path import isfile
import numpy as np


def read_data(data_path='input.txt'):
    '''
    read the input and convert to int

    :param data_path: path to input file
    :return: list of given input
    '''
    # check if path is valid
    if data_path is None or data_path == '' or not isfile(data_path):
        data_path = 'input.txt'
    # open the file, read the lines and remove the \n
    with open(data_path, 'r') as id:
        return [d.split('\n')[0]for d in id.readlines() if not d == '\n'][0]


def react_polymer(data):
    '''
    fully react the given polymer

    :param data: given data als list
    :return: remaining polymer length
    '''
    # convert the data to a list
    polymer_list = list(data)
    count = 0
    check = True
    while check:
        tmp_count = count
        # check every element and its neighbour
        for i, elem1 in enumerate(polymer_list[:-1]):
            elem2 = polymer_list[i+1]
            # if two elements match they have the same polarity
            if elem1 == elem2:
                continue
            elif elem1.lower() == elem2.lower():
                # if they match while they are lowered then they have different polarities and have the same type
                polymer_list_tmp = polymer_list[:i]
                polymer_list_tmp.extend(polymer_list[i+2:])
                # remove from list
                polymer_list = polymer_list_tmp
                tmp_count += 1
                break
        # if no more pairs are found stop
        if count == tmp_count:
            check = False
        count = tmp_count
    return len(polymer_list)


def improving_the_polymer(data):
    """
    search for the best improvement

    :param data: given data
    :return: best polymer length
    """
    # build polymer set
    polymer = data
    # lower the polymer string
    polymer_low = data.lower()
    # build a set of used letters
    polymer_set = set(list(polymer_low))
    best_polymer_length = None
    for elem in polymer_set:
        # for every character test
        polymer_tmp = polymer
        # first replace lower case letters
        polymer_tmp = polymer_tmp.replace(elem, '')
        # next replace upper case letters
        polymer_tmp = polymer_tmp.replace(elem.upper(), '')
        # react the new polymer
        len_tmp = react_polymer(polymer_tmp)
        if best_polymer_length is None or len_tmp < best_polymer_length:
            # if the length is better or there is by now no best length update
            best_polymer_length = len_tmp
    return best_polymer_length


if __name__ == '__main__':
    # read the data and sum up the list
    print('Part 1:\n')
    print(react_polymer(read_data()))
    print('Part 2:\n')
    print(improving_the_polymer(read_data()))
