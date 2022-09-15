# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

def rooting(point):
    global ans
    if point:
        ans += 1
        rooting(left[point])
        rooting(right[point])


T = int(input())
for case_num in range(1, T + 1):
    E, start = tuple(map(int, input().split()))
    lines = list(map(int, input().split()))
    left = [0]*(E+2)
    right = [0]*(E+2)
    ans = 0
    for checking in range(E):
        x = lines[checking*2]
        y = lines[checking*2 + 1]
        if left[x]:
            right[x] = y
        else:
            left[x] = y
    rooting(start)
    print(f'#{case_num} {ans}')