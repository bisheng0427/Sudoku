#!/usr/bin/python3

suduko = {}
num_range = list(range(1, 10))
suduko_size = 9

# initialize question into list
with open('questions.txt', 'r') as question:
    index = 0
    temp = []
    for line in question:
        if line != '\n':
            row = []
            for each in line.rstrip('\n').split(' '):
                row.append(int(each))
            temp.append(row)
        else:
            suduko['suduko%i' % index] = temp.copy()
            temp.clear()
            index += 1
        suduko['suduko%i' % index] = temp
print(suduko.keys())
print(suduko.items())


def init_answer():
    for keys in suduko.keys():
        answer[keys] = suduko[keys].copy()
        for r in range(suduko_size):
            for c in range(suduko_size):
                if answer[keys][r][c] == 0:
                    answer[keys][r][c] = num_range.copy()
                else:
                    answer[keys][r][c] = [suduko[keys][r][c]]

    return


def exclude_by_row(suduko_name, r, c):
    for colume in range(suduko_size):
        try:
            answer[suduko_name][r][c].remove(suduko[suduko_name][r][colume])
        except ValueError:
            print('Oww!')
    return


def exclude_by_colume(suduko_name, r, c):
    for row in range(suduko_size):
        try:
            answer[suduko_name][r][c].remove(suduko[suduko_name][row][c])
        except ValueError:
            print('Oww!')
    return

answer = {}
# print(num_range)
init_answer()
for i in range(suduko_size):
    for j in range(suduko_size):
        exclude_by_row('suduko0', i, j)
        exclude_by_colume('suduko0', i, j)
print(answer['suduko0'])

