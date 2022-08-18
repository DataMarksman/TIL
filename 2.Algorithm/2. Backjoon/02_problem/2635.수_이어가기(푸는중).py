# BOJ. 2635. 수 이어가기
# 설계 의도: 조건에 맞는 실행
# 개선점: 피보 함수가 작동 안함
memo = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]


def func(n):
    if n > 2 and len(memo) <= n:                   # 메모 길이가 n보다 작으면?
        memo.append(func(n-1) + func(n-2))  # 점화식 적용
    return memo[n]


N = int(input())
count = 4
stock = []
for put_in in range(N//2, N):
    stock += [put_in]
while True:
    switch_stock = []
    if count % 2 == 0:
        for check in stock:
            if check <= memo[count-1] / memo[count]:
                switch_stock += [check]
    else:
        for check in stock:
            if check >= memo[count-1] / memo[count]:
                switch_stock += [check]
    if len(switch_stock) >= 1:
        stock = switch_stock[::]
        count += 1
    else:
        break
ans_list = [N, stock[0]]
print(ans_list)
