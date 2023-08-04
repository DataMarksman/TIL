# BOJ.
# 설계 의도: 조건에 맞는 실행
# 예전에 비슷한 문제를 설계 했었을 때 처럼,
# 먼저 첫째 줄에 전부 더한 값을 준다.
# 한 줄 내려가면 안먹어요~, 옆으로 가면 먹어요~
# 개선점:

N, K = map(int, input().split())
weight_list = []
value_list = []
board = [[0] * (K+1) for _ in range(N+1)]
for put_in in range(N):
    lines = list(map(int, input().split()))
    weight_list += [lines[0]]
    value_list += [lines[1]]
for bag in range(1, N+1):
    for kg in range(1, K+1):
        if weight_list[bag-1] <= kg:
            board[bag][kg] = max(value_list[bag-1]+board[bag-1][kg-weight_list[bag-1]], board[bag-1][kg])
        else:
            board[bag][kg] = board[bag-1][kg]
print(board)
print(board[N][K])
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
