# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
sys.setrecursionlimit(10**6)

def erase(idx):
    if idx < 10001:
        idx = int(idx)
        numbers = list(str(idx))
        for number in numbers:
            idx += int(number)
        All_number.discard(idx)
        erase(idx)
    else:
        return


All_number = set(range(1, 10001))
for i in range(1, 10001):
    if i in All_number:
        print(i)
        erase(i)
