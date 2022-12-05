# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
N = int(sys.stdin.readline())
DP = [[(0, 0, 0)]*(N+1) for _ in range(N+1)]
for x in range(N):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    for y in range(N):
        a, b, c = max(DP[x][y+1], DP[x+1][y])
        if line[y] == 0 and c == a:
            DP[x+1][y+1] = (a + 1, b, c)
        elif line[y] == 1 and a == b + 1:
            DP[x+1][y+1] = (a, b+1, c)
        elif line[y] == 2 and b == c + 1:
            DP[x+1][y+1] = (a, b, c+1)
        else:
            DP[x + 1][y + 1] = (a, b, c)
print(sum(DP[N][N]))

