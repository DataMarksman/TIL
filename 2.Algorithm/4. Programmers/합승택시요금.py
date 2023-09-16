# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

from heapq import *
import sys


def solution(n, s, a, b, fares):
    root = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    answer = sys.maxsize
    for A, B, fare in fares:
        root[A][B] = fare
        root[B][A] = fare
    def dijkstra(start):
        dijkstra_heapq = []
        for i in range(1, n + 1):
            if root[start][i] > 0:
                heappush(dijkstra_heapq, (root[start][i], i))
        min_root = [sys.maxsize for _ in range(n + 1)]
        visited = {start, }
        min_root[start] = 0
        while dijkstra_heapq:
            fare, goal = heappop(dijkstra_heapq)
            if goal not in visited:
                visited.add(goal)
                min_root[goal] = fare
                if s in visited and a in visited and b in visited:
                    return min_root[s] + min_root[a] + min_root[b]

                for j in range(1, n + 1):
                    if j not in visited and root[goal][j] != 0:
                        heappush(dijkstra_heapq, (fare + root[goal][j], j))
        return sys.maxsize

    for case in range(1, n + 1):
        case_answer = dijkstra(case)
        answer = min(case_answer, answer)
    return answer


arr = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(6,4,6,2,arr))
