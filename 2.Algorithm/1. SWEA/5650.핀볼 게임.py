# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import defaultdict
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction_dict = {(0, 1): 2, (0, 2): 1, (0, 3): 3, (0, 4): 2, (0, 5): 2,    # 올라감
                  (1, 1): 2, (1, 2): 2, (1, 3): 1, (1, 4): -1, (1, 5): 2,   # 오른쪽
                  (2, 1): -1, (2, 2): 2, (2, 3): 2, (2, 4): 1, (2, 5): 2,   # 내려감
                  (3, 1): -3, (3, 2): -1, (3, 3): 2, (3, 4): 2, (3, 5): 2}  # 왼쪽


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    safe_zone = set()
    black_hole = set()
    block_set = [set() for _ in range(6)]
    teleport_list = [[] for _ in range(5)]
    teleport_dict = {(-5, -5): -5,}
    board = []
    ans = 0
    for put_in in range(N):
        line = list(map(int, input().split()))
        for start_pick in range(N):
            if line[start_pick] == 0:
                safe_zone.add((put_in, start_pick))
            elif line[start_pick] == -1:
                black_hole.add((put_in, start_pick))
            elif 1 <= line[start_pick] <= 5:
                block_set[line[start_pick]].add((put_in, start_pick))
            elif 6 <= line[start_pick] <= 10:
                teleport_list[line[start_pick]-6].append((put_in, start_pick))
    for tele_set in range(5):
        if teleport_list[tele_set]:
            teleport_dict[teleport_list[tele_set][0]] = teleport_list[tele_set][1]
            teleport_dict[teleport_list[tele_set][1]] = teleport_list[tele_set][0]
    start_set = set(safe_zone)
    while start_set:
        X, Y = start_set.pop()
        for direction in range(4):
            PX = X + dx[direction]
            PY = Y + dy[direction]
            D = int(direction)
            count = 0
            while True:
                # print(count)
                if (PX, PY) in black_hole or (PX, PY) == (X, Y):
                    break
                elif 0 <= PX < N and 0 <= PY < N:
                    if (PX, PY) in safe_zone:
                        PX += dx[D]
                        PY += dy[D]
                    elif (PX, PY) in teleport_dict:
                        PX, PY = teleport_dict[PX, PY]
                        PX += dx[D]
                        PY += dy[D]
                    else:
                        for checking in range(1, 6):
                            if (PX, PY) in block_set[checking]:
                                D = (D + direction_dict[(D, checking)]) % 4
                                PX += dx[D]
                                PY += dy[D]
                                count += 1
                                break
                        else:
                            break
                elif PX == -1 or PX == N or PY == -1 or PY == N:
                    D = (D + 2) % 4
                    PX += dx[D]
                    PY += dy[D]
                    count += 1
                else:
                    break
            if count > ans:
                ans = int(count)
    print(f'#{case_num} {ans}')


"""
1
10
0 1 0 3 0 0 0 0 7 0 
0 0 0 0 -1 0 5 0 0 0 
0 4 0 0 0 3 0 0 2 2 
1 0 0 0 1 0 0 3 0 0 
0 0 3 0 0 0 0 0 6 0 
3 0 0 0 2 0 0 1 0 0 
0 0 0 0 0 1 0 0 4 0 
0 5 0 4 1 0 7 0 0 5 
0 0 0 0 0 1 0 0 0 0 
2 0 6 0 0 4 0 0 0 4 
"""