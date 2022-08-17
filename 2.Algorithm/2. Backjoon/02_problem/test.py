# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
def game(x):
    if x <= 0:
        return 'D'
    if count_A[x] == count_B[x]:
        return game(x-1)
    return 'A' if count_A[x] > count_B[x] else 'B'


N = int(input())
for case_num in range(1, N+1):
    count_A = [0]*5
    count_B = [0]*5
    list_A = list(map(int, input().split()))
    for i in range(1, list_A[0]+1):
        count_A[list_A[i]] += 1
    list_B = list(map(int, input().split()))
    for j in range(1, list_B[0]+1):
        count_B[list_B[j]] += 1
    print(game(4))




