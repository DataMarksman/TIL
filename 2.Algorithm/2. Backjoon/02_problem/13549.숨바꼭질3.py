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
    while goal not in visited:
        ans += 1
        temp_Q = set()
        while Q:
            pick = Q.pop()
            if (pick + 1) not in visited:
                temp_Q.add(pick + 1)
                visited.add(pick + 1)
            if pick > 0 and (pick - 1) not in visited:
                temp_Q.add(pick - 1)
                visited.add(pick - 1)
            if (pick * 2) not in visited and pick < goal + 1:
                Q.add(pick*2)
                visited.add(pick*2)
        Q = set(temp_Q)
    print(ans)
