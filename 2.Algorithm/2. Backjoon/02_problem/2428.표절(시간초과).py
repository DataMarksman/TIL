# BOJ. 2428 표절
# 설계 의도:
# 1. for문 두개 돌리면서 조건에 맞는 케이스 카운팅
# 개선점:
# 인줄 알았는데 시간초과...

N = int(input())
num_list = list(map(int, input().split()))
num_set = set(num_list)
real_list = sorted(list(num_set), reverse=True)
K = len(real_list)
count_list = [0]*100000001
for counting in range(K):
    count_list[real_list[counting]] = num_list.count(real_list[counting])

count = 0
for summing in range(K):
    amount = count_list[real_list[summing]]

    if amount > 1:
        count += (amount * (amount-1))//2
    count += amount * sum(count_list[real_list[summing]-1:int(0.9*real_list[summing]):-1])
print(count)

# for i in range(len(real_list)):
#     for j in range(i, len(real_list)):
#         if i == j and count_list[i] > 1:
#             count += (count_list[i]*(count_list[i]-1))//2
#         elif i < j and 0.9*real_list[j] <= real_list[i]:
#             count += count_list[i]*count_list[j]
# print(count)
