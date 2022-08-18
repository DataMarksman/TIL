# 4869. 종이 붙이기
def paper(n):                                      # 메모이제이션 함수
    if n > 2 and len(memo) <= n:                   # 메모 길이가 n보다 작으면?
        memo.append(paper(n-1) + 2*(paper(n-2)))   # 점화식 적용
    return memo[n]


memo = [0, 1, 3, 5]                                # 메모 입력시, 계속 씁니당!
for case_num in range(1, int(input())+1):          # 받는 값, /10 하면 idx!
    print(f'#{case_num} {paper(int(int(input())/10))}')  # 출력!


# 점화식:
# memo[n] = memo[n-1] + 2*(memo[n-2])
# 지금 꺼 = 이전꺼 + (그전꺼 x2)
