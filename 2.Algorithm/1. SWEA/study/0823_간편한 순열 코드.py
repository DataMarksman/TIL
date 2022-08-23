# 08.23 길이 2짜리면 그냥 for 문 쓰는게 빠르다!
#
"""
arr = ['a', 'b', 'c']

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k:
                print(f'{arr[i]} {arr[j]} {arr[k]}')
"""
# 순열 N개 중에서 2개 뽑기
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j:
            print(f'{arr[i]} {arr[j]}')

# 조합 N개 중에서 2개 뽑기
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in range(len(arr)):
    for j in range(len(arr)):
        if i < j:
            print(f'{arr[i]} {arr[j]}')

# 스킬: 길이 k개 이하인 부분 집합의 요소 합이 10 이상인 것을 구하라.
arr = [1, 2, 3, 4, 6, 10, 11]
# 원본이라 가정할 때, k가 3이라면,
re_arr = [1, 2, 3, 4, 6, 10, 11, 0, 0]

for i in range(len(re_arr)):
    for j in range(len(re_arr)):
        for t in range(len(re_arr)):
            if i < j < t and (re_arr[i] + re_arr[j] + re_arr[t]) > 10:
                print(f'합계: {re_arr[i] + re_arr[j] + re_arr[t]} {re_arr[i]} {re_arr[j]} {re_arr[t]} ')







