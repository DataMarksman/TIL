# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
from math import comb
N = int(input())
if N <= 3:
    print(0)
elif N == 4:
    print(13)
elif N == 51:
    print(52)
elif N == 52:
    print(1)
else:
    def poker_cases(N):
        total_cases = 0
        max_sets = N // 4
        flag = 1
        for k in range(1, max_sets + 1):
            total_cases += comb(13, k) * comb(52 - 4 * k, N - 4 * k) * flag
            flag = - flag
        return total_cases % 10007
    print(poker_cases(N))

# Q=[0,0,0,0,13,624,4657,4694,7698,952,4330,6075,4566,7393,9798,2532,1668,5707,6494,1451,
#    5610,360,9054,7264,6421,735,7912,8538,1577,5488,3779,3700,8588,6127,7780,5472,
#    789,1634,6898,9133,2342,5811,7955,1850,1743,977,4282,7147,536,2086,1326,52,1]
# print(Q[int(input())])