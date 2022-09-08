# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

#N = int(input())

def cutting(numb ,odd_count):
    global ans
    K = len(numb)
    if numb == 1:
        if int(numb) % 2 == 1:
            odd_count += 1
        ans += odd_count
    elif K >= 3:
        for i in range(1, K-2):
            for j in range(i+1, K-1):
                
    elif K == 2:
        pass

string = input()
ans = 0
for check in range(1, len(string)-1):
    if string[check] == ' ' and string[check-1] != ' ' and string[check+1] != ' ':
        ans += 1
if ans == 0:
    if len(string.replace(' ', '')) == 0:
        ans = -1
print(ans+1)