# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
def get_position(dist_sum, depth, checked, start):
    global min_sum
    global checked_sum

    if depth >= K:
        if sum(dist_sum) <= min_sum:
            min_sum = sum(dist_sum)
            check_sum = 0
            for checking in range(K):
                if checking in checked:
                    S = checked.index(checking)
                    E = len(checked) - checked[::-1].index(checking) - 1
                    check_sum += abs(d_list[S] - d_list[E])
            if check_sum < checked_sum:
                checked_sum = check_sum
    else:
        for locating in range(start, max_po + 1):
            new_sum = dist_sum[:]
            new_checked = checked[:]
            for setting in range(N):
                A = abs(locating - d_list[setting])
                if A < dist_sum[setting]:
                    new_sum[setting] = A
                    new_checked[setting] = depth
            else:
                if new_sum < dist_sum:
                    new_start = locating
                    get_position(new_sum, depth + 1, new_checked, new_start)


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    K = int(input())
    d_list = list(map(int, input().split()))
    d_list.sort()
    min_po = min(d_list)
    max_po = max(d_list)
    min_sum = 9999999999999999999999
    checked_sum = 999999999999999999999
    first_start = d_list[0]
    get_position([9999999999999]*N, 0, [0]*N,first_start)
    print(f'#{case_num} {checked_sum}')
