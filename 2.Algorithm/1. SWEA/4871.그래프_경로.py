# 4871.그래프_경로
def dfs(arr):
    global visited
    global stack
    if len(stack) <= 0:
        return 0
    fr = stack.pop()
    for om in range(V+1):
        if arr[fr][om] == 1:
            if om == goal[1]:
                return 1
            elif (fr, om) not in visited:
                visited += [(fr, om)]
                stack += [om]
    if len(visited) >= V:
        return 0
    else:
        return dfs(arr)


T = int(input())
for case_num in range(1, T+1):
    V, E = map(int, input().split())
    V = int(V)
    E = int(E)
    board = [[0]*(V+1) for _ in range((V+1))]
    for i in range(E):
        start, end = map(int, input().split())
        board[start][end] = 1
    goal = list(map(int, input().split()))
    stack = [goal[0]]
    visited = []
    print(f'#{case_num} {dfs(board)}')
