# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)
"""
....0....
.1.2.3.4.
..5...6..
.7.8.9.10.
....11....
"""


def num_check(arr, left):
    global ans
    if ans:
        return
    else:
        arr = arr[:]
        left = left[:]
        if len(left) == 0:
            if arr[0] + arr[2] + arr[5] + arr[7] == 26 and \
                    arr[0] + arr[3] + arr[6] + arr[10] == 26 and \
                    arr[1] + arr[2] + arr[3] + arr[4] == 26 and \
                    arr[7] + arr[8] + arr[9] + arr[10] == 26 and \
                    arr[1] + arr[5] + arr[8] + arr[11] == 26 and \
                    arr[4] + arr[6] + arr[9] + arr[11] == 26:
                ans = arr[:]
        else:
            pick = 0
            for picking in range(12):
                if arr[picking] == 0:
                    pick = int(picking)
                    break
            for recur in range(len(left)):
                copy_arr = arr[:]
                copy_left = left[:]
                copy_arr[pick] = copy_left.pop(recur)
                num_check(copy_arr, copy_left)


alp_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
            'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12}
num_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F',
            7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L'}

num_list = [i for i in range(1, 13)]
empty_list = []
ans = []
for in_put in range(5):
    lines = list(input())
    for checking in range(9):
        if lines[checking] != '.':
            if lines[checking] == 'x':
                empty_list.append(0)
            else:
                empty_list.append(alp_dict[lines[checking]])
                num_list.remove(alp_dict[lines[checking]])

num_check(empty_list, num_list)
print(f'....{num_dict[ans[0]]}....')
print(f'.{num_dict[ans[1]]}.{num_dict[ans[2]]}.{num_dict[ans[3]]}.{num_dict[ans[4]]}.')
print(f'..{num_dict[ans[5]]}...{num_dict[ans[6]]}..')
print(f'.{num_dict[ans[7]]}.{num_dict[ans[8]]}.{num_dict[ans[9]]}.{num_dict[ans[10]]}.')
print(f'....{num_dict[ans[11]]}....')
