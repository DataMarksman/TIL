# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

# N = int(input())
# case_num = 1
# while N != 0:
#     board = [list(map(int, input().split())) for _ in range(N)]
#     for first_line in range(1, N):
#         board[0][first_line] = board[0][first_line] + board[0][first_line-1]
#     for x in range(1, N):
#         for y in range(N):
#             A = board[x-1][y]
#             B = board[x][y-1] if 0 <= y - 1 else 10
#             board[x][y] = board[x][y] + min(A, B)
#     for printing in range(N):
#         print(board[printing])
#     print(f'Problem {case_num}: {board[N-1][N-1]}')
#     N = int(input())
#     case_num += 1


import sys
sys.setrecursionlimit(10**6)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def root_find(idx, visited, cost):
    global ans
    if ans < 99999999999999999:
        if cost > ans:
            return
    visited = set(visited)
    x = idx[0]
    y = idx[1]
    idx_list = []
    value_list = []
    for direction in range(4):
        px = x + dx[direction]
        py = y + dy[direction]
        if 0 <= px < N and 0 <= py < N and (px, py) not in visited:
            if (px, py) == (N - 1, N - 1):
                if cost + board[px][py] < ans:
                    ans = int(cost + board[px][py])
                return
            elif idx_list:
                for arrange in range(len(idx_list)):
                    if value_list[arrange] >= board[px][py]:
                        idx_list.insert(arrange, (px, py))
                        value_list.insert(arrange, board[px][py])

            else:
                idx_list.append((px, py))
                value_list.append(board[px][py])
    for recur in range(len(idx_list)):
        root_find(idx_list[recur], visited | {idx_list[recur], }, cost + board[idx_list[recur][0]][idx_list[recur][1]])


N = int(input())
case_num = 1
while N != 0:
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 99999999999999999999999
    root_find((0, 0), set(), board[0][0])
    print(f'Problem {case_num}: {ans}')
    N = int(input())
    case_num += 1