# SWEA. 4615 재미있는 오셀로 게임
# 설계 목적:
# 1. 8방 탐색을 통해 자기와 다른 색이 있는 칸들을 탐색하고, 다시 같은 색이 나오면 Flag 반환. break
# 2. count 로 자기와 다른 색 몇개인지 카운팅하고, flag 가 True 면, 다시 돌아가서 색칠하기
# 개선점:
# 1. 범위에 N-1 줘 놓고 < 쓰고 있었네.... 반성하십시오!

dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

T = int(input())
for case_num in range(1, T + 1):
    N, M = tuple(map(int, input().split()))
    board = [[0]*N for _ in range(N)]
    board[(N // 2)-1][(N // 2)-1] = 2
    board[N // 2][N // 2] = 2
    board[N // 2][(N // 2)-1] = 1
    board[(N // 2)-1][N // 2] = 1
    color_count = [0, 2, 2]
    for turn in range(M):
        movement = list(map(int, input().split()))
        mx = movement[0] - 1
        my = movement[1] - 1
        color = movement[2]
        board[mx][my] = color
        color_count[color] += 1
        for searching in range(8):
            px = mx + dx[searching]
            py = my + dy[searching]
            flag = False
            count = 0
            while 0 <= px < N and 0 <= py < N:
                if board[px][py] == (color % 2) + 1:
                    count += 1
                    px += dx[searching]
                    py += dy[searching]
                elif board[px][py] == color:
                    flag = True
                    break
                else:
                    break
            if flag and count >= 1:
                px = mx + dx[searching]
                py = my + dy[searching]
                for coloring in range(count):
                    board[px][py] = color
                    color_count[color] += 1
                    color_count[(color % 2) + 1] -= 1
                    px += dx[searching]
                    py += dy[searching]
    print(f'#{case_num}', *color_count[1:])

"""
1
4 12 
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
"""
