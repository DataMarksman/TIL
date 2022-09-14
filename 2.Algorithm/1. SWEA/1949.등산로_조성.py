# SWEA. 1949. 등산로 조성
# 설계 목적: 재귀를 쓸거예요
# 1. 일단 각 높은 봉우리를 스타트 지점으로 놓고
# 2. 각 봉우리 좌표에서 시작하는 재귀함수를 돌릴 겁니다.
#    -> i) 재귀 함수( 현재 좌표, visited, flag T/F=한번 공사 했니 안했니)
#    -> ii) 사실 공사 부분만 없었어도 visited 없어도 될 것 같은데, 일단 넣고 진행. 등산로 길이는 len(visited)로
#    -> iii) 델타 탐색을 통해, 사방 중에 visited에 없고 현재 위치보다 낮은 걸 visited 넣고 재귀 돌리기.
#    -> iv) 돌리는 와중에 첫번째로 만나는 나보다 높은 곳과의 차이가 K 미만이면 flag를 True로 바꾸고 계속 진행.
# 3. 이렇게 재귀 돌려서 출력합니다~
# 4. 리커전 에러 나면... 몰?루
# 개선점:
# 1. 재귀함수 들어갈 때, visited = set(visited) 안써줘서 계속 값 튕기는거... 1시간 동안 못찾아서 처음부터 다시 짬.

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def find_root(start, visited, flag, ex_height):
    global max_length
    x = start[0]
    y = start[1]
    visited = set(visited)
    flag = bool(flag)
    visited.add(start)
    height = int(board[x][y])
    if ex_height < height:
        height = ex_height
    for direction in range(4):
        px = x + dx[direction]
        py = y + dy[direction]
        if 0 <= px < N and 0 <= py < N and (px, py) not in visited:
            if board[px][py] < height:
                find_root((px, py), visited, flag, height)
            elif (board[px][py] - K < height) and flag:
                find_root((px, py), visited, False, height - 1)

    if len(visited) > max_length:
        max_length = len(visited)


T = int(input())
for case_num in range(1, T + 1):
    N, K = tuple(map(int, input().split()))
    board = []
    max_height = 0
    start_point = set()
    for put_in in range(N):
        line = list(map(int, input().split()))
        for checking in range(N):
            if line[checking] > max_height:
                start_point = set()
                max_height = int(line[checking])
                start_point.add((put_in, checking))
            elif line[checking] == max_height:
                start_point.add((put_in, checking))
        board += [line]
    max_length = 0
    while start_point:
        point = start_point.pop()
        find_root(point, set(), True, max_height)

    print(f'#{case_num} {max_length}')