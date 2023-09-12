# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

zip, dok = map(int, input().split())
move, sleep = map(int, input().split())
zip_time = zip + (zip//8)*sleep if zip % 8 != 0 or zip == 0 else zip + ((zip-1)//8)*sleep
dok_time = move + dok + (dok//8)*(sleep+move*2) if dok % 8 != 0 or dok == 0 else move + dok + ((dok-1)//8)*(sleep+move*2)
if zip_time < dok_time:
    print("Zip")
    print(zip_time)
else:
    print("Dok")
    print(dok_time)