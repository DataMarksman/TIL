# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
A = input()
B = input()
C = input()
answer = ""
if A.isnumeric():
    answer = int(A) + 3
elif B.isnumeric():
    answer = int(B) + 2
elif C.isnumeric():
    answer = int(C) + 1
if answer % 5 == 0 and answer % 3 == 0:
    answer = "FizzBuzz"
elif answer % 5 == 0:
    answer = "Buzz"
elif answer % 3 == 0:
    answer = "Fizz"
print(answer)

