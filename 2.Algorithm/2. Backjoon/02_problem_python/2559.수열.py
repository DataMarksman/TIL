# BOJ.2559 수열
# 설계 의도: 누적합 개념을 적용? 이전꺼 빼고 다음거 더하고~
# 개선점:
# 1. 변수 N개 (N>1)를 받을 때, int 로 받되, map 처럼 휘발성 없게 받으려면?

N, K = map(int, input().split())
num_list = list(map(int, input().split()))
ans_list = [sum(num_list[:K])]
tmp_sum = sum(num_list[:K])
for idx in range(N-K):
    tmp_sum += (num_list[idx + K] - num_list[idx])
    ans_list += [tmp_sum]
print(max(ans_list))