# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

def rooting(point):
    global input_number
    global ans
    global root_num
    if point <= N:
        rooting(point*2)
        if point == 1:
            root_num = input_number
        if point == N//2:
            ans = input_number
        input_number += 1
        rooting(point*2 + 1)


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    input_number = 1
    root_num = 0
    ans = 0
    rooting(1)
    print(f'#{case_num} {root_num} {ans}')
