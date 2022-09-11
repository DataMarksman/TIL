# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)


memo = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023,
        2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575,
        2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823,
        2147483647, 4294967295, 8589934591, 17179869183, 34359738367, 68719476735, 137438953471]


# k 는 비교할 상수, count_J는 이미 점프한 횟수, start는 이전 점프대 위치
def jumping(k, count_J , start):
    global max_ans
    if count_J == 0:
        for jump in range(37):
            if memo[jump] > k:
                count_J += (jump-1)
                k -= memo[jump-1]
                jumping(k, count_J, jump)
                break

    else:
        for jump_2nd in memo[start:-1:-1]:
            if jump_2nd <= k:
                k -= jump_2nd
                count_J += start -1

            else:
                start -= 1





    if count > max_ans:
        max_ans = count






T = int(input())
for case_num in range(1, T+1):
    N, M = tuple(map(int, input().split()))
    size = M-N+1
    max_ans = 0
    for x in range(size):
        jumping(int(x+N), 0, 0)
    print(max_ans)
