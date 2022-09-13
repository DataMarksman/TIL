# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

def in_order(N):
    global ans
    if N:
        in_order(ch_1[N])
        ans += word_list[N]
        in_order(ch_2[N])


T = 10
for tc in range(1, T+1):
    N = int(input())
    ch_1 = [0] * (N + 1)
    ch_2 = [0] * (N + 1)
    word_list = ['']*(N+1)
    ans = str()
    for put_in in range(1, N+1):
        line = list(map(str, input().split()))
        if len(line) == 4:
            ch_1[int(line[0])] = int(line[2])
            ch_2[int(line[0])] = int(line[3])
        elif len(line) == 3:
            ch_1[int(line[0])] = int(line[2])
        word_list[int(line[0])] = line[1]
    in_order(1)
    print(f'#{tc} {ans}')