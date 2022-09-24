# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)


T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    parents = [0]*(N+1)
    for put_in in range(N-1):
        A, B = map(int, input().split())
        parents[B] = A
    start, end = map(int, input().split())
    queue_A = {start, }
    set_A = {start, }
    queue_B = {end, }
    set_B = {end, }
    ans = ''
    if start == end:
        ans = start
    while not set_A & set_B:
        temp_A = set()
        temp_B = set()
        while queue_A:
            pick = queue_A.pop()
            if parents[pick]:
                temp_A.add(parents[pick])
                set_A.add(parents[pick])
        while queue_B:
            pick = queue_B.pop()
            if parents[pick]:
                temp_B.add(parents[pick])
                set_B.add(parents[pick])
        queue_A = set(temp_A)
        queue_B = set(temp_B)
        if set_A & set_B:
            ans = set_A & set_B
            break
    print(*ans)

