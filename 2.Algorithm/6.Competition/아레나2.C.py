# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
from heapq import *
sys.setrecursionlimit(10**6)
N = int(input())
lt = list(map(int, input().split()))
Big = max(lt)
answer = sys.maxsize


def recursion(max_number):
    global answer
    if number_heapq:
        Small_number = heappop(number_heapq)
        if max_number - Small_number < answer:
            answer = max_number - Small_number
        max_number = max(2*Small_number, large)
        recursion(max_number)
    else:
        return

large = 0
small = sys.maxsize
number_heapq = []
for numbers in lt:
    while True:
        if Big//2 <= numbers <= Big + Big//2:
            break
        else:
            numbers *= 2
    if numbers > large:
        large = numbers
    if numbers <= Big:
        heappush(number_heapq, numbers)
recursion(large)
print(answer)
