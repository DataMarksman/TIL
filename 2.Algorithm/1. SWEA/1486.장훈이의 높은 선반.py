# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
def searching(arr, counting):
    global min_diff
    arr = arr[:]
    counting = int(counting)
    if arr and min_diff > 0:
        for i in range(len(arr)):
            A = arr.pop(0)
            counting += A
            B = abs(height - counting)
            if B < min_diff:
                min_diff = B
                if B == 0:
                    break
            searching(arr, counting)
            arr.append(A)


T = int(input())
for case_num in range(1, T + 1):
    N, height = tuple(map(int, input().split()))
    num_list = list(map(int, input().split()))
    min_diff = 999999999999999
    searching(num_list, 0)
    print(f'#{case_num} {min_diff}')