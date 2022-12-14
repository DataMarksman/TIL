# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
from math import lcm
from math import gcd
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]





