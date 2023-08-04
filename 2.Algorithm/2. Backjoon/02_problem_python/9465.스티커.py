# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline


# T = int(input())
# for case_num in range(1, T + 1):
#     N = int(input())
#     list_1 = list(map(int, input().split()))
#     list_2 = list(map(int, input().split()))
#
#     if N == 1:
#         print(max(list_1[0], list_2[0]))
#     else:
#         dp_1 = [list_1[0], (list_1[1]+list_2[0])]
#         dp_2 = [list_2[0], (list_2[1]+list_1[0])]
#         for dp in range(2, N):
#             dp_1.append(list_1[dp]+max(dp_2[dp-2], dp_2[dp-1]))
#             dp_2.append(list_2[dp]+max(dp_1[dp-2], dp_1[dp-1]))
#         print(max(dp_1[N-1], dp_2[N-1]))

T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    list_1 = list(map(int, input().split()))
    list_2 = list(map(int, input().split()))
    if N == 1:
        print(max(list_1[0], list_2[0]))
    else:
        list_1[1] = list_1[1]+list_2[0]
        list_2[1] = list_2[1]+list_1[0]
        for dp in range(2, N):
            list_1[dp] += max(list_2[dp-2], list_2[dp-1])
            list_2[dp] += max(list_1[dp-2], list_1[dp-1])
        print(max(list_1[N-1], list_2[N-1]))