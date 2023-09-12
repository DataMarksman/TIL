# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())
for case in range(1,N+1):
    score = int(input())
    if score >= 4501:
        print(f"Case #{case}: Round 1")
    elif score >= 1001:
        print(f"Case #{case}: Round 2")
    elif score >= 26:
        print(f"Case #{case}: Round 3")
    else:
        print(f"Case #{case}: World Finals")