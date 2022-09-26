# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# 1. 분명 쉬운 문제였는데, 후진 조건에서 사방의 벽만 생각하고, 중간 벽을 고려하지 않았다.

D_trans = [0, 3, 2, 1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
X, Y, D = map(int, input().split())
D = D_trans[D]
num_list = [list(map(int, input().split())) for _ in range(N)]
count = 0
num_list[X][Y] = 0

while True:
    if num_list[X][Y] == 0:
        num_list[X][Y] = 2
        count += 1
    for direction in range(1, 5):
        PX = X + dx[(D + direction) % 4]
        PY = Y + dy[(D + direction) % 4]
        if 0 < PX < N-1 and 0 < PY < M-1:
            if num_list[PX][PY] == 0:
                X = int(PX)
                Y = int(PY)
                D = (D + direction) % 4
                break
    else:
        PX = X - dx[D]
        PY = Y - dy[D]
        if 0 < PX < N-1 and 0 < PY < M-1 and num_list[PX][PY] != 1:
            X = int(PX)
            Y = int(PY)
        else:
            break
print(count)

"""
순서도 예시...
[01, 01, 01, 01, 01, 01, 01, 01, 01, 01]
[01, 57, 58, 47, 46, 45, 44, 43, 42, 01]
[01, 56, 49, 48, 01, 01, 01, 01, 41, 01]
[01, 51, 50, 01, 01, 37, 38, 39, 40, 01]
[01, 52, 01, 01, 36, 35, 32, 31, 00, 01]
[01, 53, 54, 13, 12, 34, 33, 30, 29, 01]
[01, 55, 15, 14, 11, 10, 00, 01, 28, 01]
[01, 17, 16, 03, 02, 09, 01, 01, 27, 01]
[01, 18, 19, 04, 05, 08, 01, 01, 26, 01]
[01, 22, 20, 21, 06, 07, 23, 24, 25, 01]
[01, 01, 01, 01, 01, 01, 01, 01, 01, 01]


7 7
4 2 1
1 1 1 1 1 1 1
1 0 0 0 1 0 1
1 0 1 1 0 0 1
1 0 0 0 0 1 1
1 0 0 1 0 0 1
1 0 0 0 0 0 1
1 1 1 1 1 1 1



"""