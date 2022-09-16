# SWEA. 1953. 탈주범 검거
# 설계 목적: 그냥 평범한 델타 탐색인데요?
# 1. 일반적인 델타 탐색 처럼 똑같은 4방 탐색인데, 뚫려있는 길이 다릅니다.
# 2. 해당 지점에 묻혀있는 파이프의 종류에 따라 뚫려있는 (=갈 수 있는) 길이 다른데, 내가 있는 위치와 탐색 위치의 특성을 같이 본다.
# 3. 내가 보는 위치는 dx, dy 상에서 찾을 수 있는 위치다. 그리고 확인해야하는 것은 탐색하는 쪽에서 내쪽으로 길이 나 있는가 여부다.
#    -> 즉, (direction + 2) % 4 는 상대가 나와 마주 보는지 파악할 수 있는 방법인 것이다. (역방향을 배정해줬으니까!)
# 4. visited에 없고, 해당 구간과 연결되어있으면 visited 에 넣고 Q에 넣기.
# 5. 이것을 주어진 횟수만큼 반복 한다.
# 개선점:
# 1.

dx = [[0], [0, 1, 0, -1], [0, 1, 0, -1], [0, 0, 0, 0], [0, 0, 0, -1], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, -1]]
dy = [[0], [1, 0, -1, 0], [0, 0, 0, 0], [1, 0, -1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, -1, 0], [0, 0, -1, 0]]

T = int(input())
for case_num in range(1, T + 1):
    info = list(map(int, input().split()))
    height = info[0]
    wide = info[1]
    start = (info[2], info[3])
    time = info[4]
    board = [list(map(int, input().split())) for _ in range(height)]
    visited = set()
    visited.add(start)
    run_queue = set()
    run_queue.add(start)
    passed_time = 1
    while passed_time < time:
        size = len(run_queue)
        temp_set = set()
        for checking in range(size):
            point = run_queue.pop()
            x = point[0]
            y = point[1]
            Ori = board[x][y]
            for direction in range(4):
                px = x + dx[Ori][direction]
                py = y + dy[Ori][direction]
                if 0 <= px < height and 0 <= py < wide and (px, py) not in visited:
                    Pre = board[px][py]
                    if Pre:
                        if (dx[Ori][direction] == (-1) * dx[Pre][(direction+2) % 4]) and \
                                (dy[Ori][direction] == (-1) * dy[Pre][(direction+2) % 4]):
                            visited.add((px, py))
                            temp_set.add((px, py))
        run_queue = set(temp_set)
        passed_time += 1
    print(f'#{case_num} {len(visited)}')
