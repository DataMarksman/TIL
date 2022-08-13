# 3499. 퍼펙트 셔플
T = int(input())
for case_num in range(1,T+1):
    N = int(input())
    deck = list(map(str,input().split()))
    re_deck = [0]*N
    for i in range(N):
        re_deck[i] = deck[(i%2)*((N+1)//2)+(i//2)]
    print(f'#{case_num}',*re_deck)