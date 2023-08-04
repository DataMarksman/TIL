# BOJ. 2096. 내려가기
# 설계 의도: 이게 왜 골드?
# 개선점:
import sys
import copy
input = sys.stdin.readline
N = int(input())
dp_max = list(map(int, input().split()))
dp_min = copy.deepcopy(dp_max)
for dp in range(N-1):
    A, B, C = map(int, input().split())
    temp_max = [0, 0, 0]
    temp_min = [0, 0, 0]
    temp_max[0] = max(dp_max[0], dp_max[1]) + A
    temp_max[1] = max(dp_max[0], dp_max[1], dp_max[2]) + B
    temp_max[2] = max(dp_max[1], dp_max[2]) + C
    temp_min[0] = min(dp_min[0], dp_min[1]) + A
    temp_min[1] = min(dp_min[0], dp_min[1], dp_min[2]) + B
    temp_min[2] = min(dp_min[1], dp_min[2]) + C
    dp_max = copy.deepcopy(temp_max)
    dp_min = copy.deepcopy(temp_min)
print(int(max(dp_max)), int(min(dp_min)))




