# 10163 색종이
N = int(input())
box_list = [list(map(int, input().split())) for _ in range(N)]
board = [[0]*101 for _ in range(101)]
ans = 0
for idx in range(N):
    dx_s = box_list[idx][0]
    dy_s = box_list[idx][1]
    for dx in range(dx_s, dx_s + 10):      # 박스 x 좌표 별
        for dy in range(dy_s, dy_s + 10):  # 박스 y 좌표 별
            if board[dx][dy] == 0:
                board[dx][dy] = 1          # 현재 박스 발자취 쓰기
                ans += 1

print(ans)