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
        tmp_dat = [d.split('\n')[0] for d in id.readlines() if not d == '\n']
        return [[d.split(' ')[1], d.split(' ')[-3]] for d in tmp_dat]


def assembly(data):
    '''
    assembly instructions

    :param data: given data als list
    :return: largest area size
    '''
    before_x = []
    assem_dat = {}
    for line in data:
        if line[0] in assem_dat.keys():
            assem_dat[line[0]].append(line[1])
        else:
            assem_dat[line[0]] = [line[1]]
        before_x.append(line[1])
    before_x = set(before_x)
    x_before = set(assem_dat.keys())
    diff_before = x_before.difference(before_x)
    done = []
    work_list = sorted(list(diff_before))
    while len(work_list) > 0:
        curr_item = work_list[0]
        work_list.remove(curr_item)
        done.append(curr_item)
        check = set(assem_dat[curr_item])
        for el in work_list:
            check =
        if curr_item in assem_dat.keys():
            work_list.extend(assem_dat[curr_item])
        work_list = sorted(list(set(work_list)))
        print(work_list)

    print(done)




if __name__ == '__main__':
    # read the data and sum up the list
    print('Part 1:\n')
    print(assembly(read_data()))
    print('Part 2:\n')
    #print(improving_the_polymer(read_data()))
