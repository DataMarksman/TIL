# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
N = int(sys.stdin.readline().strip())
X_min = N-1
X_max = 0
Y_min = N-1
Y_max = 0
verti = 200000
hori = 200000
gom_count = 0
for gomgom in range(N):
    line = list(sys.stdin.readline().strip())
    for checking in range(N):
        if line[checking] == 'G':
            gom_count += 1
            if gomgom > X_max:
                X_max = gomgom
            if gomgom < X_min:
                X_min = gomgom
            if checking > Y_max:
                Y_max = checking
            if checking < Y_min:
                Y_min = checking
if gom_count == 1:
    print(0)
else:
    LeftUP = X_max + Y_max
    RightUP = X_max + (N-1) - Y_min
    LeftDown = (N-1) - X_min + Y_max
    RightDown = (N-1) - X_min + (N-1) - Y_min
    if X_min == X_max:
        verti = min((N-1) - Y_min, Y_max)
    if Y_min == Y_max:
        hori = min((N-1) - X_min, X_max)
    ans = min(LeftUP, LeftDown, RightDown, RightUP, verti, hori)
    print(ans)