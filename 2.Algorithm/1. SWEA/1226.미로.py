# import sys
# sys.stdin = open("sample_input.txt", "r")
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


def dfs(idx):
    global visited
    if idx == goal:
        return 1
    if idx not in visited:
        visited += [idx]
    print(idx)
    for direction in range(4):
        tmp_idx = [0, 0]
        tmp_idx[0] = idx[0] + dx[direction]
        tmp_idx[1] = idx[1] + dy[direction]
        if (tmp_idx not in visited) and (board[tmp_idx[0]][tmp_idx[1]] == (0 or 2)):
            dfs(tmp_idx)  # 다음 재귀 깊이로 이동


T = 10
for tc in range(1, T+1):
    case_num = int(input())
    start = [0, 0]
    goal = [0, 0]
    board = []
    for i in range(16):
        tmp_lines = list(input())
        for check in range(16):
            if tmp_lines[check] == '2':
                start = [i, check]
            elif tmp_lines[check] == '3':
                goal = [i, check]
        board += [tmp_lines]
    visited = []
    print(visited)
    print(goal)
    print(start)
    print(f'#{case_num} {dfs(start) if (dfs(start) is not None) else 0 }')
