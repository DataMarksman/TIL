# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)
# def mintiple(minti_sum, set_A, set_B, depth):
#     global ans
#     if depth >= N:
#         if minti_sum < ans:
#             ans = minti_sum
#     elif minti_sum < ans:
#         for i in range(N):
#             for j in range(N):
#                 if i not in set_A and j not in set_B:
#                     new_minti_sum = int(minti_sum) + (A_list[i]*B_list[j])
#                     set_A.add(i)
#                     set_B.add(j)
#                     mintiple(new_minti_sum, set_A, set_B, depth + 1)
#                     set_A.remove(i)
#                     set_B.remove(j)


N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
A_list.sort()
B_list.sort(reverse=True)
# ans = 9999999999999999
# mintiple(0, set(), set(), 0)
ans = 0
for muti in range(N):
    ans += A_list[muti]*B_list[muti]
print(ans)

