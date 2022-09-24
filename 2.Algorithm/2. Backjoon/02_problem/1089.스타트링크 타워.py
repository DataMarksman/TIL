# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

def searching(idx):
    num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, }
    if board[0][idx+1] == '#':
        num_set.remove()



N = int(input())
board = [list(input()) for _ in range(N)]
numbers = [[] for _ in range(N)]
