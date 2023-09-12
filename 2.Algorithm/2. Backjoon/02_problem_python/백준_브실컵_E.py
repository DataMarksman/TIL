# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N, M, K = map(int, input().split())
min_ans = max(N - (M*K), 0)
max_ans = min(N - (M*(K-1) + 1), N - 1)
print(min_ans, max_ans)