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
        return [d.split('\n')[0]for d in id.readlines() if not d == '\n']


def split_and_sort_data(data, part1=None):
    '''
    split and sort the given data

    The method is a bit over engineerd since I thought to complex. t

    :param data: given data als list
    :param part1: part of the task
    :return:
    '''
    if part1 is None:
        part1 = True

    # split the given dat
    data_list = []
    info_list = {}

    for i, line in enumerate(data):
        # draw all informations out of the input
        date, hour, info = line.split(' ', 2)
        info = info if '#' not in info else info.split('#')[1].split(' ')[0]
        date_o = date[1:].split('-')
        date = [int(d) for d in date_o]
        date = date[1:]
        hour_o = hour[:-1].split(':')
        hour = [int(h) for h in hour_o]
        # build a numpy array with the key of the corresponding dictionary
        data_list.append([0] + date + hour + [i])
        info_list[i] = info
    # convert to numpy
    data_list = np.array(data_list)

    # calc the minutes
    data_list = data_list[data_list[:, 1].argsort()]
    month_set = set(data_list[:, 1])
    max = 23 * 60 + 59
    min = 0 * 60
    max_time = max - min
    count = -1
    sorted_list = []
    c_shift_changes = len([f for f in info_list.values() if 'asleep' not in f and 'wakes' not in f])
    time_table = np.zeros((c_shift_changes, max_time + 1), dtype=np.int)
    # sort the list
    for month in month_set:
        data = data_list[:, :][data_list[:, 1] == month]
        days_set = set(data[:, 2])
        for day in days_set:
            day_data = data[:, :][data[:, 2] == day]
            day_data = day_data[:, 3:]
            day_data[:, 0] *= 60
            day_data[:, 0] += day_data[:, 1] - min
            day_data = day_data[day_data[:, 0].argsort()]
            start = 0
            end = 0
            for dat in day_data:
                info = info_list[dat[-1]]
                sorted_list.append([dat[0], info])

    start = 0
    # interpret the info
    for line in sorted_list:
        if 'asleep' in line[1]:
            start = line[0]
        elif 'wakes' in line[1]:
            time_table[count, start+1: line[0]+1] += 1
        else:
            count += 1
            time_table[count, 0] = int(line[1])
    if part1:
        # calc the maximal number of sleep time for each employee
        shifts = time_table[:, 0]
        shifts = np.array([shifts]).T
        time_slept = np.sum(time_table[:, 1:], axis=1)
        time_slept = np.array([time_slept])
        combi = np.concatenate((shifts, time_slept.T), axis=1)
        work_dic = {}
        for line in combi:
            if line[0] in work_dic.keys():
                work_dic[line[0]] += line[-1]
            else:
                work_dic[line[0]] = line[-1]
        # get the maximum value
        max = 0
        name = 0
        for k, v in work_dic.items():
            name = k if v > max else name
            max = v if v > max else max
        # get the minute he fall asleep most
        worker_most_sleep = time_table[:, 1:][combi[:, 0] == name]
        most_minute = np.sum(worker_most_sleep, axis=0)
        most_minute = np.argmax(most_minute)
    else:
        work_dic = {}
        for line in time_table:
            if line[0] in work_dic.keys():
                work_dic[line[0]] += line[1:]
            else:
                work_dic[line[0]] = np.copy(line[1:])

        time = 0
        max_num = 0
        name = 0
        for k, v in work_dic.items():
            max_n = np.max(v)
            if max_n >= max_num:
                max_num = max_n
                name = k
                time = np.argmax(v)
        most_minute = time
    return name * most_minute


if __name__ == '__main__':
    # read the data and sum up the list
    print('Part 1:\n')
    print(split_and_sort_data(read_data()))
    print('Part 2:\n')
    print(split_and_sort_data(read_data(), part1=False))
