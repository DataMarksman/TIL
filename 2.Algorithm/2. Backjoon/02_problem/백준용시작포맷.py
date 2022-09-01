# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

N = int(input())
num_list = list(map(int, input().split()))

N = int(input())
for case_num in range(1,N+1):

    T = int(input())
    for case_num in range(1, T + 1):
        N = int(input())
        n = N - 1
        board = [list(input()) for _ in range(N)]
        re_board = list(map(list, zip(*board)))
        flag = False
        for x in range(N):
            if not flag:
                for y in range(N):
                    if y + 4 < N and board[x][y:y + 5].count("o") >= 5:
                        flag = True
                        break
                    if y + 4 < N and re_board[x][y:y + 5].count("o") >= 5:
                        flag = True
                        break
                    if y + 4 < N and x + 4 < N:
                        for cross_c in range(5):
                            if board[x + cross_c][y + cross_c] != "o":
                                break
                        else:
                            flag = True
                            break

                    if 0 <= y - 4 and x + 4 < N:
                        for cross_c in range(5):
                            if board[x + cross_c][y - cross_c] != "o":
                                break
                        else:
                            flag = True
                            break
        print(f'#{case_num} {"YES" if flag else "NO"}')