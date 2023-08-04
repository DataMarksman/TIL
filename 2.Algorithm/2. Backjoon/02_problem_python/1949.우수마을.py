# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
N = int(input())
value_list = [0] + list(map(int, input().split()))
edge_list = [set() for _ in range(N+1)]
for get_nord in range(N-1):
    A, B = map(int, input().split())
    edge_list[A].add(B)
    edge_list[B].add(A)
Q = {1, }
dp_list = []

while Q:
    temp_Q = set()
    temp_dp = 0
    while Q:
        pick = Q.pop()
        temp_dp += value_list[pick]
        while edge_list[pick]:
            add_q = edge_list[pick].pop()
            edge_list[add_q].discard(pick)
            temp_Q.add(add_q)
    Q = set(temp_Q)
    dp_list.append(temp_dp)
dp_list += [0]*2
dp = [[0, 0] for _ in range(len(dp_list))]
dp[0] = [0, dp_list[0]]
dp[1] = [dp_list[0], dp_list[1]]
for check in range(2, len(dp_list)):
    dp[check][1] = dp_list[check] + max(dp[check-1][0], dp[check-2][1])
    dp[check][0] = max(dp[check-1])
print(max(max(dp)))







