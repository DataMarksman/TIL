# import sys
# sys.stdin = open("sample_input.txt", "r")
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

T = 10
for tc in range(1, T+1):
    case_num = int(input())
    start = [0, 0]
    goal = [0, 0]
    board = []
    N = 16
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
