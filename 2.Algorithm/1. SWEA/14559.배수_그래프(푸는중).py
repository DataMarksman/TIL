# SWEA. 14559. 배수 그래프
# 설계 목적:
# 1.
# 개선점:
# 1. 지금 이대로 진행하면 4중 for 문이다. 효과적인 방법은 없는가?

T = int(input())
for case_num in range(1,T+1):
    N, S, E = map(int, input().split())
    N = int(N)
    start = int(S)
    end = int(E)
    M = int(input())
    multiple_list = []
    for write_in in range(M):
        multiple_list += list(map(int, input().split()))

    count = 0
    while True:
        count += 1
        set_S = set()
        set_E = set()
        for x in range(M):
            if start % multiple_list[x][0] == 0:
                set_S.add(x)
            if end % multiple_list[x][1] == 0:
                set_E.add(x)
        if len(set_S & set_E) >= 1:
            break
        else:
            count += 1
        


