# SWEA.
# 설계 목적: 자, 최소값을 찾기 위한 여정을 떠나보죠
# 1. 요컨데, 그리디 탐색이다. 가장 가까운곳으로 가서 사냥하고,
# 2. 해당 사냥감을 반납하는 곳 or 다음 몬스터가 있는 곳중 가까운 곳을 계속 비교하면서 찾아가자.
# 3. 첫 시행에는 몬스터 3곳의 위치와 현재 위치를 비교해서 가까운 곳으로 가고
#       이후 해당 몬스터 반납하는곳 or 남은 몬스터 2곳, 등등 유동적으로 바뀐다.
# 개선점:
# 1.


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    board = []
    monsters = [[] for _ in range(9)]
    hunt_count = [0, 0, 0, 0, 0]
    monster_number = 0
    sum_sum = 0
    for put_in in range(N):
        lines = list(map(int, input().split()))
        for finding in range(N):
            if lines[finding] != 0:
                monsters[N+lines[finding]] = [put_in, finding]
                if lines[finding] > monster_number:
                    monster_number = lines[finding]
        board += [[0] + lines]
    current = [0, 0]
    while sum(hunt_count) < monster_number*2:
        distance_list = []
        for hunting in range(1, monster_number+1):
            if hunt_count[hunting] == 0:
                dx = abs(monsters[N+hunting][0] - current[0])
                dy = abs(monsters[N+hunting][1] - current[1])
                distance_list.append((dx+dy, hunting, [monsters[N+hunting][0], monsters[N+hunting][1]]))
            elif hunt_count[hunting] == 1:
                dx = abs(monsters[N-hunting][0] - current[0])
                dy = abs(monsters[N-hunting][1] - current[1])
                distance_list.append((dx+dy, hunting, [monsters[N+hunting][0], monsters[N+hunting][1]]))
        distance_list.sort()
        target = distance_list[0]
        sum_sum += target[0]
        hunt_count[target[1]] += 1
        current = target[2]
        print(distance_list)
        print(current)
        print(monsters)
        print(hunt_count)
    print(f'#{case_num} {sum_sum}')
"""
3
3
0 0 0
0 1 -1
0 0 0
4
-3 -1 1 0
-2 0 0 3
0 0 0 0
0 0 2 0
5
0 0 -3 0 0
0 0 0 3 0
0 0 0 0 2
0 0 1 0 0
-1 0 0 -2 0
"""