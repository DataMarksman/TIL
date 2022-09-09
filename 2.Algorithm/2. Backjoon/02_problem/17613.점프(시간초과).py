# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

memo = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,
        2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576,
        2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824,
        2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472]


def jumping(t):
    global max_ans
    count = 0
    while True:
        for jump in range(37):
            if memo[jump]-1 > t:
                count += jump-1
                t -= (memo[jump-1]-1)
                break
        if t <= 0:
            break
    if count > max_ans:
        max_ans = count


T = int(input())
for case_num in range(1, T+1):
    N, M = tuple(map(int, input().split()))
    size = M-N+1
    max_ans = 0
    for x in range(size):
        jumping(int(x+N))
    print(max_ans)
