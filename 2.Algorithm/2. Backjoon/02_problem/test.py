

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

count_list = [0]*30
str_list = list(input().upper())
for checking in range(len(str_list)):
    count_list[ord(str_list[checking])-65] += 1
ans = 0
Z = max(count_list)
position = count_list.index(Z)
if count_list.count(Z) > 1:
    print('?')
else:
    print(chr(position+65))

