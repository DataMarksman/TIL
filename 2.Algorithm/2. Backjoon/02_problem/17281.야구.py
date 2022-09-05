# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

from collections import deque
import sys
sys.setrecursionlimit(10**6)


def team_making(arr, depth):
    if depth >= 9:
        line_up = arr[:3] + [0] + arr[3:]
        game(line_up, 0)

    else:
        for put_in in range(1,9):
            if put_in not in arr:
                arr.append(put_in)
                team_making(arr, depth + 1)
                arr.pop()


def game(players, score):
    global max_score
    base_ground = deque([0, 0, 0])
    out_count = 0
    ining = 0
    n = 0
    while ining < N:
        if player_list[ining][players[n]] == 0:
            out_count += 1
            if out_count == 3:
                base_ground = deque([0, 0, 0])
                ining += 1
                out_count = 0
        elif player_list[ining][players[n]] == 1:
            base_ground.append(1)
            ace = base_ground.popleft()
            if ace == 1:
                score += 1
        elif player_list[ining][players[n]] == 2:
            base_ground.append(1)
            base_ground.append(0)
            for check in range(2):
                ace = base_ground.popleft()
                if ace == 1:
                    score += 1
        elif player_list[ining][players[n]] == 3:
            score += sum(base_ground)
            base_ground = deque([1, 0, 0])
        elif player_list[ining][players[n]] == 4:
            score += sum(base_ground) + 1
            base_ground = deque([0, 0, 0])
        n += 1
        if n == 9:
            n = 0
    if score > max_score:
        max_score = int(score)


N = int(input())
player_list = [list(map(int, input().split())) for _ in range(N)]
max_score = 0
team_making([], 1)
print(max_score)
# game([], 0)

