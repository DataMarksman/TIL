# 4835. 구간합

T = int(input())
for case_num in range(1,T+1):
  N, M = map(int,input().split())
  num_list = list(map(int,input().split()))
  sum_list = []
  for order in range(N-M+1):
    tmp_sum = 0
    for idx in range(M):
      tmp_sum += num_list[order+idx]
    sum_list += [tmp_sum]
  max_sum = sum_list[0]
  min_sum = sum_list[0]
  for sums in sum_list:
    if sums > max_sum:
      max_sum = sums
    elif sums < min_sum:
      min_sum = sums
  print(f'#{case_num} {max_sum-min_sum}')
  