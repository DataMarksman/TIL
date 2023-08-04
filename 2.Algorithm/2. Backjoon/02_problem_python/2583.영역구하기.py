# BOJ. 2583 영역 구하기
# 설계 의도: 단지 나누기 열화버전
# 1. 2차원 배열 탐색하면서 0이 등장하면 그 좌표 기준으로 델타 탐색으로 0이 있는 범위 전부 탐색
# 2. 이렇게 탐색완료한 부분의 넓이를 구하고, 탐색한 부분은 += 1로 마킹. 다시 방문 X
# 개선점:
# 1.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def find_out(tx, ty):
    global board
    global ans_list
    stack = set()
    visited = set()
    stack.add((tx, ty))
    board[tx][ty] += 1
    area_count = 1
    while stack:
        pick = stack.pop()
        px = pick[0]
        py = pick[1]
        for direction in range(4):
            xx = px + dx[direction]
            yy = py + dy[direction]
            if 0 <= xx < height and 0 <= yy < wide:
                if (xx, yy) not in visited and board[xx][yy] == 0:
                    board[xx][yy] += 1
                    visited.add((xx, yy))
                    stack.add((xx, yy))
                    area_count += 1
    return int(area_count)


M, N, K = map(int, input().split())
height = int(M)
wide = int(N)
num = int(K)
board = [[0]*wide for i in range(height)]
ans_list = []
for put_in in range(num):
    lines = list(map(int, input().split()))
    for c in range(lines[0], lines[2]):
        for r in range(lines[1], lines[3]):
            board[r][c] += 1

for x in range(height):
    for y in range(wide):
        if board[x][y] == 0:
            ans_list.append(find_out(x, y))
ans_list.sort()
print(len(ans_list))
print(*ans_list)