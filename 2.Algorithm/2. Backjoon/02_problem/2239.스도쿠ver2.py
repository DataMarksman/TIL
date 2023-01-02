# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def sudoku(depth):
    if depth >= len(target):
        return False
    x0, y0 = target[depth][0], target[depth][1]
    candidate = possible_list(x0, y0)
    for c in candidate:
        arr[x0][y0] = c
        if not sudoku(depth+1):
            return False
        arr[x0][y0] = 0
    return True


def possible_list(x, y):
    lst = []
    for i in range(1, 10):
        if is_possible(x, y, i):
            lst.append(i)
    return lst


def is_possible(x, y, num):
    for i in range(9):
        if arr[x][i] == num:
            return False
        if arr[i][y] == num:
            return False
    bx, by = x//3*3, y//3*3
    for i in range(bx, bx+3):
        for j in range(by, by+3):
            if arr[i][j] == num:
                return False
    return True


arr = []
target = []
for i in range(9):
    arr.append(list(map(int, input())))
    for j in range(9):
        if not arr[i][j]:
            target.append([i, j])
sudoku(0)
for row in arr:
    print(''.join(map(str, row)))