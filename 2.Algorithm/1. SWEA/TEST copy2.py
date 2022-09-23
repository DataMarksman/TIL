import sys
sys.setrecursionlimit(10**6)


def dice_back(idx):
    reverse_idx = ''
    if idx == 0:
        reverse_idx = 5
    elif idx == 1:
        reverse_idx = 3
    elif idx == 2:
        reverse_idx = 4
    elif idx == 3:
        reverse_idx = 1
    elif idx == 4:
        reverse_idx = 2
    elif idx == 5:
        reverse_idx = 0
    return reverse_idx


def counting(depth, idx, sum_value):

    global dice
    global max_value
    next_idx_back = 0
    max_dice = 0

    if depth == N-1:
        idx_back = dice_back(idx)
        dice[depth][idx], dice[depth][idx_back] = 0, 0
        for i in range(6):
            if max_dice < dice[depth][i]:
                max_dice = dice[depth][i]
        if max_value < sum_value + max_dice:
            max_value = sum_value + max_dice
        return

    for j in range(6):
        if dice[depth][idx] == dice[depth+1][j]:
           next_idx_back = j
    next_idx = dice_back(next_idx_back)
    idx_back = dice_back(idx)

    idx_value = dice[depth][idx]
    idx_back_value = dice[depth][idx_back]
    dice[depth][idx], dice[depth][idx_back] = 0, 0

    for k in range(6):
        if max_dice < dice[depth][k]:
            max_dice = dice[depth][k]
    dice[depth][idx] = idx_value
    dice[depth][idx_back] = idx_back_value
    counting(depth+1, next_idx, sum_value + max_dice)


N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
max_value = 0
for i in range(6):
    counting(0, i, 0)
print(max_value)