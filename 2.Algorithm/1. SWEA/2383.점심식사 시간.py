# SWEA.
# 설계 목적: 그냥 문제 설명에서 대놓고 DP라고 광고하고 있어서... 가뜩이나 약한 DP 한번 풀어나보죠.
# 1. 근데 DP 할줄 몰?루 라서 SET으로 풀겠슴다. 투 트랙으로 구성하고 서로가 가져간 수는 빼줄겁니당
# 2. 길이가 3 이상이면 이전꺼랑 비교해서 커트해줄 예정.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    people_set = set()
    population = 0
    stair_list = []
    stair_1 = [set() for _ in range(200)]
    stair_2 = [set() for _ in range(200)]
    for R in range(N):
        line = list(map(int, input().split()))
        for C in range(N):
            if line[C] == 1:
                population += 1
                people_set.add((R, C, population))
            elif line[C] > 1:
                stair_list.append((line[C], R, C))
    stair_list.sort()
    X1 = stair_list[0][1]
    Y1 = stair_list[0][2]
    X2 = stair_list[1][1]
    Y2 = stair_list[1][2]
    while people_set:
        pick = people_set.pop()
        dist_1 = abs(pick[0] - X1) + abs(pick[1] - Y1)
        dist_2 = abs(pick[0] - X2) + abs(pick[1] - Y2)
        stair_1[dist_1].add(pick[2])
        stair_2[dist_2].add(pick[2])
    visited = set()

    time = 0
    while len(visited) < population:
        time += 1

    print(f'#{case_num} {ans}')