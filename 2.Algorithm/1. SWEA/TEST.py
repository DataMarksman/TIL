# 이것은 간략하게 코드 돌려보기 위한 용도의 TEST.py 입니다.

# aa = {'0': 'AA','1': 'BB','2': 'CC'}

# print(aa.get('AA'))

def combination(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result


list_A = [0, 1, 2, 3]
for j in range(len(list_A)):
    print(combination(list_A, j))
