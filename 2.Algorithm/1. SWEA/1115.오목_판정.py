# SWEA.1115 오목 판정
# 설계 목적: for 문 한방으로 전부 처리하자.
# 1. 어짜피 5개가 이어져있나 확인해야하니 슬라이싱 쓰자.
# 2. 세로도 한번에 보려면 zip으로 전치 시킨거 같이 보자
# 3. 대각선은 위, 아래로 5개 이상 뻗을 수 있으면 뻗어보자.
# 개선점:
# 1. 코드가 너무 길다... 단축 가능할까?

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
                if y + 4 < N and board[x][y:y+5].count("o") >= 5:
                    flag = True
                    break
                if y + 4 < N and re_board[x][y:y+5].count("o") >= 5:
                    flag = True
                    break
                if y + 4 < N and x + 4 <N:
                    for cross_c in range(5):
                        if board[x+cross_c][y+cross_c] != "o":
                            break
                    else:
                        flag = True
                        break

                if 0 <= y - 4 and x + 4 < N:
                    for cross_c in range(5):
                        if board[x+cross_c][y-cross_c] != "o":
                            break
                    else:
                        flag = True
                        break
    print(f'#{case_num} {"YES" if flag else "NO"}')