# BOJ. 21609. 상어 중학교
# 설계 의도: 함수로 기능 분절하여 구현하기
# 개선점:
import sys
input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 가장 큰 블록 범위를 구하기 위한 함수
def finding(pick_x, pick_y):
    # 각 외부 변수들을 global 로 뽑는다.
    global visited
    global max_score
    global target_list
    global rainbow_count

    # 탐색을 돌려주기 위한 스택
    pick_set = {(pick_x, pick_y), }

    # 시작 위치의 색
    pattern = board[pick_x][pick_y]

    # 이번 범위의 길이를 구하기 위한 visited 와 무지개 구슬 카운팅
    temp_visited = {(pick_x, pick_y), }
    temp_rainbow = 0

    # 사방 탐색하면서 BFS GO GO
    while pick_set:
        x, y = pick_set.pop()
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if 0 <= px < N and 0 <= py < N and (px, py) not in temp_visited:
                if board[px][py] == pattern:
                    pick_set.add((px, py))
                    temp_visited.add((px, py))
                elif board[px][py] == 0 and (N+1, px, py) not in temp_visited:
                    pick_set.add((px, py))
                    temp_rainbow += 1
                    temp_visited.add((N+1, px, py))

    # 이번 탐색에서 밟았던 색깔 블록은 다음 탐색에서 밟지 않음.
    visited |= temp_visited

    # 길이가 가장 큰거 찾고
    if len(temp_visited) > max_score and len(temp_visited) >= 2:
        max_score = len(temp_visited)
        rainbow_count = temp_rainbow
        target_list = sorted(temp_visited)

    # 길이가 같으면 무지개 구슬 개수 찾고
    elif len(temp_visited) == max_score and max_score >= 2:
        if temp_rainbow > rainbow_count:
            rainbow_count = temp_rainbow
            target_list = sorted(temp_visited)

        # 무지개 구슬 개수도 같으면 좌표를 min 값으로 찾기기
        elif temp_rainbow == rainbow_count:
           if min(temp_visited) > target_list[0]:
                target_list = sorted(temp_visited)


# 중력 구현 함수
def gravity():
    global board
    for fx in range(N):
        for fy in range(N):
            # -2, 즉 사라진 곳 찾으면 그걸 맨 위로 버블 정렬 하면서 올린다.
            if board[fx][fy] < -1:
                swith_x = int(fx)
                while True:
                    if 0 <= swith_x - 1 and board[swith_x-1][fy] != -1:
                        board[swith_x][fy], board[swith_x-1][fy] = board[swith_x-1][fy], board[swith_x][fy]
                        swith_x -= 1
                    else:
                        break


# 돌리는 함수. 사각형의 네 꼭지점을 반시계 방향으로 한방에 돌려준다.
def spinning():
    global board
    for spin in range((N+1)//2):
        for c in range((N-1)-spin, spin, -1):
            board[spin][c], board[(N-1) - c][spin], board[(N-1) - spin][(N-1) - c], board[c][(N-1)-spin] =\
                board[c][(N - 1) - spin], board[spin][c], board[(N - 1) - c][spin], board[(N - 1) - spin][(N - 1) - c]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 반복문으로 돌려주기!
while True:
    visited = set()
    target_list = [(-1, -1)]
    rainbow_count = 0
    max_score = 0

    # 뒤에서부터 찾아준다.
    for r in range(N - 1, -1, -1):
        for c in range(N - 1, -1, -1):
            if board[r][c] > 0 and (r, c) not in visited:
                finding(r, c)

    # 이번 회차에서 찾은 최대 범위 길이가 2 이상일 때만 진행
    if max_score >= 2:
        ans += max_score**2
        while target_list:
            pick = target_list.pop()

            # 무지개 구슬 빼기
            if pick[0] == N + 1:
                tx, ty = pick[1], pick[2]

            # 일반 색 구슬 빼기
            else:
                tx, ty = pick
            board[tx][ty] = -2

        # 중력, 돌리기, 중력
        gravity()
        spinning()
        gravity()

    # 아니라면 반복문 종료
    else:
        break
print(ans)
