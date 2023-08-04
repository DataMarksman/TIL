# BOJ. 14501. 퇴사
# 설계 의도: DP
# 개선점:
# 코드 더 줄이는 방법을 모르겠다.

import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())

# DP 값으로 쓸 수 있을 친구들을 모아놓을 리스트 입니다.
DP_sum = [[0] for _ in range(N+7)]

# 최종 DP 값을 저장할 리스트 입니다.
DP = [0]*(N+7)

# 값을 하나씩 받아주면서 DP를 진행해봅시다.
for dp in range(1, N+1):
    # 값을 받아줍니다.
    A, B = map(int, input().split())

    # 현재 날짜에서 걸리는 날짜를 더한 위치에
    # 현재 이전 날짜의 최적값과 현재 날짜의 일을 받았을 때, 받을 수 있는 돈의 합계를 넣어줍니다.
    DP_sum[dp + A - 1].append(DP[dp-1] + B)

    # 현재 밟고 있는 위치에 있는 리스트의 값들 중 가장 큰 값을 최종 DP 값에 반영해줍니다.
    DP[dp] = max(max(DP_sum[dp]), DP[dp-1])

# 최종 DP 값들 중 가장 큰 값을 도출합니다.
print(max(DP))