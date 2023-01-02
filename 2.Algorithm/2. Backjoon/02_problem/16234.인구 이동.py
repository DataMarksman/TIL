# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, L, R = map(int, input().split())
person = [list(map(int, input().split())) for _ in range(N)]


cnt = 0
flag = True
while flag:
    visited2 = set()
    flag = False
    q = []
    for r in range(N):
        for c in range(N):
            if (r, c) not in visited2:
                visited = {(r, c), }
                q = {(r, c), }
                visited2.add((r, c))
                population = 0
                while q:
                    x, y = q.pop()
                    population += person[x][y]
                    for k in range(4):
                        kr = x+dr[k]
                        kc = y+dc[k]
                        if 0 <= kr < N and 0 <= kc < N and (kr, kc) not in visited2:
                            if L <= abs(person[x][y] - person[kr][kc]) <= R:
                                q.add((kr, kc))
                                visited.add((kr, kc))
                                visited2.add((kr, kc))
                avg = int(population/len(visited))
                while visited:
                    a, b = visited.pop()
                    if person[a][b] != avg:
                        flag = True
                    person[a][b] = avg
    cnt += 1
print(cnt-1)