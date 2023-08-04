# BOJ.
# 설계 의도: 조건에 맞는 실행
# 예전에 비슷한 문제를 설계 했었을 때 처럼,
# 먼저 첫째 줄에 전부 더한 값을 준다.
# 한 줄 내려가면 안먹어요~, 옆으로 가면 먹어요~
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')


def knapsack(i, W, w, p):
    if i <= 0 or W <= 0:
        return 0
    if w[i] > W:
        value = knapsack(i - 1, W, w, p)
        return value
    else:
        left = knapsack(i - 1, W, w, p)
        right = knapsack(i - 1, W - w[i], w, p)
        return max(left, p[i] + right)

N, max_weight = map(int, input().split())
weight = [0]
price = [0]
for get_item in range(N):
    A, B = map(int, input().split())
    weight.append(A)
    price.append(B)
print(knapsack(N, max_weight, weight, price))



"""
pinrt_list = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 13, 13], 
              [0, 0, 0, 0, 8, 8, 13, 13], 
              [0, 0, 0, 6, 8, 8, 13, 14]]
              
"""

#     package_list += [lines]
# package_list.sort(key=lambda x: -(x[1]/x[0]))
# print(package_list)
#
