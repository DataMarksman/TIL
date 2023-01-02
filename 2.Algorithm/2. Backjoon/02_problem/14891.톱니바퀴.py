# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)
def spinning(k, direction, LR):
    global gear_list

    if k + 1 < 4 and 'R' in LR:
        if gear_list[k][2] != gear_list[k+1][6]:
            spinning(k+1, direction * (-1), "R")
    if k - 1 >= 0 and 'L' in LR:
        if gear_list[k][6] != gear_list[k-1][2]:
            spinning(k-1, direction * (-1), "L")

    if direction > 0:
        gear_list[k] = [gear_list[k][7]] + gear_list[k][:7]
    elif direction < 0:
        gear_list[k] = gear_list[k][1:] + [gear_list[k][0]]


gear_list = [list(input()) for _ in range(4)]
N = int(input())
for spin_trial in range(N):
    A, B = map(int, input().split())
    spinning(A-1, B, "LR")
ans = 0
for checking in range(4):
    if gear_list[checking][0] == '1':
        ans += 2**checking
print(ans)