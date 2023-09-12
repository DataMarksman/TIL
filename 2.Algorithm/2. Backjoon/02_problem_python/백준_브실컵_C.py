# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
year, month, date = map(int, input().split("-"))
delay = int(input())

date += delay
if date > 30:
    if date % 30 != 0:
        month += date//30
        date = date % 30
    else:
        month += (date-30) // 30
        date = 30

    if month > 12:
        if month % 12 != 0:
            year += month // 12
            month = month % 12
        else:
            year += (month - 12) // 12
            month = 12
if len(str(month)) == 1:
    month = "0" + str(month)
if len(str(date)) == 1:
    date = "0" + str(date)
print(f"{year}-{month}-{date}")