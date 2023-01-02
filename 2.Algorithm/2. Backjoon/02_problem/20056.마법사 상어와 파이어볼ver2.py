# BOJ. 20056. 마법사 상어와 파이어볼
# 설계 의도: set으로 구현
# 개선점:
# [set()] 을 복사할 때, *N으로 하면 오류납니다. for _in range()로 구현해야합니다... 몇번씩이나 속아버림
import sys

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, T = map(int, input().split())
board = [[set() for _ in range(N)] for _ in range(N)]
pick_set = set()
for magics in range(M):
    r, c, m, s, d = map(int, input().split())
    pick_set.add((r - 1, c - 1, m, s, d, 0))
ans = 0
turn = 0

# 제시된 턴 만큼 진행하겠습니다.
while turn < T:
    turn += 1

    # 이전 회차에서 수집한 주문 목록들을 불러와서 2차원 배열 위에서 이동시킵니다.
    while pick_set:
        x, y, fireballs, speed, D, turns = pick_set.pop()
        tx = (x + (dx[D] * speed)) % N if x + (dx[D] * speed) >= 0 else (N - (abs(x + (dx[D] * speed)) % N)) % N
        ty = (y + (dy[D] * speed)) % N if y + (dy[D] * speed) >= 0 else (N - (abs(y + (dy[D] * speed)) % N)) % N
        board[tx][ty].add((fireballs, speed, D, turns))

    # 각 2차원 배열들 위의 좌표에 있는 set의 길이가 2 이상이면 로직 진입, 아니면 그냥 다음 목록에 넣어줍니다.
    for xx in range(N):
        for yy in range(N):

            # 2개 이상 모여있으면 로직 진입
            if len(board[xx][yy]) >= 2:
                length = len(board[xx][yy])
                FB, SP, DS, turns = board[xx][yy].pop()
                fire_magics = int(FB)
                speed_count = int(SP)
                direction_odd = int(DS) % 2
                direction_flag = True

                # 존재하는 모든 주문을 합쳐주고, 조건에 맞게 4등분 해주기
                while board[xx][yy]:
                    FB, SP, DS, turns = board[xx][yy].pop()
                    fire_magics += FB
                    speed_count += SP
                    if direction_odd != int(DS) % 2:
                        direction_flag = False
                direction_plus = 0 if direction_flag else 1

                # 5등분 했을때, 주문력이 1이상이어야 하므로, 4이하는 커팅해줍니다.
                if fire_magics > 4:
                    new_speed = speed_count // length
                    for distribute in range(4):
                        new_dist = (distribute * 2) + direction_plus
                        pick_set.add((xx, yy, fire_magics // 5, new_speed, new_dist, turn))

                    # 1개만 있으면 그냥 넣어줍니다.
            elif board[xx][yy]:
                FB, SP, DS, turns = board[xx][yy].pop()
                pick_set.add((xx, yy, FB, SP, DS, turns))
while pick_set:
    ans += pick_set.pop()[2]
print(ans)