# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:



# 위상정렬과 DP를 섞어보겠습니다
# 각 노드에서 다음 노드로 진입하는 조건은 다음 노드가 자기가 가진 자식 노드를 전부 소진했을 때 입니다.
# 쉽게 말해서

# 시작해보자.
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.setrecursionlimit(10**6)
N = int(input())
connection = [[] for _ in range(N+1)]
for edges in range(N-1):
    A, B = map(int, input().split())
    connection[A].append(B)
    connection[B].append(A)

def tree_dp(parent, node):
    if connection[node] == [parent]:
        return (1, 0)
    dp_EA = 1
    dp_non_EA = 0
    for checking in connection[node]:
        if checking != parent:
            EA, non_EA = tree_dp(node, checking)
            dp_EA += min(EA, non_EA)
            dp_non_EA += EA
    return (dp_EA, dp_non_EA)

answer = min(tree_dp(0, 1))
print(answer)

