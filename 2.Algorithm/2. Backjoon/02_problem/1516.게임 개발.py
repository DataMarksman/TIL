<<<<<<< HEAD
# BOJ.
# 설계 의도: DFS로 구현하는 위상정렬
=======
# BOJ. 1516. 게임 개발
# 설계 의도: DFS 기반의 위상 정렬
# 1. 재귀 함수를 통해, 위상 정렬을 해나가면서 값을 들고 갑니다
# 2. 현재 값과 이미 넣어놓은 값을 비교해서 더 큰 쪽으로 통합 시킵니다.
# 3. 하나가 끝까지 가면, 다시 처음 뽑았던 루트 노드 들 중에 하나 뽑아서 끝까지 진행
>>>>>>> 073580aabcc2df062116a4b420e6a076d6a5e684
# 개선점:
# 1. 자, 이건 DFS 입니다. 재귀입니다. 값 가져갈 때, 갱신 시키는건
#     ans_list 뿐만 아니라 들고 가는 값도 갱신 시켜야 합니다.
import sys
<<<<<<< HEAD
import heapq
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())


=======
input = sys.stdin.readline
def dfs_topol(start, price):
    global edge_list
    global ans_list
    if ans_list[start] < price:
        ans_list[start] = price
    else:
        price = ans_list[start]
    if not edge_list[start]:
        for rooting in range(1, N + 1):
            if start in edge_list[rooting]:
                edge_list[rooting].remove(start)
                dfs_topol(rooting, price + time_list[rooting])


N = int(input())
edge_list = [set() for _ in range(N+1)]
time_list = [0] * (N + 1)
ans_list = [0] * (N + 1)
for put_in in range(1, N + 1):
    line = list(map(int, input().split()))
    time_list[put_in] = line.pop(0)
    line.remove(-1)
    if line:
        edge_list[put_in] |= set(line)
stack = set()
for checking in range(1, N + 1):
    if not edge_list[checking]:
        stack.add(checking)
while stack:
    pick = stack.pop()
    dfs_topol(pick, time_list[pick])
for printing in range(1, N+1):
    print(ans_list[printing])
>>>>>>> 073580aabcc2df062116a4b420e6a076d6a5e684


"""
4
1 -1
1 1 -1
1 1 -1
1 2 3 -1

3
5 -1
10 -1
5 1 2 -1

4
1 4 3 2 -1
2 4 -1
1 4 -1
1 -1

5
10 -1
20 1 -1
30 2 -1
40 3 5 -1
100 -1
== 10 30 60 140 100

4
20 -1
10 -1
1 1 2 -1
1000 1 2 3 -1
== 20 10 21 1021
"""
