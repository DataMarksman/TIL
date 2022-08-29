

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
A = [1,2,3,4,5,6,7,8,9]
line_up = A[:3]+[0]+A[3:]
print(line_up)