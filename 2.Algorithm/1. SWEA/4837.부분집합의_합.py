# 4837.  부분 집합의 합

T = int(input())
for case_num in range(1, T + 1):
    N, K = map(int, input().split())
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ans_count = 0
    partial_list = []
    for check in range(1 << 12):
        for pick in range(12):
            if check & (1 << pick):
                partial_list.append(num_list[pick])
    for partial in partial_list:
        if len(partial) == N and sum(partial) == K:
            ans_count += 1
    print(f'#{case_num} {ans_count}')

