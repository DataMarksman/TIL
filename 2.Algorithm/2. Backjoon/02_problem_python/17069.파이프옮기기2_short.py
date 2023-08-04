# BOJ. 17069. 파이프 옮기기 2
# 설계 의도: 그냥 약간 어려운 D네요. D 치고는 깔끔하게 떨어집니다.
# 1. 내가 있는 지점이 어떤 모양의 끝 점인지를 알면 된다.
# 2. 3가지 값을 각 D 좌표에 배정해주고 각각이 가로, 대각선, 세로를 의미하게 한다.
# 개선점:
# 1. 더 빠르게 가능한가? 일단 36ms 인데..
import sys
p = sys.stdin.readline
N = int(p())
B = [[0]*N] + [list(map(int, p().split())) for _ in range(N)]
D = [[[0, 0, 0] for i in range(N)] for j in range(N+1)]
D[1][1][0] = 1
for x in range(1,N):
    for y in range(1,N):
        if B[x][y]==0:
            D[x][y][0]=D[x][y-1][0]+D[x][y-1][1]
            D[x][y][2]=D[x-1][y][2]+D[x-1][y][1]
            if B[x-1][y]==0 and B[x][y-1]==0:
                D[x][y][1]=sum(D[x-1][y-1])
print(sum(D[N][N-1]))

