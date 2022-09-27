# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T + 1):
    lines = list(map(int, input().split()))
    N = lines[0]
    ans = 0
    start = 1
    end = start + lines[start]
    max_dist = end
    while end < N:
        for searching in range(start, end + 1):
            if searching + lines[searching] > max_dist:
                max_dist = searching + lines[searching]

        start = end + 1
        end = max_dist
        ans += 1
    print(f'#{case_num} {ans}')