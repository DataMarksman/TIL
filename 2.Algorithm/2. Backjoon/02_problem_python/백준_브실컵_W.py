# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
# sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip('\r\n')
J, N = map(int, input().split())
answer = 0
for case in range(N):
    grain = input()
    point = 0
    for check in grain:
        if check == " ":
            point += 1
        elif 65 <= ord(check) <= 90:
            point += 4
        else:
            point += 2
    if point <= J:
        answer += 1
print(answer)