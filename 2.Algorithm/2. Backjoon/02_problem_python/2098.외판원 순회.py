# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# # sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
#
# def travel(start, idx, visited, value):
#     global ans
#     visited = set(visited)
#     if len(visited) == N:
#         if board[idx][start] != 0:
#             value += board[idx][start]
#             if value < ans:
#                 ans = value
#     min_value = 9999999999999
#     min_idx = N
#     for picking in range(N):
#         if picking not in visited:
#             if board[idx][picking] < min_value:
#                 min_value = board[idx][picking]
#                 min_idx = picking
#     if min_idx < N:
#         travel(start, min_idx, visited | {min_idx, }, value + min_value)
#
#
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# ans = 99999999999999999999
# for pick in range(N):
#     travel(pick, pick, {pick, }, 0)
# print(ans)


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def travel(start, idx, visited, value):
    global ans
    if value > ans:
        return
    else:
        visited = set(visited)
        if len(visited) == N:
            if board[idx][start] != 0:
                value += board[idx][start]
                if value < ans:
                    ans = value
        for picking in range(N):
            if picking not in visited:
                travel(start, picking, visited | {picking, }, value + board[idx][picking])


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 99999999999999999999
for pick in range(N):
    travel(pick, pick, {pick, }, 0)
print(ans)