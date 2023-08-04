# BOJ. 21610 마법사 상어와 비바라기
# 설계 의도: % N 으로 좌표 가지고 놀아보자~
# 1. 그냥 뚝딱 뚝딱 구현하기.
# 개선점:
# 1. 문제가 쉬워서 효율화 쪽으로 고민하기가 오히려 힘들다. 로직을 바꿔야 한다.
import sys
input = sys.stdin.readline

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1), ]
ans = 0

# 마법 방향, 거리 받을 때마다 시뮬레이션 실행
for turn in range(M):

    # 방향과 거리를 변수로 받기
    direction, length = map(int, input().split())

    # 넘어가면 다시 처음부터. 라고 생각하면 그냥 %N 해주자. 음수값을 예상해서 +N 해주고 하자.
    for moving in range(len(cloud)):
        R, C = cloud[moving]
        PR = ((R + dx[direction]*length) + N) % N
        PC = ((C + dy[direction]*length) + N) % N
        board[PR][PC] += 1
        cloud[moving] = (PR, PC)
    else:

        # 위에서 이동 다하면, 각 이동된 좌표에서 대각선 탐색해서 빗물이 있는 장소 만큼 현재 위치에 += 1
        for pooling in range(len(cloud)):
            R, C = cloud[pooling]
            for cross_check in [2, 4, 6, 8]:
                PR = R + dx[cross_check]
                PC = C + dy[cross_check]
                if 0 <= PR < N and 0 <= PC < N:
                    if board[PR][PC]:
                        board[R][C] += 1

    # 이전에 비를 뿌렸던 곳을 set 으로 만들어서 검증용으로 쓰자.
    rained_set = set(cloud)

    # cloud 리스트 리셋해주고, 다시 채워넣기
    cloud = []
    if turn == M-1:
        for x in range(N):
            for y in range(N):
                if board[x][y] >= 2 and (x, y) not in rained_set:
                    board[x][y] -= 2
                    cloud.append((x, y))
                ans += board[x][y]

    else:
        for x in range(N):
            for y in range(N):
                if board[x][y] >= 2 and (x, y) not in rained_set:
                    board[x][y] -= 2
                    cloud.append((x, y))

# 합산 하기
print(ans)