import itertools
import random
import time
from os import listdir

import numpy as np

from Interface import *


def Generate_grid(grid=None, I=None, J=None, N=None, A=None):
    if grid is None:
        grid = [[0 for x in range(9)] for y in range(9)]
        grid[random.randint(0, 8)][random.randint(0, 8)] = random.randint(1, 9)
        X = list(range(1, 10))
        random.shuffle(X)
        # fill the first 3x3 square of the grid with X
        for n in range(1, 4):
            random.shuffle(X)
            for j in range((n - 1) * 3, n * 3):
                for i in range((n - 1) * 3, n * 3):
                    grid[i][j] = [np.array_split(X, 3)[0].tolist(), np.array_split(X, 3)[1].tolist(),
                                  np.array_split(X, 3)[2].tolist()][i % 3][j % 3]
    return grid


#
# def Solve0(grid):
#     if not emptyCell(grid):
#         return True  # Board is filled
#     else:
#         y, x = emptyCell(grid)
#         for n in range(1, 10):
#             if isValid(grid, n, (y, x)):
#                 grid[y][x] = n
#                 if Solve0(grid):
#                     return True
#                 grid[y][x] = 0
#     return False

def limit_recursion(limit):
    def inner(func):
        func.count = 0

        def wrapper(*args, **kwargs):
            func.count += 1
            if func.count < limit:
                result = func(*args, **kwargs)
            else:
                print('Recursion limit reached')
                result = None
            func.count -= 1
            return result

        return wrapper

    return inner


def solve(grid):
    # Find next empty cell
    findEmpty = emptyCell(grid)

    if not findEmpty:
        return True  # Board is filled
    else:
        row, column = findEmpty

    for i in range(1, 10):
        if isValid(grid, i, (row, column)):
            grid[row][column] = i

            if solve(grid):
                return True

            grid[row][column] = 0
    return False


def isValid(board, num, pos):
    raw = pos[0]
    column = pos[1]
    # Check Row
    for i in range(9):
        if num == board[raw][i]:
            return False
    # Check Column
    for i in range(9):
        if num == board[i][column]:
            return False

    # Check Sub Grid
    subrow = raw // 3
    subcolumn = column // 3

    for i in range(subrow * 3, (subrow * 3) + 3):
        for j in range(subcolumn * 3, (subcolumn * 3) + 3):
            if num == board[i][j]:
                return False
    return True


def emptyCell(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return row, column
    return None


def getnewgrid():
    grid = Generate_grid()
    solve(grid)
    while type(emptyCell(grid)) == tuple:
        print(grid)
        grid = Generate_grid()
        solve(grid)
    # write the grid in a file
    save_grid(grid)
    return grid


def remove_number(grid, pos):
    y = pos[0]
    x = pos[1]
    grid[y][x] = 0
    return grid


def random_position():
    y = random.randint(0, 8)
    x = random.randint(0, 8)
    return y, x


def uniquegrid(grid0):
    def possible(y, x, n, grid1):
        for i in range(9):
            if grid1[y][i] == n:
                return False
        for i in range(9):
            if grid1[i][x] == n:
                return False
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if grid1[y0 + i][x0 + j] == n:
                    return False
        return True



    def Solve(grid3):
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    for n in range(1, 10):
                        if possible(y, x, n, grid3):
                            grid[y][x] = n
                            yield from Solve(grid3)
                            grid[y][x] = 0
                    return
        yield (np.matrix(grid))

    def s0lv(s):
        S = {}
        j = 1
        try:
            i = next(s)
            S["{}".format(str(j))] = i
        except StopIteration:
            i = 'StopIteration'
        while i != 'StopIteration':
            S["{}".format(str(j))] = i
            try:
                i = next(s)
                j += 1
            except StopIteration:
                i = 'StopIteration'
        return S

    if len(list(Solve(grid0))) != 1:
        return False
    else:
        return True


# method to read every grid in the folder
def get_file_names():
    path = './gen'
    files = [path + '/' + f for f in listdir(path)]
    return files


def save_grid(grid):
    gridf = []
    dupl = False
    files = get_file_names()
    for f in files:
        gridf = []
        # syntaxe to a regular expression to a sequence of numbers
        with open(f, 'r') as f:
            for row in f:
                line = row.split(' ')
                gridf.append([int(i) for i in line[:-1]])
        f.close()
        if gridf != []:
            if (gridf == grid) or dupl:
                dupl = True
    if not dupl:
        with open('.\gen\grid' + f'{time.time()}' + '.txt', 'w') as f:
            for i in range(9):
                for j in range(9):
                    f.write(str(grid[i][j]) + ' ')
                f.write('\n')
        f.close()


def count_zero(grid):
    count = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                count += 1
    return count


grid = getnewgrid()

i = 0

# pos = random_position()
# grid = remove_number(grid, pos)
# delete = True
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     # wait 2 seconds
#     time.sleep(0.2)
#     # if delete:
#     pos = random_position()
#     grid2 = grid.copy()
#     grid2 = remove_number(grid2, pos)
#     if uniquegrid(grid2):
#         grid = remove_number(grid, pos)
#         i += 1
#     else:
#         print("max complexity reached", i)
#         save_grid(grid)
#         delete = False
#     sudoku = Sudoku(taille_ecran_sudoku, grid)
#     pygame.display.flip()  # Actualise lecran
#
# for j in range(1):
#     c = 0
#     grid = getnewgrid()
#     positions = []
#     for i in range(9):
#         for j in range(9):
#             positions.append((i, j))
#     # creat a generator giving the elements of the list "positions"
#     random.shuffle(positions)
#     positions = itertools.cycle(positions)
#     # shuffle the list of positions
#     pos = next(positions)
#     grid = remove_number(grid, pos)
#     while c < 60:
#         pos = next(positions)
#         grid2 = grid.copy()
#         grid2 = remove_number(grid2, pos)
#         if uniquegrid(grid2):
#             grid = remove_number(grid, pos)
#             c += 1
#             print(c)
#             save_grid(grid)
#             print(grid)
#             # print('\n\n[',end='')
#             # for i in grid[:-1]:
#             #     print('[', end='')
#             #     for j in i[:-1]:
#             #         print(j, end=', ')
#             #     print(i[-1], end='],')
#             # print('[', end='')
#             # for j in grid[-1]:
#             #     print(j, end=', ')
#             # print(i[-1], end=']')
#             # print(']', end='')
#     print('num0', count_zero(grid))
