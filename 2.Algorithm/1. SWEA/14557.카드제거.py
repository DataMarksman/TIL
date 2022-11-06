# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T + 1):
    ans = (sum(list(map(int, input())))) % 2
    print(f'#{case_num} {"yes" if ans else "no"}')
