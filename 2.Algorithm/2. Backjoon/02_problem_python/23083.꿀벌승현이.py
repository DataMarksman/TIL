# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

dx = [1, 0, -1]
dy = [-1, -1, 0]
tx = [0, -1, -1]
ty = [-1, -1, 0]

N, M = map(int, input().split())
DP = [[1]*M for _ in range(N)]
K = int(input())
for get_hole in range(K):
    a, b = map(int, input().split())
    DP[a-1][b-1] = 0
cut_flag = False
for first_line in range(N):
    if cut_flag:
        DP[first_line][0] = 0
    elif DP[first_line][0] == 0:
        cut_flag = True

for y in range(1, M):
    for x in range(N):
        temp_dp = 0
        if DP[x][y] > 0:
            if y % 2 == 1:
                for direction in range(3):
                    px = x + dx[direction]
                    py = y + dy[direction]
                    if 0 <= px < N and 0 <= py < M:
                        temp_dp += DP[px][py]
            else:
                for direction in range(3):
                    px = x + tx[direction]
                    py = y + ty[direction]
                    if 0 <= px < N and 0 <= py < M:
                        temp_dp += DP[px][py]
        DP[x][y] = temp_dp % 1000000007
print(DP[N-1][M-1] % 1000000007)
