# BOJ.21275.폰 호석만
# 설계 의도: 조건에 맞는 실행
# 개선점:
# 1. 사실 try, except 쓴 시점에서 맞은게 아니다.
A, B = tuple(map(str, input().split()))
count = 0
ans = []
flag = True

for i in range(2, 37):
    if flag:
        for j in range(2, 37):
            if i != j:
                try:
                    if int(str(A), i) == int(str(B), j) and 0 <= int(str(A), i) < 2**63:
                        count += 1
                        if count == 1:
                            ans = [int(A, i), int(i), int(j)]
                        elif count >= 2:
                            flag = False
                            break
                except:
                    pass

if count == 1:
    print(*ans)
elif count >= 2:
    print("Multiple")
else:
    print("Impossible")
