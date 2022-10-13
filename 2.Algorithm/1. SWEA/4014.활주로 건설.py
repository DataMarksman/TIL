# SWEA. 4014. 활주로 건설
# 설계 목적: 돌리고 앞뒤로 경사로 만들고 GO
# 1.
def check(r, platform):
    flag = True
    stair_set = set()
    checking = 0
    while flag and checking < N - 1:
        if abs(platform[r][checking] - platform[r][checking + 1]) >= 2:
            flag = False
            break
        elif platform[r][checking] - platform[r][checking + 1] == 1:
            for setting in range(K):
                place_A = int(checking + 1 + setting)
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


T = int(input())
for tc in range(1, T + 1):
    N, K = tuple(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    re_board = list(map(list, zip(*board)))

    ans = 0
    for x in range(N):
        if check(x, board):
            ans += 1
        if check(x, re_board):
            ans += 1
    print(f'#{tc} {ans}')