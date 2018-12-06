"""
@created: 6.12.2018
@author: Jan Lenk

@py_version: 3.6
"""

from os.path import isfile


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
    with open(data_path, 'r') as freq:
        return [int(d.split('\n')[0]) for d in freq.readlines() if not d == '\n']


def find_first_twice_val(values):
    '''
    find the first value that is reached twice

    :param values: value list
    :return: value that is reached twice first
    '''
    # catch the extreme case
    if values is None or len(values) == 0:
        return None
    value_list = [0]
    # go through the values list
    while True:
        for val in values:
            # calculate the new value
            new_val = value_list[-1] + val
            # if value is already in list great
            if new_val in value_list:
                return new_val
            # else append and continue
            value_list.append(new_val)


if __name__ == '__main__':
    # read the data and sum up the list
    print('Part 1:\n')
    print(sum(read_data()))
    print('Part 2:\n')
    print(find_first_twice_val(read_data()))
