# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
ans = 0
count = 0
list_A = [0, 0] + [i for i in range(2, N+1)]
flag = True
for j in range(N+1):
    if list_A[j] != 0 and flag:
        m = int(j)
        while m <= N and flag:
            if list_A[m] != 0:
                list_A[m] = 0
                count += 1
            if count == K:
                ans = int(m)
                flag = False
                break
            m += j
print(ans)