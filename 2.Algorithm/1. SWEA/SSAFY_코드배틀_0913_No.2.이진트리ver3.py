# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1. 코드 잘못 짬.
# 2. 문제 이해 잘못 함.
# 3. 실전이었으면 이거 1시간 통으로 날린거다.
# 4. 확실하게 조건 전부 정리하고 어떻게 구현할지 고민한 다음에 코드 짜야 손실이 없다.
T = int(input())
for tc in range(1, T+1):
    N, V = tuple(map(int, input().split()))
    ans = 0
    while N > 4:
        N /= 2
        ans += 1
    while V > 4:
        V /= 2
        ans += 1
    if V == 3:
        if N == 1:
            ans += 1
        else:
            ans += 2
    elif V == 2:
        ans += 1
    print(f'#{tc} {ans}')


"""
10
1 1
2 1
2 2
6 1
6 2
6 4
6 6
25 7
1000000000 1
1000000000 1000000000

"""