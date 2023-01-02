# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
ans = 0
for i in range(N-2):
    if ans == M:
        break
    for j in range(i+1, N-1):
        if ans == M:
            break
        for k in range(j+1, N):
            if ans == M:
                break
            if ans <= num_list[i] + num_list[j] + num_list[k] <= M:
                ans = num_list[i] + num_list[j] + num_list[k]
print(ans)

