# BOJ. 7569. 토마토
# 설계 의도: 3차원 좌표 귀찮으니까 그냥 SET으로 idx 받아서 set 연산으로 풀자.
# 개선점:

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]


def tomato(candidate, date):
    global remain_set
    candidate = set(candidate)
    New_tomato = set()
    while candidate:
        pick = candidate.pop()
        z, x, y = pick[0], pick[1], pick[2]
        for direction in range(6):
            PX = x + dx[direction]
            PY = y + dy[direction]
            PZ = z + dz[direction]
            if (PZ, PX, PY) in remain_set:
                remain_set.remove((PZ, PX, PY))
                New_tomato.add((PZ, PX, PY))
    if New_tomato:
        return tomato(New_tomato, date + 1)
    else:
        if not New_tomato and not remain_set:
            return date
        else:
            return int(0)


row, column, height = map(int, input().split())
remain_set = set()
first_set= set()
for first_z in range(height):
    for first_x in range(column):
        tomato_box = list(map(int, input().split()))
        for first_y in range(row):
            if tomato_box[first_y] == 1:
                first_set.add((first_z, first_x, first_y))
            elif tomato_box[first_y] == 0:
                remain_set.add((first_z, first_x, first_y))
if len(remain_set) == 0:
    print(0)
else:
    dates = int(tomato(first_set, 0))
    if dates > 0:
        print(dates)
    else:
        print(-1)