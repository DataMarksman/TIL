# BOJ. 21923. 곡예 비행
# 설계 의도: 양쪽에서 DP 걸고 들어오면 됩니다.
# 좌 -> 우 의 DP + 우 -> 좌 의 DP 값을 더해주면 해당 좌표에서 만나는 상/하향 비행의 궤적의 최적 값이 나오죠.
# 개선점:
# 조금 더 빨리 하고자 하는데, 로직의 문제인듯 하다.
import sys
from copy import deepcopy
input = sys.stdin.readline
N, M = map(int, input().split())

# 한칸짜리면 그냥 2배해서 출력하자.
if N == 1 and M == 1:
    print(int(input())*2)

# 그 외에는 값을 받고 좌, 우 DP로 쌓아 올리면 된다.
else:
    score_board = [list(map(int, input().split())) for _ in range(N)]

    # 좌 -> 우 방향의 DP
    DP_A = deepcopy(score_board)
    ans = -9999999999999999
    for first_X in range(N-2, -1, -1):
        DP_A[first_X][0] += DP_A[first_X+1][0]
    for Ax in range(1, M):
        for Ay in range(N-1, -1, -1):
            if Ay == N-1:
                DP_A[Ay][Ax] += DP_A[Ay][Ax-1]
            else:
                DP_A[Ay][Ax] += max(DP_A[Ay+1][Ax], DP_A[Ay][Ax-1])

    # 우 -> 좌 방향의 DP
    DP_B = deepcopy(score_board)
    for first_X in range(N-2, -1, -1):
        DP_B[first_X][M-1] += DP_B[first_X+1][M-1]
    for Bx in range(M-2, -1, -1):
        for Ay in range(N-1, -1, -1):
            if Ay == N-1:
                DP_B[Ay][Bx] += DP_B[Ay][Bx+1]
            else:
                DP_B[Ay][Bx] += max(DP_B[Ay+1][Bx], DP_B[Ay][Bx+1])

    # 양쪽 방향의 값을 합쳐준 값들 중에서 가장 큰 값을 구한다.
    for sum_x in range(N):
        for sum_y in range(M):
            sum_XY = DP_A[sum_x][sum_y] + DP_B[sum_x][sum_y]
            if sum_XY > ans:
                ans = sum_XY
    print(ans)