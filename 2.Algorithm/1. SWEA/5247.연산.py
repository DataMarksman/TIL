# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


# T = int(input())
# for case_num in range(1, T + 1):
#     print(case_num)
#     N, M = map(int, input().split())
#     count = 0
#     small_N = int(N)
#     while True:
#         if N >= M:
#             break
#         small_N = int(N)
#         N *= 2
#         count += 1
#     A = str(N - M)
#     ans_A = int(count) + int(A[0])
#     for sum_A in range(len(A)-1):
#         ans_A += int(A[sum_A+1]) * (10**sum_A)
#     print(count)
#     print(ans_A)
#
#     ans_B = int(count) + int(M-small_N)
#     print(ans_B)
#     ans = ans_A if ans_A < ans_B else ans_B
#     print(f'#{case_num} {ans}')

# T = int(input())
# for case_num in range(1, T + 1):
#
#     N, M = map(int, input().split())
#     count = 0
#     ans = 0
#     small_N = int(N)
#     while True:
#         if N >= M:
#             break
#         small_N = int(N)
#         N *= 2
#         count += 1
#     print('case :', case_num, 'count :', count, 'N :', N, 'samll N ;', small_N)
#     if N == M:
#         ans = int(count)
#     else:
#         ans_A = (count - 1) + (M - small_N)
#         print(ans_A)
#         B_check = str(N - M)
#         print('B_check : ', B_check)
#         ans_B = int(count)
#         ans_B += int(B_check[0]) if int(B_check[0]) <= 5 else (abs(10 - int(B_check[0])) + 1)
#         for sum_B in range(len(B_check)-1):
#             ans_B += int(B_check[sum_B+1]) * (10**sum_B)
#         ans = ans_A if ans_A < ans_B else ans_B
#     print(f'#{case_num} {ans}')
# count = 0
#     Target = bin(M)[2:]
#     mine = bin(N)[2:]
#     for checking in range(len(mine)):


#
# def calculator(K, count):
#     global ans
#     if count > ans or K <= 0 or K:
#         return
#     elif K == N:
#         if count < ans:
#             ans = count
#         return
#     if K + 1 < 1000000:
#         calculator(K + 1, count + 1)
#     if 0 < K - 1:
#         calculator(K - 1, count + 1)
#     if K // 2 > 0:
#         if K % 2 == 0:
#             calculator(K // 2, count + 1)
#         else:
#             calculator((K // 2) + 1, count + 2)
#             calculator((K // 2) - 1, count + 2)
#     if K + 10 < 1000000:
#         calculator(K + 10, count + 1)
#
#
T = int(input())
for case_num in range(1, T + 1):
    N, M = map(int, input().split())
    visited = set()
    count = 0
    stack = {N, }
    while M not in visited:
        stock = set()
        while stack:
            pick = stack.pop()
            A = pick + 1
            B = pick - 1
            C = pick * 2
            D = pick - 10
            if A <= 1000000 and A not in visited:
                stock.add(A)
                visited.add(A)
            if 0 < B and B not in visited:
                stock.add(B)
                visited.add(B)
            if C <= 1000000 and C not in visited:
                stock.add(C)
                visited.add(C)
            if 0 < D and D not in visited:
                stock.add(D)
                visited.add(D)
        stack = set(stock)
        count += 1
    print(f'#{case_num} {count}')










