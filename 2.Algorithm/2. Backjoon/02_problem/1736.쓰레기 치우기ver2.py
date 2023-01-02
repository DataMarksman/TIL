# BOJ. 1736 쓰레기 치우기
# 설계 의도: 딱 한바퀴만 돌거임.
# 1. 2차원 배열 도는 함수를 만들고 2차원 배열 돌면서 각 리스트의 1을 visited로
# 2. 밟았던 visited를 다시 밟으면, 찾는 함수건 도는 2중 for문이건 break 걸어줌. -> 백트래킹

# 개선점: 어예 40ms 1등이당.
# 1. 이걸 죄다 visited에 안넣고 각 리스트별 최대 좌표만 찍어주고 연산으로 뺄 수 있을 듯 함.

# 계단식으로 타고 내려갈 visited 찍기 용 함수
def bf(start_x, start_y):
    for R in range(start_x, N):
        for C in range(start_y, M):
            if board[R][C] == 1:
                if (R, C) not in visited:
                    visited.add((R, C))
                    if C > start_y:
                        start_y = int(C)
                else:
                    break


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = set()
ans = 0
# 2차원 배열을 돌면서, visited 찍어주고, 만약 같은곳 다시 밟으면 바로 다음 행 들어가기.
for X in range(N):
    for Y in range(M):
        if board[X][Y] == 1:
            if (X, Y) not in visited:
                ans += 1
                bf(X, Y)
            break
print(ans)
