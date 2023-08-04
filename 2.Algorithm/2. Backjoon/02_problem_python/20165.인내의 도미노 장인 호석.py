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
for turn in range(2*T):

    # 공격자 턴: 0,2,4 ... 즉 짝수다.
    if turn % 2 == 0:
        X, Y, D = input().split()
        X = int(X) - 1
        Y = int(Y) - 1
        if (X, Y) not in fallen:
            D = direction_dict[D]

            # 넘어진 곳은 fallen 에 넣어주고 공격자의 점수에도 + 1 해준다.
            fallen.add((X, Y))
            ans += 1
            distance = board[X][Y]-1

            # 해당 방향으로 계속 진행하면서 넘어져서 닿는 거리가 0이 될때까지 계속 한다.
            while True:
                X += dx[D]
                Y += dy[D]

                # 인덱싱 컨트롤과 더불어서, 해당 지점이 넘어졌는지 여부는 fallen 으로 체크한다.
                if 0 <= X < N and 0 <= Y < M and (X, Y) not in fallen and distance > 0:
                    fallen.add((X, Y))
                    ans += 1
                    distance = max((distance - 1), board[X][Y] - 1)
                elif (X, Y) in fallen and distance > 0:
                    distance -= 1
                else:
                    break

    # 세우는 것은 fallen 에서 discard로 구현한다. 만약 값이 없더라도 오류 안나도록.
    else:
        X, Y = map(int, input().split())
        fallen.discard((X-1, Y-1))

# 먼저 공격자의 점수를 출력해준다.
print(ans)
for print_x in range(N):

    # 프린팅 효율을 위해서 바로바로 판단해서 뽑아준다.
    for print_y in range(M-1):
        print('F' if (print_x, print_y) in fallen else 'S', end=' ')
    else:
        print('F' if (print_x, M-1) in fallen else 'S')



