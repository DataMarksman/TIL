# BOJ.15661. 링크와 스타트
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
from itertools import combinations
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
num_dict = {}
for x in range(N):
    for y in range(N):
        if x < y:
            num_dict[(x, y)] = int(board[x][y] + board[y][x])
iter_set = set(combinations((i for i in range(1, N+1)), j) for j in range(1, N+1))
visited = set()
while iter_set:
    temp_ans = 0
    temp_list = list(iter_set.pop())
    for i in range(len(temp_list)-1):
        for j in range(i, len(temp_list)):
            temp_ans += num_dict[(i, j)]
            if temp_ans >





ans = 99999999999999
case_sort(0, set())
print(ans)