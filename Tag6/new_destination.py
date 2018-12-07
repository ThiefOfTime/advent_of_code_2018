"""
@created: 6.12.2018
@author: Jan Lenk

@py_version: 3.6
"""

from os.path import isfile
import numpy as np


def read_data(data_path='t_input.txt'):
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
        return [d.split('\n')[0].split(', ') for d in id.readlines() if not d == '\n']


def get_largest_area(data):
    '''
    compute the largest area

    :param data: given data als list
    :return: largest area size
    '''
    coord_dict = {}
    coord_arr = []
    for i, line in enumerate(data):
        coord_dict[i+1] = (int(line[0]), int(line[1]))
        coord_arr.append([int(line[0]), int(line[1])])
    coord_arr = np.array(coord_arr)
    max_y = np.max(coord_arr[:, 0])
    max_x = np.max(coord_arr[1])
    universe = np.zeros((1000, 1000), dtype=np.int)
    for i, line in enumerate(universe):
        for j, col in enumerate(line):
            lowest_dist = None
            name = None
            for name, coord in coord_dict.items():
                dist = np.abs(i - coord[0]) + np.abs(j - coord[1])
                if lowest_dist is None or lowest_dist > dist:
                    lowest_dist = dist
                elif lowest_dist == dist:
                    break
            if lowest_dist is not None:
                universe[i, j] = lowest_dist
    print(universe)
    bin_t = np.bincount(universe.flatten())
    print(len(bin_t))


if __name__ == '__main__':
    # read the data and sum up the list
    print('Part 1:\n')
    print(get_largest_area(read_data()))
    print('Part 2:\n')
    #print(improving_the_polymer(read_data()))
