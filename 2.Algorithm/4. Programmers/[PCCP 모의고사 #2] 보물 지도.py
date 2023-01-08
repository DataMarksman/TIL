# PRG.
# https://school.programmers.co.kr/learn/courses/15009/lessons/121690
# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:
import heapq
import sys
sys.setrecursionlimit(10**8)
# 이번 문제 또한 수학에서 배우는 2차원 좌표계를 기준으로 한다.
# 이동하기 위한 좌표 가산 값을 배정해준다.
# idx 0, 1, 2, 3 각각이 위, 오른쪽, 아래, 왼쪽을 의미한다.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 본 풀이는 heapQ 기반이기 때문에 move_count 가 가장 작은 친구가 먼저 뽑힙니다.
# 이 부분에서 시간적인 이득을 얻을 수 있는데, 다음과 같습니다.
# 1. 진입할 때의 움직임 카운트가 가장 적은 친구를 뽑아서 사용하기 때문에 이후에 같은 위치에 진입하면 무조건 기존 값보다 크게 나옵니다.
# 2. 이렇게 뽑아 나가면 최종 좌표의 값을 처음 뽑았을 때의 값이 최적의 값이다. BFS과 같은 개념으로 진입 가능하다.


def solution(n, m, hole):
    if n == 1 or m == 1:                    # 만약 지도가 일직선인 지도라면,
        if len(hole) >= 2:                  # 구멍이 2개 이상 일 때, 두번 뛰어넘을 수 없으므로
            return -1                       # 무조건 -1을 반환합니다.
        else:                               # 그 외의 경우에는 바로 옆에 있거나 2칸일 경우 1로 동일하기 때문에
            return max(abs(m-n)-1, 1)       # max를 걸어주고 (일직선 거리, 1) 중에서 최적 값을 반환 해줍니다

    hole_set = set()                        # 좌표 기반 구멍을 조회하기 위해 set 을 만들어줍니다.
    for check_hole in hole:                 # 구멍을 순회하면서 SET에 넣어줍니다.
        hole_set.add(tuple(check_hole))

    maxi = sys.maxsize                      # 첫 값은 최대치로 주기 위해서 시스템상 max 값을 넣어줍니다.

    # 백트래킹을 위해 각 좌표에 [점프를 쓰지 않았을 때의 최솟값, 점프를 쓰고 나서의 최솟값] 을 배정해줍니다.
    DP = [[[0, 0]] +                         # 그 주위로 [0, 0] 으로 패딩해줍니다.
          [[maxi, maxi] for _ in range(m)]   # DP 기반 백트래킹이기 때문에 [0, 0] 으로 패딩된 값은 진입하지 않습니다.
          + [[0, 0]] for _ in range(n)]      # [Tip!] 0 < px <= n 과 같은 식으로 좌표 조건을 줄 수도 있습니다.
    DP = [[[0, 0] for _ in range(m + 2)]] + DP + [[[0, 0] for _ in range(m + 2)]]
    DP[1][1] = [0, 0]                        # 시작점은 [0, 0] 으로 초기화 시켜줍니다.

    Q = []                                   # 뽑아 쓸 Q 리스트를 만들어줍니다.
    Q.append((0, 1, 1, 0))                   # 시작 값인 ( 0번 움직임, x 좌표는 1, y 좌표는 1, 점프는 쓰지 않음) 을 넣어줍니다.
    answer = n * m                           # 첫 값은 n*m 값, 즉 모든 값을 순회하는 값으로 넣어줍니다.

    while Q:                                 # 뽑을 수 있는 Q가 있는 한 계속 돌아갑니다.
        pick = heapq.heappop(Q)              # Q에서 값을 하나씩 뽑아줍니다.
        move_count = pick[0]                 # 값을 넣어줄 때,
        x = pick[1]                          # (움직인 횟수, x좌표, y좌표, 점프 사용 여부) 로 넣어줬으므로
        y = pick[2]                          # 뽑은 값을 그대로 할당해줍니다.
        jump = pick[3]

        if x == n and y == m:                # 만약 여기가 최종 좌표라면 HeapQ 기반이므로 처음 뽑은 값이 최적의 값입니다.
            return move_count                # 바로 return 시켜줍니다.

        elif move_count < answer and DP[x][y][jump] >= move_count:  # 아니라면 메인 로직에 진입합니다.
            move_count += 1                  # 먼저 이번 움직임을 기록해주기 위해 move_count를 +=1 해줍니다.

            for direction in range(4):       # 델타 탐색을 진행하여 4방 탐색을 시행합니다.
                px = x + dx[direction]       # 각각의 값의 가중치는 dx, dy에 배정해주었습니다.
                py = y + dy[direction]

                # [Tip!] 만약 패딩을 해주지 않았다면, 아래와 같은 식이 필요합니다.
                # if 1 <= px <= n and 1 <= py <= m:
                if (px, py) not in hole_set and move_count < DP[px][py][jump]:
                    DP[px][py][jump] = move_count
                    heapq.heappush(Q, (move_count, px, py, jump))

                if jump == 0:
                    px += dx[direction]
                    py += dy[direction]
                    if 1 <= px <= n and 1 <= py <= m and (px, py) not in hole_set:
                        if move_count < DP[px][py][1]:
                            DP[px][py][1] = move_count
                            heapq.heappush(Q, (move_count, px, py, 1))

    # 만약 중간에 함수가 return 되어서 정지하지 않고, Q가 없어서 반복문이 종결되었다면,
    # 이는 답이 없다는 의미이므로 answer 는 -1로 반환 시켜줍니다.
    return -1