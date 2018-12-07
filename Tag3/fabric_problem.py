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
        fabric_list = [d.split('\n')[0].split('@')[1] for d in id.readlines() if not d == '\n']
        return [tuple(f.split(':')[0].split(',')) + tuple(f.split(': ')[1].split('x')) for f in fabric_list]


def count_sqaure_inches_overlapping(values):
    '''
    count the square inches that are claimed by two or more teams

    :param values: value list
    :return: square inches (int)
    '''
    # build the fabric 1000x1000
    fabric = np.zeros((1000, 1000))
    for (col, row, w, t) in values:
        # for every claim add one to the matrix
        fabric[int(row): int(row) + int(t), int(col): int(col) + int(w)] += 1
    # sum over all values that are greater than one
    # these are the ones with more than one claim
    return (fabric > 1).sum()


def get_non_overlapping(values):
    '''
    which claim does not overlapp

    :param values: value list
    :return: int containing the claim number
    '''
    # build the fabric 1000x1000
    fabric = np.zeros((1000, 1000))
    for (col, row, w, t) in values:
        # for every claim add one to the matrix
        fabric[int(row): int(row) + int(t), int(col): int(col) + int(w)] += 1
    for i, (col, row, w, t) in enumerate(values):
        if np.sum(fabric[int(row): int(row) + int(t), int(col): int(col) + int(w)] - 1) == 0:
            return i+1


if __name__ == '__main__':
    # read the data and sum up the list
    print('Part 1:\n')
    print(count_sqaure_inches_overlapping(read_data()))
    print('Part 2:\n')
    print(get_non_overlapping(read_data()))
