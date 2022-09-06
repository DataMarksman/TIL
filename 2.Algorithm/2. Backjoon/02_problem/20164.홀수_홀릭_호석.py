# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

#N = int(input())


string = input()
ans = 0
for check in range(1, len(string)-1):
    if string[check] == ' ' and string[check-1] != ' ' and string[check+1] != ' ':
        ans += 1
if ans == 0:
    if len(string.replace(' ', '')) == 0:
        ans = -1
print(ans+1)