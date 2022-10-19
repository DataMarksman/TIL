# BOJ. 그냥 N M 시리즈 이거로 돌려막기 다했슴다
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
from itertools import combinations
input = sys.stdin.readline

A, B = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
ans_list = list(combinations(num_list, B))
ans_list.sort()
print(*ans_list[0])
for printing in range(1, len(ans_list)):
    if ans_list[printing] != ans_list[printing-1]:
        print(*ans_list[printing])