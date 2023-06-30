# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

import sys

def solution(line):
    answer = []

    X_max = -sys.maxsize
    X_min = sys.maxsize
    Y_max = -sys.maxsize
    Y_min = sys.maxsize

    dot_set = set()

    for X_line in range(len(line) - 1):
        for Y_line in range(X_line + 1, len(line)):
            A, B, E = line[X_line]
            C, D, F = line[Y_line]
            inclination = (A * D - B * C)
            if inclination == 0:
                continue
            else:
                X = int((B * F - E * D) / inclination)
                Y = int((E * C - A * F) / inclination)
                X_max = max(X_max, X)
                X_min = min(X_min, X)
                Y_max = max(Y_max, Y)
                Y_min = min(Y_min, Y)
                dot_set.add((-Y, X))

    X_length = int(X_max - X_min + 1)
    Y_length = int(Y_max - Y_min + 1)
    for y in range(Y_length):
        basic_line = "." * (X_length)
        for x in range(X_length):
            if (y - Y_max, x + X_min) in dot_set:
                basic_line[x] = "*"

    return answer

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))
