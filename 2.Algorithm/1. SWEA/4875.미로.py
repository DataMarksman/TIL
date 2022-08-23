# SWEA.4875. 미로
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
dx = [0, -1, 0, 1]      # 좌 상 우 하 순서
dy = [-1, 0, 1, 0]


def maze(location, stack):
    global visited
    visited[location[0]][location[1]] = 1
    for src in range(4):
        if board[location[0]+dx[src]][location[1]+dy[src]] == 3:
            return print(f'#{case_num} {1}')
        elif board[location[0]+dx[src]][location[1]+dy[src]] == 0 and\
                visited[location[0]+dx[src]][location[1]+dy[src]] == 0 and\
                [location[0] + dx[src], location[1]+dy[src]] not in stack:
            stack += [[location[0] + dx[src], location[1]+dy[src]]]
    if len(stack) <= 0:
        return print(f'#{case_num} {0}')
    else:
        location = stack.pop(0)
        return maze(location, stack)


T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    # board
    board = [[1]*(N+2)]
    visited = [[0]*(N+2) for _ in range(N+2)]
    start = []
    end = []
    try:
        for searching in range(N):
            write_in = list(input())
            put_in = [1]
            for chk in range(N):
                put_in += [int(write_in[chk])]
                if int(write_in[chk]) == 2:
                    start = [searching+1, chk+1]
                elif int(write_in[chk]) == 3:
                    end = [searching+1, chk+1]
            else:
                put_in += [1]
                board += [put_in]
        else:
            board += [[1]*(N+2)]
        print(board)
        if start and end:
            maze(start, [])
        else:
            print(f'#{case_num} {0}')

    except:
        print(f'#{case_num} {0}')

"""
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
"""
