"""
@created: 6.12.2018
@author: Jan Lenk

@py_version: 3.6
"""

from os.path import isfile
import numpy as np
import nltk

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
        return [d.split('\n')[0] for d in id.readlines() if not d == '\n']


def count_occurence(values):
    '''
    find the first value that is reached twice

    :param values: value list
    :return: value that is reached twice first
    '''
    c_2 = 0
    c_3 = 0
    # iterate all words
    for val in values:
        # create dictionary over the occurence of every single letter
        unique, counts = np.unique(np.array([list(val)]), return_counts=True)
        occurence = dict(zip(unique, counts))

        count_2 = 0
        count_3 = 0
        # iterate dictionary
        for v in occurence.values():
            # increase count if one is 2
            if v == 2 and count_2 == 0:
                count_2 += 1
            # or if one is 3
            elif v == 3 and count_3 == 0:
                count_3 += 1
        # increase general count
        c_2 += count_2
        c_3 += count_3
    # return the checksum
    return c_2*c_3


def get_common_letters(values):
    '''
    find the lowest edit distance and get similarity

    :param values: list of words
    :return: string containing the similarities
    '''
    distance = None
    id1, id2 = None, None
    # calculate all distances
    for i, w_id1 in enumerate(values):
        for w_id2 in values[i+1:]:
            # since the pre condition was that just one pair has a distance of one
            # cut the computational time and stop if that pair is found
            distance = nltk.edit_distance(w_id1, w_id2)
            if distance == 1:
                id1, id2 = w_id1, w_id2
                break
        if distance == 1:
            break
    # convert the string to list
    id1_list = list(id1)
    # compare the two strings
    for i, (id_letter1, id_letter2) in enumerate(zip(id1_list, list(id2))):
        if not id_letter1 == id_letter2:
            # and replace the differential character
            id1_list[i] = ''
            return ''.join(id1_list)
    return None


if __name__ == '__main__':
    # read the data and sum up the list
    print('Part 1:\n')
    print(count_occurence(read_data()))
    print('Part 2:\n')
    print(get_common_letters(read_data()))
