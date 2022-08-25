# SWEA.1226 미로
# 설계 목적: DFS로 풀기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = 10
for tc in range(1, T+1):
    case_num = int(input())
    board = []
    start = []
    for i in range(16):
        in_list = list(input())
        if '2' in in_list:
            start = [i, in_list.index('2')]
        board += [in_list]
    # print(board)
    # print(start)
    stack = [start]
    visited = set()
    flag = False
    while stack:
        A = stack.pop()
        for d in range(4):
            px = A[0] + dx[d]
            py = A[1] + dy[d]
            # print(px, py, queue, visited)
            if px < 0 or px >= 16 or py < 0 or py >= 16:
                continue
            elif board[px][py] == '3':
                flag = True
                stack.clear()
                break
            elif board[px][py] == '0' and (px, py) not in visited:
                stack.append((px, py))
                visited.add((px, py))
    if flag:
        print(f'#{case_num} {1}')
    else:
        print(f'#{case_num} {0}')

