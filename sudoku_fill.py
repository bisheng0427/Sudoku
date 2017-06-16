#!/usr/bin/python3
import copy
import datetime

SUDOKU = {}
SUDOKU_SIZE = 9
NUM_RANGE = [str(x) for x in range(1, 10)]
ORIGIN = {}
ANSWER = {}
# Initialize question into SUDOKU{}
# SUDOKU[key] is a list[][]
# SUDOKU{} contains the questions, query one by select SUDOKU[SUDOKU%i % number]
# ORIGIN{} like SUDOKU. If ORIGIN[key][][] = 1, means this was set in question
with open('questions.txt', 'r') as question:
    index = 0
    temp = []
    row = []
    for line in question:
        if line != '\n':
            for each in line.rstrip('\n').split(' '):
                row.append(each)
            temp.append(row.copy())
            row.clear()
        else:
            SUDOKU['sudoku%i' % index] = temp.copy()
            temp.clear()
            row.clear()
            index += 1
        SUDOKU['sudoku%i' % index] = temp.copy()


def init_answer():
    for key in SUDOKU.keys():
        ORIGIN[key] = []
        ANSWER[key] = copy.deepcopy(SUDOKU[key])
        for r in range(SUDOKU_SIZE):
            ORIGIN[key].append([])
            for c in range(SUDOKU_SIZE):
                if ANSWER[key][r][c] == '0':
                    ORIGIN[key][r].append('0')
                    ANSWER[key][r][c] = NUM_RANGE.copy()
                else:
                    ORIGIN[key][r].append('1')
                    ANSWER[key][r][c] = [SUDOKU[key][r][c]]
    return


def print_matrix(dic):
    for i in dic:
        print(i)
    return


def read_row(sudoku_name, row):
    value_list = set()
    for column in range(SUDOKU_SIZE):
        value_list.update(str(SUDOKU[sudoku_name][row][column]))
    return value_list


def read_column(sudoku_name, column):
    value_list = set()
    for row in range(SUDOKU_SIZE):
        value_list.update(str(SUDOKU[sudoku_name][row][column]))
    return value_list


def read_square(sudoku_name, r, c):
    square = []
    square_r = []
    square_c = []
    value_list = set()
    for i in range(0, len(NUM_RANGE), 3):
        square.append(NUM_RANGE[i:i+3])
    for i in range(3):
        if r in square[i]:
            square_r = square[i]
        if c in square[i]:
            square_c = square[i]
    for i in square_c:
        for j in square_r:
            value_list.update(str(SUDOKU[sudoku_name][i][j]))
    return value_list


def check_cell(sudoku_name, r, c):
    value_list = NUM_RANGE.copy()
    rr = read_row(sudoku_name, r)
    rc = read_column(sudoku_name, c)
    rs = read_square(sudoku_name, r, c)
    exclude_set = rr | rc | rs
    print(rr)
    print(rc)
    print(rs)
    print(exclude_set)
    for each in exclude_set:
        try:
            value_list.remove(each)
        except ValueError:
            print('VE')
    return value_list



def main():
    # start_time = datetime.datetime.now()
    # init_answer()
    # print_matrix(SUDOKU, 'sudoku0')
    # print_matrix(ANSWER, 'sudoku0')
    # print_matrix(ORIGIN, 'sudoku0')
    # for r in range(SUDOKU_SIZE):
    #     for c in range(SUDOKU_SIZE):
    #         read_row('sudoku0', r, c)
    #         read_column('sudoku0', r, c)
    # print_matrix(ANSWER, 'sudoku0')
    # end_time = datetime.datetime.now()
    # delta = end_time - start_time
    # print(delta)
    init_answer()
    print(SUDOKU['sudoku0'][1][2])
    for i in range(9):
        for j in range(9):
            if ORIGIN['sudoku0'][i][j] == '1':
                pass
            else:
                ANSWER['sudoku0'][i][j] = check_cell('sudoku0', i, j)
    print_matrix(ANSWER['sudoku0'])

if __name__ == '__main__':
    main()
# print_matrix(ANSWER['sudoku0'])
