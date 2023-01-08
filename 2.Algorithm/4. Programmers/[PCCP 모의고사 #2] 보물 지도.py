# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

import sys
sys.setrecursionlimit(10 ** 8)
# 이번 문제 또한 수학에서 배우는 2차원 좌표계를 기준으로 한다.
# 이동하기 위한 좌표 가산 값을 배정해준다.
# idx 0, 1, 2, 3 각각이 위, 오른쪽, 아래, 왼쪽을 의미한다.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution(n, m, hole):
    if n == 1 or m == 1:
        if len(hole) >= 2:
            return -1
        else:
            return max(abs(m - n) - 1, 1)
    hole_set = set()
    for check_hole in hole:
        hole_set.add(tuple(check_hole))
    INF = sys.maxsize

    DP = [[[0, 0]] + [[INF, INF] for _ in range(m)] + [[0, 0]] for _ in range(n)]
    DP = [[[0, 0] for _ in range(m + 2)]] + DP + [[[0, 0] for _ in range(m + 2)]]
    DP[1][1] = [0, 0]


    def find_root(x, y, move_count, jump, ex):
        nonlocal answer
        direction_list = [0, 1, 2, 3]
        if x == n and y == m:
            if move_count < answer:
                DP[n][m][jump] = move_count
                answer = move_count
            return
        elif move_count < answer:
            for direction in list(direction_list - ex):
                px = x + dx[direction]
                py = y + dy[direction]
                if move_count + 1 < DP[px][py][jump]:
                    if (px, py) not in hole_set:
                        DP[px][py][jump] = move_count + 1
                        find_root(px, py, move_count + 1, jump, ex)
                    elif jump == 0:
                        px += dx[direction]
                        py += dy[direction]
                        if move_count + 1 < DP[px][py][1] and (px, py) not in hole_set:
                            if move_count < DP[px][py][1]:
                                DP[px][py][1] = move_count + 1
                                find_root(px, py, move_count + 1, 1, ex)

    answer = INF
    find_root(1, 1, 0, 0, -1)
    if answer == INF:
        answer = -1
    return answer

data = [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]
# data = [[2, 3], [3, 3]]
print(solution(5, 5, data))

