

# M = 8
# batch_set = set()
# batch_position = [t for t in range(M)]
#
# for i in range(M):
#     for j in range(M):
#         for k in range(M):
#             if i < j < k:
#                 batch_set.add((i, j, k))
# print(batch_position)
# print(batch_set)
# A = [1,2,3,4,5,6,7,8,9]
# line_up = A[1:6]
# print(line_up)
# from collections import deque
#
# base_ground = deque([0, 0, 0])
# print(base_ground)
# base_ground.append(3)
# ace = base_ground.popleft()
# print(sum(base_ground), ace)



N = int(input())
num_list = list(map(int, input().split()))
sum_num = 0
M = max(num_list)
for check in range(N):
    num_list[check] = (num_list[check]/M)*100
    if num_list[check] > 100:
        num_list[check] = 100
    sum_num += num_list[check]
ans = sum_num / N
print(ans)