# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)
import itertools


def game(players, score):
    global max_score
    base_ground = [0, 0, 0]
    out_count = 0
    ining = 0
    n = 0
    while ining < N:
        if player_list[ining][players[n%9]] == 0:
            out_count += 1
            if out_count == 3:
                base_ground = [0, 0, 0]
                ining += 1
                out_count = 0
        elif player_list[ining][players[n%9]] == 1:
            base_ground.append(1)
            ace = base_ground.pop(0)
            if ace == 1:
                score += 1
        elif player_list[ining][players[n%9]] == 2:
            base_ground.append(1)
            base_ground.append(0)
            for check in range(2):
                ace = base_ground.pop(0)
                if ace == 1:
                    score += 1
        elif player_list[ining][players[n%9]] == 3:
            score += sum(base_ground)
            base_ground = [1, 0, 0]
        elif player_list[ining][players[n%9]] == 4:
            score += sum(base_ground) + 1
            base_ground = [0, 0, 0]
        n += 1
    if score > max_score:
        max_score = int(score)


N = int(input())
player_list = [list(map(int, input().split())) for _ in range(N)]
max_score = 0
player_number = [i for i in range(1, 9)]
score_set = set(itertools.permutations(player_number, 8))
while score_set:
    A = list(score_set.pop())
    line_up = A[:3]+[0]+A[3:]
    game(line_up, 0)
print(max_score)
# game([], 0)

