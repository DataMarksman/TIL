# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
N = int(input())
idx_list = []
for put_in in range(N):
    idx_list.append(tuple(map(int, input().split())))
ans = 0
for pick_1 in range(N-2):
    for pick_2 in range(pick_1+1, N-1):
        for pick_3 in range(pick_2+1, N):
            X1, Y1 = idx_list[pick_1]
            X2, Y2 = idx_list[pick_2]
            X3, Y3 = idx_list[pick_3]
            D1 = ((X2-X1)**2 + (Y2-Y1)**2)
            D2 = ((X3-X2)**2 + (Y3-Y2)**2)
            D3 = ((X3-X1)**2 + (Y3-Y1)**2)
            if D2 + D1 == D3 or D3 + D1 == D2 or D2 + D3 == D1:
                ans += 1
print(ans)