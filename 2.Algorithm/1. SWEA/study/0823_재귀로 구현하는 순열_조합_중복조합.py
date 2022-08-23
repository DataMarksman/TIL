# 08.23 자, 이제 재귀로 다시 해보자구요

# 순열 nPm
def permutation(depth):
    if depth == m:
        print(sel)




# 조합 nCm
def combination(depth):
    if depth == m:
        print(sel)



# 중복 조합 nHm
def combi_rep(depth):
    if depth == m:
        print(sel)







n, m = map(int, input().split())
arr = list(range(1, n+1))
sel = [0]*m

permutation()
combination()
nombi_rep()

# 조합 N개 중에서 2개 뽑기
arr1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in range(len(arr1)):
    for j in range(i+1, len(arr1)):
        print(f'{arr1[i]} {arr1[j]}')

# 스킬: 길이 k(k=5)개 이하의 중복 조합의 부분 집합에서 합이 10 이상인 케이스를 구하라.
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




