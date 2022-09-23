# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.
def searching(start, tall_sum):
    global min_diff
    if min_diff == 0 or tall_sum - height > min_diff:
        return
    elif tall_sum >= height:
        if tall_sum - height < min_diff:
            min_diff = tall_sum - height
            return
    else:
        for checking in range(start, N):
            searching(checking+1, tall_sum + num_list[checking])


T = int(input())
for case_num in range(1, T + 1):
    N, height = map(int, input().split())
    num_list = list(map(int, input().split()))
    min_diff = 999999999
    searching(0, 0)
    print(f'#{case_num} {min_diff}')