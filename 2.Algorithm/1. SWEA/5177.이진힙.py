# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    num_list = [0] + list(map(int, input().split()))
    for point in range(2, N+1):
        while point > 1:
            if point >= 2 and num_list[point] < num_list[point//2]:
                num_list[point], num_list[point // 2] = num_list[point // 2], num_list[point]
            point = point//2
    ans = 0
    size = int(N)
    while size > 1:
        size = size//2
        ans += num_list[size]
    print(f'#{case_num} {ans}')