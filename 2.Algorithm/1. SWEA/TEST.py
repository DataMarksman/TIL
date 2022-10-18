# 이것은 간략하게 코드 돌려보기 위한 용도의 TEST.py 입니다.

# aa = {'0': 'AA','1': 'BB','2': 'CC'}

# print(aa.get('AA'))
"""
def combination(arr, n):
    result = []
    if n == 0:
        return [result]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result


list_A = [0, 1, 2, 3]
for j in range(len(list_A)):
    print(combination(list_A, j))
"""

"""
def test(x):
    list_A = []
    count = 0
    if x < 10:
        count += 1
        list_A += [x]
        test(x+1)
    else:
        return [list_A]


print(test(1))
"""

"""
in_case = ['(', '[', '{', '<', ' ']
out_case = []
if '{' in in_case:
    print('hi')
out_case += [in_case.pop()]
print(out_case)
"""
"""
list_A = [0,1,2,3,4,5,60,7,8,9,10]
target = max(list_A)
position = list_A.index(target)
for selling in range(position+1):
    list_A.pop(position-selling)
print(list_A[position::-1])
"""
"""
list_A = [[1,2,3,4,5],[1,2,3,4,5,6,7]]
print(list_A[0:2][2])
"""
# M = 5
# batch_position = [i for i in range(M)]
# print(batch_position)
#
# K = 5
# if 1 in range(K-4, K+4):
#     print(range(K-4, K+4))
#     print('hi')
# def pre_order(N):
#     global ans_list
#     if N:
#         ans_list.append(N)
#         pre_order(ch_1[N])
#         pre_order(ch_2[N])
#
#
# N = int(input())
# tree_list = list(map(int, input().split()))
# ch_1 = [0] * (N+1)
# ch_2 = [0] * (N+1)
# ans_list = []
#
# for checking in range(N-1):
#     if ch_1[tree_list[checking*2]] == 0:
#         ch_1[tree_list[checking*2]] = tree_list[(checking*2) + 1]
#     else:
#         ch_2[tree_list[checking*2]] = tree_list[(checking*2) + 1]
# pre_order(1)
# print(ans_list)
# byte_mask = [1, 2, 4, 8, 16, 32, 64, 128, 256]

# T = int(input())
#
# for _ in range(T):
#     arr = input()
#     binary = []
#     ans = []
#
#     while arr:
#         binary = int(arr[:7], 2)
#         decimal = 0
#         print(binary)
#         for i in range(7):
#             if binary & (1 << i):
#                 print(binary, i, 1 << i)
#                 decimal += 2 ** i
#         else:
#             ans.append(decimal)
#
#         arr = arr[7:]
#     print(ans)
#
# """
# 2
# 00000010001101
# 0000000111100000011000000111100110000110000111100111100111111001100111
#
# """


# T = int(input())
# for tc in range(1, T+1):
#     N, string = input().split()
#     ans = ''
#     for changing in range(int(N)):
#         A = '0000'
#         A += bin(int(string[changing], 16))[2:]
#         ans += A[len(A)-4:]
#     print(f'#{tc} {ans}')
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = float(input())
#     count = 1
#     ans = ''
#     flag = True
#     while N > 0 and flag:
#         if count >= 13:
#             flag = False
#             break
#         if N >= (1/2)**count:
#             N -= (1/2)**count
#             ans += '1'
#         else:
#             ans += '0'
#         count += 1
#     if flag:
#         print(f'#{tc} {ans}')
#     else:
#         print(f'#{tc} overflow')
#
#
# #
#
# list_A = [1, 2, 3, 4, 5, 6, 8]
# for i in range(len(list_A)-2):
#     print(sum(list_A[i:i+3]))
#
#
# def setting(x, y, d, p, numbering):
#     global board
#     for fill_X in range(x - d, x + d + 1):
#         for fill_Y in range(y - d, y + d + 1):
#             Plus = (fill_X-x) + (fill_Y-y)
#             Minus = (fill_X-x) - (fill_Y-y)
#             if 0 <= fill_X < 10 and 0 <= fill_Y < 10 and -d <= Plus <= d and -d <= Minus <= d:
#                 board[fill_X][fill_Y] += p
#
#
# board = [[0]*10 for _ in range(10)]
# setting(4, 4, 2, 10, 1)
# for printing in range(10):
#     print(board[printing])
#
# import sys
# input = sys.stdin.readline
# N = int(input().rstrip())
# for p in range(N):
#     A, B = input().split()
#     print(int(A) + int(B))
#
#

# A = {1,2,3,4,5,6, }
# print({7, 9} & A)
#
# print(A)
#
#
# import sys
# input = sys.stdin.readline
# T = int(input())
# for tc in range(1, T+1):
#     num_list = list(map(int, input().split()))
#     A = sum(num_list[1:])/num_list[0]
#     B = num_list[0]
#     count = 0
#     for checking in range(1, len(num_list)):
#         if num_list[checking] > A:
#             count += 1
#     ans = (count/B)*100
#     print(f'{ans:.3f}%')



dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())  # N이 세로, M이 가로
cheese = [list(map(int, input().split())) for _ in range(N)]
# print(cheese)


cnt = 0
flag = True
real_cheese_cnt = [0]
q = [(0, 0), ]

while True:
    cheese_cnt = 0
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 3:
                q.append((i, j))
                cheese[i][j] = 0
    melting = set()
    while q:
        x, y = q.pop(0)
        for k in range(4):
            if 0 <= x+dr[k] < N and 0 <= y+dc[k] < M:
                if cheese[x+dr[k]][y+dc[k]] == 0:
                    cheese[x+dr[k]][y+dc[k]] = 2
                    q.append((x+dr[k], y+dc[k]))
                elif cheese[x+dr[k]][y+dc[k]] == 1:
                    melting.add((x+dr[k], y+dc[k]))

    for pick in range(len(melting)):
        r, c = melting.pop()
        cheese[r][c] = 3
        cheese_cnt += 1

    if cheese_cnt == 0:
        flag = False
        break

    cnt += 1
    real_cheese_cnt.append(cheese_cnt)

    for ch in cheese:
        print(*ch)
    print()
    print(real_cheese_cnt)
print(cnt)
print(real_cheese_cnt[-1])