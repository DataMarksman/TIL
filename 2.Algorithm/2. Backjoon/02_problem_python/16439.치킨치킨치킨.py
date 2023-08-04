# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
chicken_list = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(K - 2):
    for j in range(i + 1, K - 1):
        for k in range(j + 1, K):
            happiness = 0
            for checking in range(N):
                happiness += max(chicken_list[checking][i],
                                 chicken_list[checking][j],
                                 chicken_list[checking][k])
            if happiness > ans:
                ans = int(happiness)
print(ans)