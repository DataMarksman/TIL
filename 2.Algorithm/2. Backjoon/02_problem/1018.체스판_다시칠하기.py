# BOJ.1018 체스판 다시 칠하기
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

N, M = tuple(map(int, input().split()))
count_even = [0, 0]
count_odd = [0, 0]
board = [list(input()) for _ in range(N)]
sum_set = set()
for srch_x in range(N-7):
    for srch_y in range(M - 7):
        count_even = [0, 0]
        count_odd = [0, 0]
        for x in range(8):
            for y in range(8):
                if board[srch_x+x][srch_y+y] == 'W':
                    if (x + y) % 2 == 0:
                        count_even[0] += 1
                    else:
                        count_odd[0] += 1
                elif board[srch_x+x][srch_y+y] == 'B':
                    if (x + y) % 2 == 0:
                        count_even[1] += 1
                    else:
                        count_odd[1] += 1
        sum_set.add(min(count_even[0]+count_odd[1], count_even[1]++count_odd[0]))
print(min(sum_set))
