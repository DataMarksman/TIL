# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


def solution(board, flag, idx):
    if flag:
        pick = board[idx].pop()
        board[idx].insert(0, pick)
        return board
    else:
        result = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                result[j][N-1 - i] = board[i][j]
        return result


T = int(input())
for tc in range(T):
    data = list(map(int, input().split()))
    if data[0] == 1:
        numb = data[1]
        board = solution(board, True, int(numb)-1)
    else:
        board = solution(board, False, 0)

for output in range(N):
    print(*board[output])
