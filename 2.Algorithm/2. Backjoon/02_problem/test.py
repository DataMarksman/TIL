

# M = 8
# batch_set = set()
# batch_position = [t for t in range(M)]
#
# for i in range(M):
#     for j in range(M):
#         for k in range(M):
#             if i < j < k:
#                 batch_set.add((i, j, k))
# print(batch_position)
# print(batch_set)
# A = [1,2,3,4,5,6,7,8,9]
# line_up = A[1:6]
# print(line_up)
# from collections import deque
#
# base_ground = deque([0, 0, 0])
# print(base_ground)
# base_ground.append(3)
# ace = base_ground.popleft()
# print(sum(base_ground), ace)
#
# count_list = [0]*30
# str_list = list(input().upper())
# for checking in range(len(str_list)):
#     count_list[ord(str_list[checking])-65] += 1
# ans = 0
# Z = max(count_list)
# position = count_list.index(Z)
# if count_list.count(Z) > 1:
#     print('?')
# else:
#     print(chr(position+65))
#
# N, M = tuple(map(int, input().split()))
# num_list = list(map(int, input().split()))
# ans_list = []
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#              ans_list.append((num_list[i] + num_list[j] + num_list[k])-M)
#
#
#
# num_list = list(int(input()) for _ in range(9))
# print(max(num_list))
# print(num_list.index(max(num_list))+1)
#
# A, B = map(int, input().split())
# B += int(input())
# C = B // 60
# B = B % 60
# A = (A + C) % 24
# print(A, B)


# T = int(input())
# for tc in range(1, T+1):
#     P = input()
#     ans = []
#     for checking in range(len(P)//7):
#         ans.append(int(P[checking*7:(checking*7)+7], 2))
#     print(*ans)

# T = int(input())
# for tc in range(1, T+1):
#     P = input()
#     D = ''
#     ans = []
#     for check in range(len(P)):
#         C = '0000'
#         C += bin(int(P[check], 16))[2:]
#         D += C[len(C)-4:len(C)]
#     for checking in range(len(D) // 7 + 1):
#         ans.append(int(D[checking*7:(checking*7)+7], 2))
#     print(*ans)
# ans_dict = {'001101': 0, '010011': 1, '111011': 2, '110001': 3,
#             '100011': 4, '110111': 5, '001011': 6, '111101': 7,
#             '011001': 8, '101111': 9, }
#
#
# T = int(input())
# for tc in range(1, T+1):
#     P = input()
#     D = ''
#     ans = []
#     for check in range(len(P)):
#         C = '0000'
#         C += bin(int(P[check], 16))[2:]
#         D += C[len(C)-4:len(C)]
#     idx = 0
#     while True:
#         if D[idx:idx+6] in ans_dict:
#             break
#         else:
#             idx += 1
#     for checking in range((len(D) - idx) // 6):
#         ans.append(ans_dict[(D[idx:][checking*6:(checking*6)+6])])
#     print(*ans)
#
#
# """
# 2
# 0DEC
# 0269FAC9A0
# """
#
# month_count = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# ans_list = []
# for i in range(13):
#     ans_list.append(sum(month_count[:i]))
# print(ans_list)
# list_A = [0]*7
# A, B, C = map(int, input().split())
# list_A[A] += 1
# list_A[B] += 1
# list_A[C] += 1
# Max_count = max(list_A)
# if Max_count == 3:
#     print(10000 + A*1000)
# elif Max_count == 2:
#     print(1000 + list_A.index(Max_count) * 100)
# else:
#     print(max(A, B, C)*100)


#
# N = int(input())
# print((N+1)*N//2)



# T = int(input())
# for tc in range(1, T+1):
#     num_list = list(map(int, input().split()))
#     A = sum(num_list[1:])/num_list[0]
#     B = num_list[0]
#     count = 0
#     for checking in range(1, len(num_list)):
#         if num_list[checking] > A:
#             count += 1
#     print(f'{count/B*100: .3f)}%')


#
#
# queue = {(2, 6), (1, 12), (5, 12), (8, 1), (10, 1), }
# queue.discard(min((queue)))
# print(min((queue)))
#
#
# import sys
# input = sys.stdin.readline
# N = int(input())
# str_list = list({input().rstrip() for _ in range(N)})
# str_list.sort(key=lambda x: (len(x), x))
# for printing in range(len(str_list)):
#     print(str_list[printing])

# from fractions import Fraction
# from math import factorial
# import sys

# dc = [0, 1, 0, -1, 1, 1, -1, -1]
# dr = [1, 0, -1, 0, 1, -1, -1, 1]
#
# t = int(input())
# for tc in range(t):
#     N, M = map(int, input().split())
#     o_list = [list(map(int, input().split())) for _ in range(M)]
#     # print(o_list)
#     arr = [['.'] * N for _ in range(N)]
#
#     if N == 4:
#         arr[1][1] = 'W'
#         arr[1][2] = 'B'
#         arr[2][1] = 'B'
#         arr[2][2] = 'W'
#     elif N == 6:
#         arr[2][2] = 'W'
#         arr[2][3] = 'B'
#         arr[3][2] = 'B'
#         arr[3][3] = 'W'
#     elif N == 8:
#         arr[3][3] = 'W'
#         arr[3][4] = 'B'
#         arr[4][3] = 'B'
#         arr[4][4] = 'W'
#
#
#     for i in range(M):
#         y = o_list[i][0] - 1
#         x = o_list[i][1] - 1
#         if o_list[i][2] == 1:
#             arr[x][y] = 'B'
#             for k in range(8):
#                 change_stone = []
#                 if 0 <= x + dr[k] < N and 0 <= y + dc[k] < N:
#                     if arr[x + dr[k]][y + dc[k]] == 'W':
#                         change_stone.append((x + dr[k], y + dc[k]))
#
#                         for g in range(2, N):
#                             if 0 <= x + dr[k] * g < N and 0 <= y + dc[k] * g < N:
#                                 if arr[x + dr[k] * g][y + dc[k] * g] == 'W':
#                                     change_stone.append((x + dr[k] * g, y + dc[k] * g))
#                                 elif arr[x + dr[k] * g][y + dc[k] * g] == 'B':
#                                     for t in range(len(change_stone)):
#                                         r, c = change_stone.pop(0)
#                                         arr[r][c] = 'B'
#                                     break
#                                 else:
#                                     break
#
#         elif o_list[i][2] == 2:
#             arr[x][y] = 'W'
#             for k in range(8):
#                 change_stone = []
#                 if 0 <= x + dr[k] < N and 0 <= y + dc[k] < N:
#                     if arr[x + dr[k]][y + dc[k]] == 'B':
#                         change_stone.append((x + dr[k], y + dc[k]))
#
#                         for g in range(2, N):
#                             if 0 <= x + dr[k] * g < N and 0 <= y + dc[k] * g < N:
#                                 if arr[x + dr[k] * g][y + dc[k] * g] == 'B':
#                                     change_stone.append((x + dr[k] * g, y + dc[k] * g))
#                                 elif arr[x + dr[k] * g][y + dc[k] * g] == 'W':
#                                     for t in range(len(change_stone)):
#                                         r, c = change_stone.pop(0)
#                                         arr[r][c] = 'W'
#                                     break
#                                 else:
#                                     break
#
#     white = 0
#     black = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 'W':
#                 white += 1
#             elif arr[i][j] == 'B':
#                 black += 1
#     print(f'#{tc + 1} {black} {white}')


# N = int(input())
#
# for pick in range(N//10, N):
#     temp = sum(map(int, str(pick)))
#     result = pick + temp
#     if result == N:
#         print(pick)
#         break
# else:
#     print(0)

# import sys
# input = sys.stdin.readline
# T = int(input())
# check_set = set(map(int, input().split()))
# N = int(input())
# num_list = list(map(int, input().split()))
# for printing in range(N):
#     if num_list[printing] in check_set:
#         print(1)
#     else:
#         print(0)



# A, B, K = map(int, input().split())
# if K <= A:
#     print(1)
# else:
#     aim = K - A
#     count = aim//(A-B)
#     if aim%(A-B) > 0:
#         count += 2
#     else:
#         count += 1
#     print(count)

# import sys
# T = int(sys.stdin.readline())
# for tc in range(T):
#     string = list(sys.stdin.readline().rstrip())
#     stack = 0
#     for checking in range(len(string)):
#         if string[checking] == '(':
#             stack += 1
#         else:
#             stack -= 1
#             if stack < 0:
#                 print('NO')
#                 break
#     else:
#         if stack == 0:
#             print('YES')
#         else:
#             print('NO')

# import math
# A, B = map(int, input().split())
# print((math.factorial(A)) // ((math.factorial(A-B))*(math.factorial(B))))


# import heapq
# import sys
# input = sys.stdin.readline
# N = int(input())
# H_queue = []
# for put_in in range(N):
#     line = tuple(map(int, input().split()))
#     heapq.heappush(H_queue, (line[1], line[0]))
# for printing in range(N):
#     pick = heapq.heappop(H_queue)
#     print(pick[1], pick[0])

# import sys
# input = sys.stdin.readline
# N = int(input())
# Queue = []
# for Q in range(N):
#     line = list(input().split())
#     if line[0] == 'push':
#         Queue.append(line[1])
#     elif line[0] == 'front':
#         if Queue:
#             print(Queue[0])
#         else:
#             print(-1)
#     elif line[0] == 'back':
#         if Queue:
#             print(Queue[len(Queue)-1])
#         else:
#             print(-1)
#     elif line[0] == 'pop':
#         if Queue:
#             print(Queue.pop(0))
#         else:
#             print(-1)
#     elif line[0] == 'size':
#         if Queue:
#             print(len(Queue))
#         else:
#             print(0)
#     elif line[0] == 'pop':
#         if Queue:
#             print(Queue.pop(0))
#         else:
#             print(-1)
#     elif line[0] == 'empty':
#         if Queue:
#             print(0)
#         else:
# #             print(1)
#
# t = int(input())
# for tc in range(t):
#     N = int(input())
#     tree = list(map(int, input().split()))
#     # print(tree)
#
#     max_tree = max(tree)
#     day = 0
#     small_tree = []
#     for i in range(N):
#         if tree[i] < max_tree:
#             small_tree.append(tree[i])
#     while small_tree:
#         for x in range(len(small_tree)):
#             if small_tree[x] == max_tree:
#                 small_tree.sort()
#                 small_tree.pop()
#                 break
#
#         if len(small_tree) == 0:
#             break
#         for j in range(len(small_tree)):
#             if max_tree - small_tree[j] == 1:
#                 if day % 2 == 0:
#                     small_tree[j] += 1
#                     day += 1
#                     break
#             elif max_tree - small_tree[j] == 2:
#                 if day % 2 == 1:
#                     small_tree[j] += 2
#                     day += 1
#                     break
#
#             if max_tree - small_tree[j] > 2:
#                 if day % 2 == 0:
#                     small_tree[j] = small_tree[j] + 1
#                     day += 1
#                     break
#                 elif day % 2 == 1:
#                     small_tree[j] = small_tree[j] + 2
#                     day += 1
#                     break
#         else:
#             day += 1
#
#     print(f'#{tc+1} {day}')
#
#
#
# """
# 10
# 10
# 9 9 9 9 9 9 9 9 9 10
# 10
# 8 9 9 9 9 9 9 9 9 10
# 10
# 7 9 9 9 9 9 9 9 9 10
# 10
# 7 7 7 7 7 7 9 9 9 10
# 10
# 8 8 8 8 8 8 8 8 8 10
# 2
# 1 1
# 3
# 1 1 100
# 100
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 3
# 10
# 1 2 1 2 1 2 1 2 1 3
# 10
# 1 9 9 9 9 9 9 9 9 10
#
#
# #1 17
# #2 15
# #3 17
# #4 17
# #5 12 [
# #6 0
# #7 132
# #8 132 [
# #9 10
# #10 17 [
# < 다솔 쓰 답 >
# #1 17
# #2 15
# #3 17
# #4 17
# #5 18 [
# #6 0
# #7 132
# #8 198 [
# #9 10
# #10 21 [
# 1 2 1 / 2 1 1 / 2
#
# """
#

#
#
# import sys
# input = sys.stdin.readline
# N = int(input())
# info = [list(map(int, input().split())) for _ in range(N)]
# price = []
# for r in range(N):
#     for c in range(N):
#         if r == 0 or r == N - 1:
#             continue
#         elif c == 0 or c == N - 1:
#             price.append(3001)
#         else:
#             temp = info[r][c] + info[r - 1][c] + info[r + 1][c] + info[r][c - 1] + info[r][c + 1]
#             price.append(temp)
# ans = 3000
# for i in range(N*(N-2)):
#     visited_i = {i+N, i+N-1, i+N, i+N+1, i+2*N, }
#     if price[i] > ans:
#         continue
#     for j in range(i+3, N*(N-2)):
#         if j in visited_i or price[i]+price[j] > ans:
#             continue
#         visited_j = {j+N, j+N-1, j+N, j+N+1, j+2*N, }
#         for k in range(j+3, N*(N-2)):
#             if k in visited_i or k in visited_j:
#                 continue
#             elif ans > price[i]+price[j]+price[k]:
#                 ans = price[i]+price[j]+price[k]
# print(ans)
#
#
#
#

# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# for x in range(N):
#     line = list(map(int, input().split()))
#     for y in range(M):
#         board[x][y] += line[y]
# for printing in range(N):
#     print(*board[printing])

# import sys
# input = sys.stdin.readline
# max_ans = -1
# idx = (0, 0)
# for x in range(1, 10):
#     line = list(map(int, input().split()))
#     for y in range(9):
#         if line[y] > max_ans:
#             max_ans = int(line[y])
#             idx = (x, y+1)
# print(max_ans)
# print(*idx)

#
# import sys
# input = sys.stdin.readline
# A, B, C = map(int, input().split())
# if B >= C:
#     print(-1)
# elif A == 0 and C > B:
#     print(1)
# else:
#     ans = A//(C-B)
#     ans += 1
#     print(ans)
#
#
#


# import sys
# input = sys.stdin.readline
# N = int(input())
# ans = 0
# for text in range(N):
#     line = list(input())
#     check_set = {line[0]}
#     for check in range(1, len(line)):
#         if line[check] == line[check-1]:
#             pass
#         elif line[check] in check_set:
#             break
#         else:
#             check_set.add(line[check])
#     else:
#         ans += 1
# print(ans)

# # import sys
# # input = sys.stdin.readline
# # N = int(input())
# # pick = 1
# # ans = 0
# # while True:
# #     if N - pick <= 0:
# #         ans = N
# #         break
# #     else:
# #         N -= pick
# #         pick += 1
# # short = pick - N + 1
# # if pick % 2 != 0:
# #     ans, short = short, ans
# # print(f'{ans}/{short}')
#
# original = { '5', '6', '7', '8', '9', '1', '2', '3', '4',}
# print(sorted(original))


#
# import sys
# input = sys.stdin.readline
# A, B = map(int, input().split())
# ans = A // B
# print(ans)
# print(A - (ans*B))


# import sys
# input = sys.stdin.readline
# from collections import deque
# n = int(input())
# q = deque([])
# for i in range(n):
#     s = input().split()
#     if s[0] == 'push':
#         q.append(s[1])
#     elif s[0] == 'pop':
#         if not q:
#             print(-1)
#         else:
#             print(q.popleft())
#     elif s[0] == 'size':
#         print(len(q))
#     elif s[0] == 'empty':
#         if not q:
#             print(1)
#         else:
#             print(0)
#     elif s[0] == 'front':
#         if not q:
#             print(-1)
#         else:
#             print(q[0])
#     elif s[0] == 'back':
#         if not q:
#             print(-1)
#         else:
#             print(q[-1])

# import sys
# input = sys.stdin.readline
#
#
# fibo = [0 for _ in range(1500000)]
# N = int(input())
# fibo[0:1] = [0, 1]
#
# if N < 0:
#     for i in range(-1, N - 1, -1):
#         data = fibo[i+2] - fibo[i+1]
#         if data < 0:
#             fibo[i] = (abs(data) % 1000000000) * -1
#         else:
#             fibo[i] = data % 1000000000
#     if fibo[N] < 0:
#         print(-1)
#         print(fibo[N] * -1)
#     else:
#         print(1)
#         print(fibo[N])
#
#
# elif N > 0:
#     for i in range(2, N + 1):
#         fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 1000000000
#
#     print(1)
#     print(fibo[N])
#
# else:
#     print(0)
#     print(0)

#
#
#
# import sys
# input = sys.stdin.readline
# N = int(input())
# Queue = []
# for checking in range(N):
#     pick = int(input())
#     if pick == 0:
#         Queue.pop()
#     else:
#         Queue.append(pick)
# print(sum(Queue))





#
# import sys
# N, M = map(int, input().split())
#
# pokemon = {}
# for get in range(1, N+1):
#     pick = sys.stdin.readline().strip()
#     pokemon[pick] = str(get)
#     pokemon[str(get)] = pick
#
# for solve in range(M):
#     Q = sys.stdin.readline().strip()
#     print(pokemon[Q])

#
# import sys
# input = sys.stdin.readline
# N = int(input())
#
# fibo = 1
# ans = 1
# while N > fibo:
#     fibo += 6 * ans
#     ans += 1
# print(ans)

# pick = 'abcd'
# print(pick[:1])





A = [1,2,3,4,5]
print(A[:-1])



