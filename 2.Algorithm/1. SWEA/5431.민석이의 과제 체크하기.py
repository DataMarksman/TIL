# SWEA.5431. 민석이의 과제 체크하기
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T + 1):
    N, M = tuple(map(int, input().split()))
    score_list = list(map(int, input().split()))
    ans_list = [i for i in range(1, N+1)]
    for erase in range(M):
        ans_list.remove(score_list[erase])
    print(f'#{case_num}', *ans_list)