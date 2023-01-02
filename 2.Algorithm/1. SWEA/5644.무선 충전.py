# SWEA. 5644. 무선 충전
# 설계 목적:
# 1.
# 개선점:
# 1.

dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]
def setting(x, y, d, p, numbering):
    global board
    for fill_X in range(x - d, x + d + 1):
        for fill_Y in range(y - d, y + d + 1):
            Plus = (fill_X-x) + (fill_Y-y)
            Minus = (fill_X-x) - (fill_Y-y)
            if 0 <= fill_X < 10 and 0 <= fill_Y < 10 and -d <= Plus <= d and -d <= Minus <= d:
                board[fill_X][fill_Y].add((p, numbering))


T = int(input())
for case_num in range(1, T + 1):
    Time, Charger = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    board = [[{(0, 0), } for i in range(10)] for j in range(10)]
    for BC_set in range(1, Charger+1):
        X, Y, V, P = map(int, input().split())
        setting(Y-1, X-1, V, P, BC_set)
    passed = 0
    idx_A = (0, 0)
    idx_B = (9, 9)
    ans = max(board[0][0])[0] + max(board[9][9])[0]

    while passed < Time:
        idx_A = (idx_A[0] + dx[A[passed]], idx_A[1] + dy[A[passed]])
        idx_B = (idx_B[0] + dx[B[passed]], idx_B[1] + dy[B[passed]])
        pick_A = max(board[idx_A[0]][idx_A[1]])
        pick_B = max(board[idx_B[0]][idx_B[1]])
        if pick_A == pick_B:
            pick_C = board[idx_A[0]][idx_A[1]] | board[idx_B[0]][idx_B[1]]
            pick_C.remove(pick_A)
            if len(pick_C) >= 1:
                pick_B = max(pick_C)
            else:
                pick_B = (0, 0)
        ans += pick_A[0] + pick_B[0]
        passed += 1

    print(f'#{case_num} {ans}')