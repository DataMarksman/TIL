# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)


memo = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023,
        2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575,
        2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]


# k 는 비교할 상수, count_J는 이미 점프한 횟수
def jumping(K, count_J):
    global max_ans
    t = 30
    while K > 0:
        if K >= memo[t]:
            K -= memo[t]
            count_J += t
        else:
            t -= 1
    if count_J > max_ans:
        max_ans = count_J


T = int(input())
for case_num in range(1, T+1):
    N, M = tuple(map(int, input().split()))
    size = M-N+1
    max_ans = 0
    for x in range(size):
        jumping(int(x+N), 0)
    print(max_ans)
