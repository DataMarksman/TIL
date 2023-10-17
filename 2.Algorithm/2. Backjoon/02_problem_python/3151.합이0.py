# # BOJ.
# # 설계 의도: 조건에 맞는 실행
# # 개선점:
# import sys
# # sys.setrecursionlimit(10**6)
# input = lambda: sys.stdin.readline().rstrip('\r\n')
# N = int(input())
# num_list = list(map(int, input().split()))
# number_dict = dict()
# under_set = set()
# upper_set = set()
# zero_flag = False
#
# for num in num_list:
#     if num in number_dict.keys():
#         number_dict[num] += 1
#     else:
#         number_dict[num] = 1
#     if num > 0:
#         upper_set.add(num)
#     elif num < 0:
#         under_set.add(num)
#     else:
#         zero_flag = True
#
# under_list = list(under_set)
# upper_list = list(upper_set)
# answer = 0
# for i in range(len(upper_list)):
#     left_numb = upper_list[i]
#     left_cnt = number_dict[left_numb]
#     double_numb = -(left_numb * 2)
#     if double_numb in under_set:
#         answer += left_cnt * (left_cnt-1) * number_dict[double_numb] // 2
#         # print('number:', left_numb, left_numb, double_numb)
#         # print('ncount:', left_cnt, left_cnt - 1, number_dict[double_numb])
#         # print('answer:', answer)
#     if zero_flag and -left_numb in under_set:
#         answer += left_cnt * number_dict[0] * number_dict[-left_numb]
#         # print('number:', left_numb, -left_numb, 0)
#         # print('ncount:', left_cnt, number_dict[-left_numb], number_dict[0])
#         # print('answer:', answer)
#
#     for j in range(i+1, len(upper_list)):
#         right_numb = upper_list[j]
#         right_cnt = number_dict[right_numb]
#
#         combine_numb = -(left_numb + right_numb)
#         if combine_numb in under_set:
#             answer += left_cnt * right_cnt * number_dict[combine_numb]
#             # print('number:', left_numb, right_numb, combine_numb)
#             # print('ncount:', left_cnt, right_cnt, number_dict[combine_numb])
#             # print('answer:', answer)
#
# for i in range(len(under_list)):
#     left_numb = under_list[i]
#     left_cnt = number_dict[left_numb]
#     double_numb = -(left_numb * 2)
#     if double_numb in upper_set:
#         answer += left_cnt * (left_cnt - 1) * number_dict[double_numb] // 2
#         # print('number:', left_numb, left_numb, double_numb)
#         # print('ncount:', left_cnt, left_cnt - 1, number_dict[double_numb])
#         # print('answer:', answer)
#
#     for j in range(i+1, len(under_list)):
#         right_numb = under_list[j]
#         right_cnt = number_dict[right_numb]
#
#         combine_numb = -(left_numb + right_numb)
#         if combine_numb in upper_set:
#             answer += left_cnt * right_cnt * number_dict[combine_numb]
#             # print('number:', left_numb, right_numb, combine_numb)
#             # print('ncount:', left_cnt, right_cnt, number_dict[combine_numb])
#             # print('answer:', answer)
# if zero_flag and number_dict[0] >= 3:
#     zero_cnt = number_dict[0]
#     answer += zero_cnt * (zero_cnt-1) * (zero_cnt-2) // 6
# print(answer)
#
# """
# 10
# 2 -5 2 3 -4 7 -4 0 1 -6
# """

# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())
num_list = list(map(int, input().split()))
number_dict = dict()
under_set = set()
upper_set = set()
zero_flag = False

for num in num_list:
    if num in number_dict.keys():
        number_dict[num] += 1
    else:
        number_dict[num] = 1
    if num > 0:
        upper_set.add(num)
    elif num < 0:
        under_set.add(num)
if 0 in number_dict.keys():
    zero_flag = True

under_list = list(under_set)
upper_list = list(upper_set)
answer = 0
if zero_flag:
    for i in range(len(upper_list)):
        left_numb = upper_list[i]
        left_cnt = number_dict[left_numb]
        double_numb = -(left_numb * 2)
        if double_numb in under_set:
            answer += left_cnt * (left_cnt-1) * number_dict[double_numb] // 2
        if zero_flag and -left_numb in under_set:
            answer += left_cnt * number_dict[0] * number_dict[-left_numb]
        for j in range(i+1, len(upper_list)):
            right_numb = upper_list[j]
            right_cnt = number_dict[right_numb]
            combine_numb = -(left_numb + right_numb)
            if combine_numb in under_set:
                answer += left_cnt * right_cnt * number_dict[combine_numb]
    for i in range(len(under_list)):
        left_numb = under_list[i]
        left_cnt = number_dict[left_numb]
        double_numb = -(left_numb * 2)
        if double_numb in upper_set:
            answer += left_cnt * (left_cnt - 1) * number_dict[double_numb] // 2
        for j in range(i+1, len(under_list)):
            right_numb = under_list[j]
            right_cnt = number_dict[right_numb]
            combine_numb = -(left_numb + right_numb)
            if combine_numb in upper_set:
                answer += left_cnt * right_cnt * number_dict[combine_numb]
    if number_dict[0] >= 3:
        zero_cnt = number_dict[0]
        answer += zero_cnt * (zero_cnt-1) * (zero_cnt-2) // 6
    print(answer)
else:
    for i in range(len(upper_list)):
        left_numb = upper_list[i]
        left_cnt = number_dict[left_numb]
        double_numb = -(left_numb * 2)
        if double_numb in under_set:
            answer += left_cnt * (left_cnt-1) * number_dict[double_numb] // 2
        for j in range(i+1, len(upper_list)):
            right_numb = upper_list[j]
            right_cnt = number_dict[right_numb]
            combine_numb = -(left_numb + right_numb)
            if combine_numb in under_set:
                answer += left_cnt * right_cnt * number_dict[combine_numb]
    for i in range(len(under_list)):
        left_numb = under_list[i]
        left_cnt = number_dict[left_numb]
        double_numb = -(left_numb * 2)
        if double_numb in upper_set:
            answer += left_cnt * (left_cnt - 1) * number_dict[double_numb] // 2
        for j in range(i+1, len(under_list)):
            right_numb = under_list[j]
            right_cnt = number_dict[right_numb]
            combine_numb = -(left_numb + right_numb)
            if combine_numb in upper_set:
                answer += left_cnt * right_cnt * number_dict[combine_numb]
    print(answer)

"""
10
2 -5 2 3 -4 7 -4 0 1 -6
"""