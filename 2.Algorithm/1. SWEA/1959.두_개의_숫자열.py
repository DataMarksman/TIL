# SWEA. 1959. 두개의 숫자열
# 설계 목적:
# 1. 쉽다.
# 개선점:
# 1. 문제를 잘 보자... 길이 차이가 주어진다고 했지 N이 더 짧다고 한 적 없다.


T = int(input())
for case_num in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N >= M:
        moving_plate = B
        fixed_plate = A
        N, M = M, N
    else:
        moving_plate = A
        fixed_plate = B

    sum_set = set()
    for checking in range(M-N+1):
        check_sum = 0
        for comparing in range(N):
            check_sum += moving_plate[comparing] * fixed_plate[checking+comparing]
        else:
            sum_set.add(check_sum)
    else:
        ans = max(sum_set)
    print(f'#{case_num} {ans}')
