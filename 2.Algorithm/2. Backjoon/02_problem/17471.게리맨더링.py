# BOJ. 17471 게리 맨더링
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
value_list = [0] + list(map(int, input().split()))



for put_in in range(N):



    T = int(input())
    for case_num in range(1, T + 1):
