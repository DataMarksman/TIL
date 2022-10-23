# BOJ. 16437. 양 구출 작전
# 설계 의도: 재귀를 어떻게 써야할지에 대한 고민
# 루트를 전부 커팅하는게 아니라 그냥 한번씩만 밟을 생각으로 하면 되는게 아닐까?
# 재귀로 가장 깊은 곳 부터 들어가면서 DP 처럼 값을 쌓아올린다.
# 1. 값을 받을 때, 해당 노드에 연결되어있는 친구들을 싹다 해당 노드 좌표의 리스트에 넣어준다.
# 2. DFS를 짤 때, 이번 재귀의 연산은 먼저 Depth를 들어간 다음에 시행하도록 하여,
#   이번 Depth의 연산이 가장 나중에 일어나도록 한다.
# 3. 이를 통해 이전까지의 값의 연산이 끝나고 이번 연산이 시행되므로, 해당 노드가 서브 루트 노드가 되어
#   그 아래의 값을 싹다 연산하고 오는 효과를 가진다.
# 4. 이렇게 구해진 값을 출력하면, 따로 커팅하거나 루트 효율화 시키거나 하는 작업이 필요없다.
# 개선점:
# 쉽지 않다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def sheepsDFS(k):
    result = 0
    for idx in tree_list[k]:
        result += sheepsDFS(idx)
    result += island_sum[k]
    if result < 0:
        result = 0
    return result


N = int(input())
tree_list = [[]for _ in range(N+1)]
island_sum = [0]*(N+1)
for put_in in range(2, N+1):
    lines = list(input().split())
    tree_list[int(lines[2])].append(put_in)
    if lines[0] == 'W':
        island_sum[put_in] -= int(lines[1])
    else:
        island_sum[put_in] += int(lines[1])
print(sheepsDFS(1))