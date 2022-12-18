# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
check_list = [[] for _ in range(N+1)]
for check_fill in range(1, N+1):

T = int(input())
for tc in range(T):
    S, E = map(int, input().split())
    lst = num_list[S-1:E]
    if lst == lst[::-1]:
        print(1)
    else:
        print(0)

