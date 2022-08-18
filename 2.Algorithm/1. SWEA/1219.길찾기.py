# 1219. 길찾기
def dfs(arr):
    global visited
    global stack
    if len(stack) <= 0:
        return 0
    fr = stack.pop()
    for om in range(100):
        if arr[fr][om] == 1:
            if om == 99:
                return 1
            if visited[fr][om] == 0:
                visited[fr][om] = 1
                stack += [om]
    else:
        return dfs(arr)


T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    case_num = int(V)
    N = int(E)
    board = [[0]*101 for _ in range(101)]
    visited = [[0]*101 for _ in range(101)]
    stack = [0]
    road_list = list(map(int, input().split()))
    for i in range(N):
        board[road_list[2*i]][road_list[(2*i)+1]] = 1
    print(f'#{case_num} {dfs(board)}')
