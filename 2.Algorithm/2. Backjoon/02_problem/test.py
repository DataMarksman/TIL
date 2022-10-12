

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
import sys
# input = sys.stdin.readline
T = input()
while T != '0':
    if T == T[::-1]:
        print('yes')
    else:
        print('no')
    T = input()