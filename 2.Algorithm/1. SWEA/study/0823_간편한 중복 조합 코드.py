# 08.23 for 문도 좋은거야~
# 우리는 이전 학습에서 조합을 for 문으로 구현했다.
# 자, 그럼 5C3 를 해봤으니, 3H5를 해볼까?

# 조합 N개 중에서 2개 뽑기
arr1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in range(len(arr1)):
    for j in range(i+1, len(arr1)):
        print(f'{arr1[i]} {arr1[j]}')

# 스킬: 길이 k(k=5)개 이하의 중복 조합의 부분 집합에서 합이 10 이상인 케이스를 구하라.
# 구하고자 하는 것은 3H5
original_arr = [1, 2, 3]
arr = [1, 2, 3, 0, 0, 0, 0]
h_count = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        for k in range(j, len(arr)):
            for t in range(k, len(arr)):
                for p in range(t, len(arr)):
                    if (arr[i]+arr[j]+arr[k]+arr[t]+arr[p]) >10:
                        h_count += 1
                        print(f'{arr[i]} {arr[j]} {arr[k]} {arr[t]} {arr[p]}')
print(h_count)




