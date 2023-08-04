# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
start, goal = map(int, input().split())

if start == goal:
    print(0)
else:
    visited = {start, }
    Q = {start, }
    ans = 0
    get_in = start
    while get_in < 100001:
        get_in *= 2
        Q.add(get_in)
        visited.add(get_in)
    while goal not in visited:
        ans += 1
        temp_Q = set()
        while Q:
            pick = Q.pop()
            visited.add(pick)
            if (pick + 1) not in visited:
                temp_Q.add(pick + 1)
            if pick > 0 and (pick - 1) not in visited:
                temp_Q.add(pick - 1)
            if (pick * 2) not in visited and pick < 100001:
                Q.add(pick*2)
        visited |= set(temp_Q)
        Q = set(temp_Q)
    print(ans)
