# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
def summing(current, visited, used, queue):
    global ans
    visited = set(visited)
    if used > ans:
        return
    elif current >= N:
        print(current, visited, used, queue)
        if used < ans:
            ans = used
    else:
        for picking in range(N):
            if (picking not in visited) and (picking != current):
                visited.add(picking)
                summing(current + 1, visited, used + board[current][picking], queue + [picking])
                visited.remove(picking)


T = int(input())
for case_num in range(1, T + 1):
    ans = 99999999999999999999999
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(case_num, N, board)
    summing(0, set(), 0, [])
    print(f'#{case_num} {ans}')