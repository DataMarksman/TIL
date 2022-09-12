# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)
#
#
memo = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023,
        2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575,
        2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]

memo_cut = [0, 1, 2, 2, 3, 4, 4, 3, 4, 5, 5, 6, 7, 7, 6, 4, 5, 6, 6, 7, 8, 8, 7, 8, 9, 9,
            10, 11, 11, 10, 8, 5, 6, 7, 7, 8, 9, 9, 8, 9, 10, 10, 11, 12, 12, 11, 9, 10, 11,
            11, 12, 13, 13, 12, 13, 14, 14, 15, 16, 16, 15, 13, 10, 6, 7, 8, 8, 9, 10, 10, 9, 10, 11, 11, 12, 13, 13, 12, 10, 11, 12, 12, 13, 14, 14, 13, 14, 15, 15, 16, 17, 17, 16, 14, 11, 12, 13, 13, 14, 15, 15, 14, 15, 16, 16, 17, 18, 18, 17, 15, 16, 17, 17, 18, 19, 19, 18, 19, 20, 20, 21, 22, 22, 21, 19, 16, 12, 7]

# k 는 비교할 상수, count_J는 이미 점프한 횟수
def jumping(K, count_J, start):
    global max_ans
    t = start
    while K > 0:
        if K <= 127:
            count_J += memo_cut[K]
            K = 0
        elif K >= memo[t]:
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
    speed_idx = 0
    for first_checking in range(30):
        if N - memo[first_checking] < 0:
            speed_idx = first_checking - 1
            break

    for x in range(size):
        if int(x+N) - memo[speed_idx + 1] >= 0:
            speed_idx += 1
        jumping(int(x+N)-memo[speed_idx], speed_idx, speed_idx)
    print(max_ans)


