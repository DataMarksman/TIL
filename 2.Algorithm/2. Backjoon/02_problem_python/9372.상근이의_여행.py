# BOJ. 9372 상근이의 여행
# 설계 의도: 조건에 맞는 실행
# 개선점:
# 빡구현 하면 틀린다. python 쓰면 시간 초과 난다.
# 그냥 쓰레기 문제.
# import sys
# sys.setrecursionlimit(10**6)


# T = int(input())
# for tc in range(1, T + 1):
#     N, M = tuple(map(int, input().split()))
#     board = [[0]*N for _ in range(1001)]
#     for put_in in range(N):
#         lines = tuple(map(int, input().split()))
#         A = lines[0]
#         B = lines[1]
import sys
for tc in range(1, int(sys.stdin.readline()) + 1):
    N, M = map(int, sys.stdin.readline().split())
    for A in range(M):
        map(int, sys.stdin.readline().split())
    print(N - 1)
