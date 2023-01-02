# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# import heapq
# input = sys.stdin.readline
# N, T = map(int, input().split())
# H_queue = []
# for put_in in range(N):
#     A, B = map(int, input().split())
#     heapq.heappush(H_queue, (-B, A))
# ans = 0
# for pulling in range(T-1, -1, -1):
#     X, Y = heapq.heappop(H_queue)
#     ans += (-X)*pulling + Y
#     if not H_queue:
#         break
# print(ans)


import sys
input = sys.stdin.readline
N, T = map(int, input().split())
ans = 0
H_queue = []
for put_in in range(N):
    A, B = map(int, input().split())
    H_queue.append((B, -A))
H_queue.sort(reverse=True)
for pulling in range(0, N):
    ans += H_queue[pulling][0]*(T-pulling-1) - H_queue[pulling][1]
print(ans)


# 36
#


"""
4 : 9
3 : 7
2 : 3
1 : 3
0 : 1



"""