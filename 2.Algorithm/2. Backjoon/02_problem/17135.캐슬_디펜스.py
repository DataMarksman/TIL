# BOJ.
# 설계 의도: 각 턴마다 가장 많이 잡을 수 있는 케이스들을 쭉쭉 뽑자.
# 1. shooting 함수를 통해 해당 턴에서 해당 범위 내 잡을 수 있는 가장 많은 수를 도출한다.
# 2. 매 BFS를 시행할 때마다
#   각 궁수들에게서 매 행의 적들과의 길이를 도출하여, 해당 적들을 처단.
#   우선순위는 각 행의 모든 적을 죽이는 것이 최우선. 그 다음이
# 3. 각 궁수들의 위치는 순열로 모두 도출하여 위의 루틴에 집어 넣는다.
#   N은 최대 턴수로서, 가장 아래부터 d 만큼의 범위를 탐색하면서 올라오는 재귀함수를 만들어 사용해보자
# 4. 각 킬의 카운트는 set에 저장된 좌표의 개수로 한다.
# 개선점:
import sys
sys.setrecursionlimit(10**6)


dx = [0, -1, 0]
dy = [-1, 0, 1]


def shooting(depth, distance, batch, kill_set):
    global max_kill
    n = int(depth)
    d = int(distance)
    kill_count = [0, 0, 0]
    kill_queue = [(n, batch[0], 0), (n, batch[1], 1), (n, batch[2], 2)]
    while sum(kill_count) < 3 and d > 0 and n >= 0:
        temp_kill_set = set()
        size = len(kill_queue)
        for killing in range(size):
            archer = list(kill_queue.pop(0))
            if kill_count[archer[2]] == 0:
                for direct in range(3):
                    px = archer[0] + dx[direct]
                    py = archer[1] + dy[direct]
                    if 0 <= px < n and 0 <= py < M:
                        if board[px][py] == 1 and (px, py) not in kill_set:
                            kill_count[archer[2]] = 1
                            temp_kill_set.add((px, py))
                            break
                        else:
                            kill_queue.append((px, py, archer[2]))
            if sum(kill_count) >= 3:
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


"""