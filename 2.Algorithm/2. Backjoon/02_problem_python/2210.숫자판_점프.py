# BOJ. 2210 숫자판 점프
# 설계 의도:
# 1. 2차원 배열 순회하면서 순열 만들고
# 2. 해당 순열로 만들어진 좌표에서 델타 탐색으로 4방향 탐색을 가는 각각의 케이스를 재귀로 불러오고
# 3. 해당 과정에서 만들어진 모든 숫자를 set에 저장하여 중복 제거
# 4. 이후 set의 len 반환하면 끝
# 개선점:
# 1. 백트래킹 하나도 안걸었다... 그런데도 되는 신기한 문제

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def numbering(x, y, k, arr):
    global color_set
    if k >= 6:
        color_set.add(arr)
    else:
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if 0 <= px < 5 and 0 <= py < 5:
                new_str = arr + str(board[px][py])
                numbering(px, py, k + 1, new_str)


board = [list(map(int, input().split())) for _ in range(5)]
flag = True
color_set = set()
for r in range(5):
    for c in range(5):
        numbering(r, c, 0, str())
print(len(color_set))