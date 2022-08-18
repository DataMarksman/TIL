# BOJ.10158 개미
# 설계 의도: X 좌표와 Y 좌표를 따로 보면, 너무나 쉽다.
# 1. 문제에서 준대로 설계할 필요는 없다. 편한대로 구하고 형식에 맟춰서 반환할 뿐.
# 2. 대각선 이동? x,y 좌표 이동시 제자리에 멈춰있을 일이 없네?
# 개선점:
# 1. 변수 N개 (N>1)를 받을 때, int 로 받되, map 처럼 휘발성 없게 받으려면?
# 2. if now_idx[0] == max_x or now_idx[0] == 0: 는 되는데,
#       왜 if now_idx[0] == (max_x or 0): 은 안될까???????

# 조타용 좌표, 0이 없으므로 생략한다~
dx = [1, -1]
dy = [1, -1]
now_dir = [0, 0]

W, H = map(int, input().split())
max_x = int(W)
max_y = int(H)

p, q = map(int, input().split())
now_idx = [int(p), int(q)]
t = int(input())
for turn in range(t):
    if now_idx[0] == max_x or now_idx[0] == 0:
        now_dir[0] = (now_dir[0] + 1) % 2
    if now_idx[1] == max_y or now_idx[1] == 0:
        now_dir[1] = (now_dir[1] + 1) % 2
    now_idx[0] += dx[now_dir[0]]
    now_idx[1] += dy[now_dir[1]]

print(*now_idx)
