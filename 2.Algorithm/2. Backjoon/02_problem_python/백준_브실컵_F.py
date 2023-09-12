# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())
box_weight = 0
money_value = 0
for case in range(N):
    AB, W, H, L = input().split()
    if AB == "A":
        apple_cnt = (int(W)//12) * (int(H)//12) * (int(L)//12)
        box_weight += 1000 + apple_cnt*500
        money_value += apple_cnt * 4000
    else:
        box_weight += 6000
print(box_weight)
print(money_value)
