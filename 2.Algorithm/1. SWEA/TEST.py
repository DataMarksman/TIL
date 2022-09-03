# 이것은 간략하게 코드 돌려보기 위한 용도의 TEST.py 입니다.

# aa = {'0': 'AA','1': 'BB','2': 'CC'}

# print(aa.get('AA'))
"""
def combination(arr, n):
    result = []
    if n == 0:
        return [result]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result


list_A = [0, 1, 2, 3]
for j in range(len(list_A)):
    print(combination(list_A, j))
"""

"""
def test(x):
    list_A = []
    count = 0
    if x < 10:
        count += 1
        list_A += [x]
        test(x+1)
    else:
        return [list_A]


print(test(1))
"""

"""
in_case = ['(', '[', '{', '<', ' ']
out_case = []
if '{' in in_case:
    print('hi')
out_case += [in_case.pop()]
print(out_case)
"""
"""
list_A = [0,1,2,3,4,5,60,7,8,9,10]
target = max(list_A)
position = list_A.index(target)
for selling in range(position+1):
    list_A.pop(position-selling)
print(list_A[position::-1])
"""
"""
list_A = [[1,2,3,4,5],[1,2,3,4,5,6,7]]
print(list_A[0:2][2])
"""
# M = 5
# batch_position = [i for i in range(M)]
# print(batch_position)
#
# K = 5
# if 1 in range(K-4, K+4):
#     print(range(K-4, K+4))
#     print('hi')
num_list = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
A = 7
ans = int(str(A)*num_list[A])
print(ans)