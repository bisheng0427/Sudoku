#!/usr/bin/python3
import copy
import datetime

SUDUKO = {}
SUDUKO_SIZE = 9
NUM_RANGE = list(range(1, 10))
ORIGIN = {}
ANSWER = {}
# Initialize question into SUDUKO{}
# SUDUKO[key] is a list[][]
# SUDUKO{} contains the questions, query one by select SUDUKO[suduko%i % number]
# ORIGIN{} like suduko. If ORIGIN[key][][] = 1, means this was set in question
with open('questions.txt', 'r') as question:
    index = 0
    temp = []
    row = []
    for line in question:
        if line != '\n':
            for each in line.rstrip('\n').split(' '):
                row.append(int(each))
            temp.append(row.copy())
            row.clear()
        else:
            SUDUKO['suduko%i' % index] = temp.copy()
            temp.clear()
            row.clear()
            index += 1
        SUDUKO['suduko%i' % index] = temp.copy()


def init_answer():
    for key in SUDUKO.keys():
        ORIGIN[key] = []
        ANSWER[key] = copy.deepcopy(SUDUKO[key])
        for r in range(SUDUKO_SIZE):
            ORIGIN[key].append([])
            for c in range(SUDUKO_SIZE):
                if ANSWER[key][r][c] == 0:
                    ORIGIN[key][r].append(0)
                    ANSWER[key][r][c] = NUM_RANGE.copy()
                else:
                    ORIGIN[key][r].append(1)
                    ANSWER[key][r][c] = [SUDUKO[key][r][c]]
    return


def print_matrix(dic, key):
    for i in dic[key]:
        print(i)
    return


def read_row(suduko_name, row):
    value_list = set()
    for column in range(SUDUKO_SIZE):
        value_list.update(str(SUDUKO[suduko_name][row][column]))
    print(value_list)
    return


def read_column(suduko_name, column):
    value_list = set()
    for row in range(SUDUKO_SIZE):
        value_list.update(str(SUDUKO[suduko_name][row][column]))
    print(value_list)
    return


def read_square(suduko_name, r, c):
    square_size = 3  # TODO: update it for further questions
    square0 = []
    if ORIGIN[suduko_name][r][c] == 1:
        print('Skip this one')
    else:
        count = 0
        for row in range(SUDUKO_SIZE):
            try:
                ANSWER[suduko_name][r][c].remove(SUDUKO[suduko_name][row][c])
            except ValueError:
                print('ValueError!')
            except AttributeError:
                print('AttributeError')
    return


def main():
    # start_time = datetime.datetime.now()
    # init_answer()
    # print_matrix(SUDUKO, 'suduko0')
    # print_matrix(ANSWER, 'suduko0')
    # print_matrix(ORIGIN, 'suduko0')
    # for r in range(SUDUKO_SIZE):
    #     for c in range(SUDUKO_SIZE):
    #         read_row('suduko0', r, c)
    #         read_column('suduko0', r, c)
    # print_matrix(ANSWER, 'suduko0')
    # end_time = datetime.datetime.now()
    # delta = end_time - start_time
    # print(delta)
    print("Read by row:")
    for i in range(SUDUKO_SIZE):
        read_row('suduko0', i)
    print("Read by column:")
    for i in range(SUDUKO_SIZE):
        read_row('suduko0', i)


if __name__ == '__main__':
    main()
# print_matrix(ANSWER['suduko0'])
