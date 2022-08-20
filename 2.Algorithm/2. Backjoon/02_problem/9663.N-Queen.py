# 9663. N-Queen
# 체스판을 봤을 때,
#    0     1     2     3     4     5     6
# 0(0,0)                  *(0,4)  -> 역대각선: 위치 좌표 (x,y)의 합 [x+y]가 일치하는 좌표를 의미.
# 1      (1,1)      *(1,3)
# 2           *(2,2)
# 3     *(1,3)-      (3,3)        -> 대각선: 위치 좌표 (x,y)의 차이, 즉 [x-y]가 일치하는 좌표를 의미.
# 4            (2,4)-
# 5                  (5,3)-       -> 대각선: 단, 위치 좌표중 y가 더 큰 경우,
# 6                                         x-y가 음수값이 나오므로, N+(x-y)로 양수화

N = int(input())
count = 0                                                     #
stock = []
check = set()
cross_check = set()
r_cross_check = set()
start = 0
n = 0

while True:
    if n >= N:                                                    # 반환할 조건은, n이 N에 도달했을 때
        count += 1                                                # 여기까지 도달하면 카운트 +1

    else:
        for i in range(start, N):
            if (i not in check) and (n+i not in cross_check) and (N+(n-i) not in r_cross_check):
                check.add(i)
                cross_check.add(n+i)
                r_cross_check.add(N+(n-i))
                stock.append(i+1)
                n += 1
                start = 0
                break
        else:
            stack = stock.pop()
            check.remove(stack-1)
            cross_check.remove(stack + n - 2)
            r_cross_check.remove(N+(n-stack))
            n -= 1
            while stack + 1 > N:
                stack = stock.pop()
                check.remove(stack - 1)
                cross_check.remove(stack + n - 2)
                r_cross_check.remove(N + (n - stack))
                n -= 1
            start = stack
print(count)
