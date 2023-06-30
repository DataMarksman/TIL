# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
import bisect
input = lambda: sys.stdin.readline().rstrip('\r\n')

n = int(input())
seq = list(map(int, input().split()))
dp = [seq[0]]

for i in range(1, n):
    print(dp)
    if seq[i] > dp[-1]:  # 현재 값이 dp의 마지막 값보다 클 경우
        dp.append(seq[i])  # dp에 추가
    else:  # 그렇지 않은 경우
        idx = bisect.bisect_left(dp, seq[i])  # 이진 탐색으로 현재 값이 들어갈 위치 찾기
        dp[idx] = seq[i]  # 해당 위치의 값을 현재 값으로 업데이트

print(len(dp))  # dp의 길이가 LIS의 길이
