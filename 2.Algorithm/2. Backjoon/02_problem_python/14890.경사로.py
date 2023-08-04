# BOJ. 14890 경사로
# 설계 의도: 인덱스 컨트롤
# 1. 그냥 뒤에꺼가 더 높으면 뒤로 K칸을 계단으로 만들고 이 좌표를 stair_set에 넣음.
# 2. 뒤에가 더 낮으면, 현재 위치로부터 뒤의 K칸의 좌표를 stair_set에 넣음.
# 3. 만약 넣은 좌표가 이미 set에 있거나 범위를 넘어가면 False 반환.
# 4. 끝까지 True 남아있는 개수 반환
# 개선점:
import sys
sys.setrecursionlimit(10**6)
def check(r, platform):
    flag = True
    stair_set = set()
    checking = 0
    while flag and checking < N-1:
        if abs(platform[r][checking] - platform[r][checking+1]) >= 2:
            flag = False
            break
        elif platform[r][checking] - platform[r][checking+1] == 1:
            for setting in range(K):
                place_A = int(checking+1+setting)
                if place_A not in stair_set and 0 <= place_A < N:
                    stair_set.add(place_A)
                else:
                    flag = False
                    break
        elif platform[r][checking] - platform[r][checking + 1] == -1:
            for setting in range(K):
                place_B = int(checking - setting)
                if place_B not in stair_set and 0 <= place_B < N:
                    stair_set.add(place_B)
                else:
                    flag = False
                    break
        checking += 1
    if flag:
        return True
    else:
        return False


N, K = tuple(map(int, input().split()))
board = []
for put_in in range(N):
    board.append(list(map(int, input().split())))
re_board = list(map(list, zip(*board)))

ans = 0
for x in range(N):
    if check(x, board):
        ans += 1
    if check(x, re_board):
        ans += 1
print(ans)
