# BOJ. 17265 인생은 수학이야.
# 설계 의도: DP 설계
# 개선점:
# 우왕 1등이당
import sys
input = sys.stdin.readline
N = int(input())
board = [list(input().split()) for _ in range(N)]

# [최소값, 최대값] 저장용 DP 리스트 만들기
DP = [[['0', '0'] for _ in range(N)] for _ in range(N)]

# DP 첫 값은 첫 값 그대로 가져갑니당
DP[0][0] = [board[0][0], board[0][0]]
for x in range(N):
    for y in range(N):
        # 지금 밟은 칸이 숫자칸이면?
        if board[x][y].isnumeric():
            # 지금 칸에서 가능한 연산 값들을 저장해놓을 리스트
            temp_ans = []

            # 이전 숫자 + 연산자 + 지금 값 계산할 조건 분기

            # 위쪽 연산자 볼 수 있나요?
            if x-1 >= 0:
                # 위쪽 연산자 + 위위 쪽 숫자 계산 가능한가요?
                if x-2 >= 0:
                    # 최소값과 계산한 값과 최대값과 계산한 값 둘다 넣어줍니다.
                    temp_ans.append(eval(DP[x-2][y][0]+board[x-1][y]+board[x][y]))
                    temp_ans.append(eval(DP[x - 2][y][1] + board[x - 1][y] + board[x][y]))
                # 위쪽 연산자 + 위/왼 쪽 숫자 계산 가능한가요?
                if y-1 >= 0:
                    temp_ans.append(eval(DP[x-1][y-1][0]+board[x-1][y]+board[x][y]))
                    temp_ans.append(eval(DP[x - 1][y - 1][1]+ board[x - 1][y] + board[x][y]))
            # 왼쪽 연산자 볼 수 있나요?
            if y-1 >= 0:
                # 왼쪽 연산자 + 왼왼쪽 숫자 계산 가능한가요?
                if y-2 >= 0:
                    temp_ans.append(eval(DP[x][y-2][0]+board[x][y-1]+board[x][y]))
                    temp_ans.append(eval(DP[x][y - 2][1]+ board[x][y - 1] + board[x][y] ))
                # 왼쪽 연산자 + 왼/윗 쪽 숫자 계산 가능한가요?
                if x-1 >= 0:
                    temp_ans.append(eval(DP[x-1][y-1][0]+board[x][y-1]+board[x][y]))
                    temp_ans.append(eval(DP[x - 1][y - 1][1]+ board[x][y - 1] + board[x][y] ))
            # temp 값이 존재하면, 최대값과 최소값을 저장해줍니당~
            if temp_ans:
                DP[x][y] = [str(max(temp_ans)), str(min(temp_ans))]
print(*DP[N-1][N-1])











