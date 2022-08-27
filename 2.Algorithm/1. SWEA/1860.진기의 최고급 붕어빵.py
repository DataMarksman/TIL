# SWEA. 1860 진기의 최고급 붕어빵
# 설계 목적: range를 얼마나 잘 쓰는지 물어보는 문제
# 1. range로 만든 i에 조건을 주어서, 리스트의 각 idx가 지난 시간을 의미하게 함.
#   -> 즉 idx의 값을 잘 표현하면,
#   = 시간을 붕어빵 만드는 단위시간으로 나눈 몫 * 단위 시간당 만들 수 있는 빵 개수
#       로 표시할 수 있게 되는 것이다.
# 2. 그리고 손님들이 오는 시간을 오름차순으로 정렬하면, 손님 리스트의 idx가 현재까지 온 손님들의 수 -1이 되므로,
#   이를 +1해서 반영하면, 해당 시간 idx에서 도출한 해당 시간에 만들어놓은 빵의 개수에서
#   손님들이 가져간 붕어빵의 개수를 빼는 것으로 possible 여부를 도출 가능하다.
# 개선점:
# 1. 아직은 몰?루

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T + 1):
    N, M, K = tuple(map(int, input().split()))
    customer = list(map(int, input().split()))
    customer.sort()
    limit_c = customer[N-1]
    making_list = [(i//M)*K for i in range(limit_c + 1)]
    flag = True
    for check in range(N):
        if making_list[customer[check]] - (check+1) < 0:
            flag = False
            break
    if flag:
        print(f'#{case_num} Possible')
    else:
        print(f'#{case_num} Impossible')
