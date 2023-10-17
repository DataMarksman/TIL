# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())
num = list(map(int, input().split()))
arr = [0]*40001
answer = 0
for i in range(1, N):
    answer += arr[20000-num[i]]
    for j in range(i):
        arr[20000+num[i]+num[j]] += 1
print(answer)


"""
10
2 -5 2 3 -4 7 -4 0 1 -6
"""