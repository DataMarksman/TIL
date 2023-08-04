# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import itertools


def game(players, score):
    global max_score
    base_1 = 0
    base_2 = 0
    base_3 = 0
    out_count = 0
    ining = 0
    player_hit = player_list[ining]
    n = 0
    while ining < N:
        hitter = player_hit[players[n]]
        if hitter == 0:
            out_count += 1
            if out_count == 3:
                base_1 = 0
                base_2 = 0
                base_3 = 0
                ining += 1
                if ining < N:
                    player_hit = player_list[ining]
                else:
                    break
                out_count = 0
        elif hitter == 1:
            score += base_3
            base_1, base_2, base_3 = 1, base_1, base_2

        elif hitter == 2:
            score += base_3 + base_2
            base_1, base_2, base_3 = 0, 1, base_1

        elif hitter == 3:
            score += base_3 + base_2 + base_1
            base_1, base_2, base_3 = 0, 0, 1

        elif hitter == 4:
            score += base_3 + base_2 + base_1 + 1
            base_1 = 0
            base_2 = 0
            base_3 = 0
        n += 1
        if n == 9:
            n = 0
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

