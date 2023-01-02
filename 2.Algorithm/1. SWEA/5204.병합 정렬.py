# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
def merge_sort(arr, n):
    global ans
    arr = arr[:]
    size = len(arr)
    if size == 1:
        return [arr[0], ]
    else:
        left = arr[:size//2]
        right = arr[size//2:size]
        list_A = merge_sort(left, len(left)) if type(left) == 'list' else [left, ]
        list_B = merge_sort(right, len(right)) if type(right) == 'list' else [right, ]
        if list_A[-1] >= list_B[-1]:
            ans += 1
        merge_list = []
        while list_A and list_B:
            if list_A[0] <= list_B[0]:
                merge_list.append(list_A.pop(0))
            else:
                merge_list.append(list_B.pop(0))
        if list_A:
            merge_list += list_A
        else:
            merge_list += list_B
        return merge_list


T = int(input())
for case_num in range(1, T + 1):
    ans = 0
    N = int(input())
    num_list = list(map(int, input().split()))
    A = merge_sort(num_list, N)
    print(A)
    print(f'#{case_num} {ans}')