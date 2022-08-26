# SWEA.농작물 수확하기
# 설계 목적: 자료 받으면서 그냥 합산 하지?
# 1. 2차원 좌표를 가지고 놀 수 있나요?
# 개선점:
# 1. abs(y - x) <= limit_p and limit_p <= x + y <= 3*limit_p: <- 간편화 어떻게?

T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    limit_p = N//2
    count_sum = 0
    for x in range(N):
        write_in = list(input())
        for y in range(N):
            if abs(y - x) <= limit_p and limit_p <= x + y <= 3*limit_p:
                count_sum += int(write_in[y])
    print(f'#{case_num} {count_sum}')
