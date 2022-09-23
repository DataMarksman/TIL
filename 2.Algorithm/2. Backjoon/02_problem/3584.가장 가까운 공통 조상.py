# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)


T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    left = [0]*(N+1)
    right = [0]*(N+1)
    parents = [0]*(N+1)
    for put_in in range(N-1):
        A, B = map(int, input().split())
        if left[A]:
            right[A] = B
        else:
            left[A] = B
        parents[B] = A
    target = list(map(int, input().split()))
    start = target[0]
    end = target[1]
    queue_A = {start}
    set_A = set()
    queue_B = {end}
    set_B = set()
    ans = ''
    while not A & B:
        temp_A = set()
        temp_B = set()
        while queue_A:
            pick = queue_A.pop()
            if left[pick]:
                temp_A.add(left[pick])
                if right[pick]:
                    temp_A.add(right[pick])
        while queue_B:
            pick = queue_B.pop()
            if left[pick]:
                temp_B.add(left[pick])
                if right[pick]:
                    temp_B.add(right[pick])
        queue_A = set(temp_A)
        queue_B = set(temp_B)
        if A & B:
            ans = A & B
            break
    print(ans)

