# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

N = int(input())
AM, AW = map(int, input().split())
BM, BW = map(int, input().split())
CM, CW = map(int, input().split())

if AM <= BW + CW and BM <= AW + CW and CM <= AW + BW:
    pass

else:
    print(0)
