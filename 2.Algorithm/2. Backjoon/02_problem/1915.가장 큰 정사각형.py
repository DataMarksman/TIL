# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

#
# DP = [[0]*M for _ in range(N)]
# max_size = 0
# for first_x in range(M):
#     if board[0][first_x] == '1':
#         DP[0][first_x] = 1
#         max_size = 1
# for x in range(1, N):
#     for y in range(M):
#         if board[x][y] == '1':
#             DP[x][y] = DP[x - 1][y] + 1
#             if DP[x][y] > max_size:
#                 count = 1
#                 for check_m in range(1, DP[x][y]):
#                     if y - check_m < 0 or DP[x][y] > DP[x][y-check_m]:
#                         break
#                     else:
#                         count += 1
#                 for check_p in range(1, DP[x][y]):
#                     if y + check_p >= M or DP[x][y] > DP[x][y+check_p]:
#                         break
#                     else:
#                         count += 1
#                 if count >= DP[x][y]:
#                     max_size = int(DP[x][y])
# print(max_size**2)





"""
4 4
0100
0111
1111
0011


4 4
0100
0111
1111
1110


4 4
1111
0111
1110
0010


4 4
0000
0000
0000
0000

4 4
1010
0101
1010
0101



"""