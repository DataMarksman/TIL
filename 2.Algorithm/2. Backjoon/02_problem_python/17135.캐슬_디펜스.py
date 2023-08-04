# BOJ. 17135 캐슬 디펜스
# 설계 의도: 빡 구현
# 1. shooting 함수를 통해 제시된 절차에 맞게 한턴동안 잡을 수 있는 최대한의 적들을 산출한다.
# 2. 각 궁수 (3명) 별 < 화살 카운트 >를 부여하여, 화살을 사용하였는지 여부를 파악한다.
#   이는 같은 적을 두명이 같이 쏴도, 킬 카운트는 하나만 오르기 때문에 넣은 조건이다.
# 3. 그렇다면 킬 카운트는 다르게 잡아야하는데, 이를 set() 위치좌표 저장으로 카운팅했다.
#   잡은 적들의 위치 정보를 set()에 넣어서 set의 길이가 잡은 적을 의미하도록 했다.
# 4. if 0 <= px < n and 0 <= py < M: <- 좌표 컨트롤로, 첫 시작 좌표를 아예 적들이 있는 범위 밖에서 시작했다.
#   이를 통해, 첫 탐색에서는 무조건 위에 있는 한칸만 도출 되도록 하였다.
# 개선점: 내가 적은 코드를 믿지 말고, 내 구상을 믿어라.
# 1. temp_kill_set = set() <- 이게 while문 안에 들어가있는걸 끝까지 캐치하지 못해서 맞왜틀 하고 있었다.
#   리셋 조건 등 구현을 확실하게 하려면 문제를 조금더 정교하게 풀 필요가 있을 것 같다.
#


import sys
sys.setrecursionlimit(10**6)


dx = [0, -1, 0]
dy = [-1, 0, 1]


def shooting(depth, distance, batch, kill_set):
    global max_kill
    n = int(depth)
    d = int(distance)
    arrow_count = [0, 0, 0]
    kill_queue = [(n, batch[0], 0), (n, batch[1], 1), (n, batch[2], 2)]
    temp_kill_set = set()
    while sum(arrow_count) < 3 and d > 0 and n >= 0:
        size = len(kill_queue)
        for killing in range(size):
            archer = list(kill_queue.pop(0))
            if arrow_count[archer[2]] == 0:
                for direct in range(3):
                    px = archer[0] + dx[direct]
                    py = archer[1] + dy[direct]
                    if 0 <= px < n and 0 <= py < M:
                        if board[px][py] == 1 and (px, py) not in kill_set:
                            arrow_count[archer[2]] = 1
                            temp_kill_set.add((px, py))
                            break
                        else:
                            kill_queue.append((px, py, archer[2]))
            if sum(arrow_count) >= 3:
                d = 0
                break
        d -= 1
    kill_set |= temp_kill_set
    if depth <= 1 and len(kill_set) > max_kill:
        max_kill = len(kill_set)
    elif depth > 1:
        return shooting(depth - 1, distance, batch, kill_set)


N, M, D = tuple(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
batch_set = set()
batch_position = [t for t in range(M)]
max_kill = 0
for i in range(M):
    for j in range(M):
        for k in range(M):
            if i < j < k:
                shooting(N, D, (i, j, k), set())
print(max_kill)
"""
엣지 케이스 탐색용 

2 4 2
1 1 1 1
0 1 1 0

10 10 8
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

5 5 3
1 1 1 0 1
0 1 1 0 0
1 1 1 0 0
0 1 1 0 0
1 1 1 0 0

"""