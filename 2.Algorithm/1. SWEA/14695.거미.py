# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1,T+1):
    N = int(input())
    idx_list = [list(map(int, input().split())) for _ in range(N)]

    if N == 3:
        print(f'#{case_num} TAK')

