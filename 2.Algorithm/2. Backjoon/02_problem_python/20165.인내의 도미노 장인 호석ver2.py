# 강환석
# BOJ. 20165. 인내의 도미노 장인 호석
# 설계 의도: 조건에 맞는 실행. 쉽다.
# 개선점:
# 첫트에서 공격자 점수 안넣어서 틀렸다.... ㅠ ㅠ
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
direction_dict = {'N': 0, 'S': 1, 'E': 2, 'W': 3}

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
fallen = set()
ans = 0
for turn in range(T):
    X, Y, D = input().split()
    X = int(X) - 1
    Y = int(Y) - 1
    if (X, Y) not in fallen:
        D = direction_dict[D]
        fallen.add((X, Y))
        ans += 1
        distance = board[X][Y] - 1
        while True:
            X += dx[D]
            Y += dy[D]
            if 0 <= X < N and 0 <= Y < M and (X, Y) not in fallen and distance > 0:
                fallen.add((X, Y))
                ans += 1
                distance = max((distance - 1), board[X][Y] - 1)
            elif (X, Y) in fallen and distance > 0:
                distance -= 1
            else:
                break
    XX, YY = map(int, input().split())
    fallen.discard((XX - 1, YY - 1))

print(ans)
for print_x in range(N):
    line= []
    for print_y in range(M):
        print('F' if (print_x, print_y) in fallen else 'S', end=' ')
    else:
        print(*line)