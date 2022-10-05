# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
import heapq
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# import sys
# input = sys.stdin.readline
# N = int(input())
# num_list = [0]*10001
# for put_in in range(N):
#     num_list[int(input())] += 1
# for printing in range(1, 10001):
#     if num_list[printing]:
#         for p in range(num_list[printing]):
#             print(printing)

Money = int(input())
N = int(input())
ans = 0
for put_in in range(N):
    A, B = map(int, input().split())
    ans += A * B
if Money == ans:
    print('Yes')
else:
    print('No')

