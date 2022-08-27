# SWEA.4466. 최대 성적표 만들기
# 설계 목적:
# 1.
# 개선점:
# 1.

T = int(input())
for case_num in range(1, T + 1):
    N, K = tuple(map(int, input().split()))
    score_list = list(map(int, input().split()))
    score_list.sort(reverse=True)
    print(f'#{case_num} {sum(score_list[:K])}')