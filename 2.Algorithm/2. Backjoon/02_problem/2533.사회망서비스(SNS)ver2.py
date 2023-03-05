# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')


# 자, 이 문제는 Depth를 기반으로 하는 DP 문제다.
# root 노드를 무조건 1로 잡고 시작하겠다.
# 가정은 아래와 같다.
# 1. 리프노드는 무조건 체크하지 않는다.
# 2. 연속으로 3번 체크는 하지 않는다.

# 시작해보자.

N = int(input())
connection = [set() for _ in range(N+1)]
leaf_nodes = set()
for get_edges in range(N-1):
    U, V = map(int, input().split())
    connection[U].add(V)
    connection[V].add(U)
for leaf_check in range(1, N+1):
    if len(connection[leaf_check]) == 1:
        leaf_nodes.add(leaf_check)

visited = set(leaf_nodes)
pick_nodes = set()
pick_flag = True
pick_set = set(leaf_nodes)
while pick_set:
    tmp_set = set()
    if pick_flag:
        while pick_set:
            pick = pick_set.pop()
            tmp_set |= connection[pick]
        pick_set = set(tmp_set - visited)
        pick_nodes |= pick_set
        visited |= pick_set

    else:
        while pick_set:
            pick = pick_set.pop()
            tmp_set |= connection[pick]
        pick_set = set(tmp_set-leaf_nodes)
        visited |= pick_set
print(pick_nodes)
print(len(pick_nodes))




