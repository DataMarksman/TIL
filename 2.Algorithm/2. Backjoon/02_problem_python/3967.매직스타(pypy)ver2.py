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
alp_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
            'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12}

def num_check(arr, left):
    global ans
    if ans:
        return
    else:
        arr = arr[:]
        left = left[:]
        if len(left) == 0:
            if alp_dict[arr[0]] + alp_dict[arr[2]] + alp_dict[arr[5]] + alp_dict[arr[7]] == 26 and \
                    alp_dict[arr[0]] + alp_dict[arr[3]] + alp_dict[arr[6]] + alp_dict[arr[10]] == 26 and \
                    alp_dict[arr[1]] + alp_dict[arr[2]] + alp_dict[arr[3]] + alp_dict[arr[4]] == 26 and \
                    alp_dict[arr[7]] + alp_dict[arr[8]] + alp_dict[arr[9]] + alp_dict[arr[10]] == 26 and \
                    alp_dict[arr[1]] + alp_dict[arr[5]] + alp_dict[arr[8]] + alp_dict[arr[11]] == 26 and \
                    alp_dict[arr[4]] + alp_dict[arr[6]] + alp_dict[arr[9]] + alp_dict[arr[11]] == 26:
                ans = arr[:]
        else:
            pick = 0
            for picking in range(12):
                if arr[picking] == 'x':
                    pick = int(picking)
                    break
            for recur in range(len(left)):
                copy_arr = arr[:]
                copy_left = left[:]
                copy_arr[pick] = copy_left.pop(recur)
                num_check(copy_arr, copy_left)


num_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
empty_list = []
ans = []
for in_put in range(5):
    lines = list(input())
    for checking in range(9):
        if lines[checking] != '.':
            if lines[checking] == 'x':
                empty_list.append('x')
            else:
                empty_list.append(lines[checking])
                num_list.remove(lines[checking])
num_check(empty_list, num_list)
print(f'....{ans[0]}....')
print(f'.{ans[1]}.{ans[2]}.{ans[3]}.{ans[4]}.')
print(f'..{ans[5]}...{ans[6]}..')
print(f'.{ans[7]}.{ans[8]}.{ans[9]}.{ans[10]}.')
print(f'....{ans[11]}....')
