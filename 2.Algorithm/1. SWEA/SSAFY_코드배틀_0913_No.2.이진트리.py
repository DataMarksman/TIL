# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1. 코드 잘못 짬.
# 2. 문제 이해 잘못 함.
# 3. 실전이었으면 이거 1시간 통으로 날린거다.
# 4. 확실하게 조건 전부 정리하고 어떻게 구현할지 고민한 다음에 코드 짜야 손실이 없다.


memo = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,
        2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576,
        2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]


def find_idx(K):
    K = int(K)
    t = 0
    LR = 0
    while True:
        if memo[t] <= K < memo[t+1]:
            if t > 1:
                if memo[t]+(memo[t-1]//2) <= K:
                    LR = 1
            break
        else:
            t += 1
    idx = (t, LR)
    return idx


T = input()
for tc in range(1, T+1):
    N, V = tuple(map(int, input().split()))
    N_idx, N_LR = find_idx(N)
    V_idx, V_LR = find_idx(V)
    diff = 0
    if V_idx == 0:
        ans = N_idx
    else:
        ans = N_idx + V_idx + max(N_LR, V_LR) - 1
    print(f'#{tc} {ans}')



