# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    count = 1
    ans = ''
    flag = True
    while N > 0 and flag:
        if count >= 13:
            flag = False
            break
        if N >= (1/2)**count:
            N -= (1/2)**count
            ans += '1'
        else:
            ans += '0'
        count += 1
    if flag:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} overflow')
