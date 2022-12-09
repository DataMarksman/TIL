# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
N, M = map(int, sys.stdin.readline().split())
ans = 0

first_line = list(map(int, sys.stdin.readline().split()))
if 
ex_max = M-((first_line[::-1].index(1))+1)
for input_line in range(1, N):
    line = list(map(int, sys.stdin.readline().split()))
    if 1 in line[:ex_max]:
        ex_max = M-((line[::-1].index(1))+1)
        ans += 1


print(ans)