# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())
words = {"Never gonna give you up",
         "Never gonna let you down",
         "Never gonna run around and desert you",
         "Never gonna make you cry",
         "Never gonna say goodbye",
         "Never gonna tell a lie and hurt you",
         "Never gonna stop"}
answer = "No"
for case in range(1, N+1):
    if input() not in words:
        answer = "Yes"
print(answer)