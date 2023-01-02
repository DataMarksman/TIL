# SWEA. 3000. 중간값 구하기
# 설계 목적: 작은놈이랑 큰놈이랑 가운데 놈을 만들자,
# 1. 원래 있던 가운데 값과 받은 두놈을 비교한다.
# case 1. 있던 놈보다 새로온 두놈이 같거나 크다.
#       -> 새로온 두놈을 큰놈에 둘다 넣고 큰놈에서 작은 놈 빼서 가운데에 놓는다. 물론 원래 가운데 놈은 작은 쪽으로
# case 2. 있던 놈보다 새로온 두 놈이 같거나 작다.
#       -> 새로 온 두놈을 작은 놈에 넣고 작은 놈 중 가장 큰 놈을 가운데에 놓는다. 원 가운데는 큰놈으로.
# case 3. 그 외에는 위 아래로 보내면 된다.

# 개선점:
# 1. 아니 마지막 값에도 %20171109 해야된다구... 쉬부레


import heapq
T = int(input())
for case_num in range(1, T + 1):
    N, start = map(int, input().split())
    small_h = []
    big_h = []
    ans = 0    # 답 내기 위한 변수
    mid = int(start)    # 가운데 값
    for put_in in range(N):
        A, B = map(int, input().split())
        if mid <= A and mid <= B:
            heapq.heappush(big_h, A)
            heapq.heappush(big_h, B)
            heapq.heappush(small_h, (-mid, mid))
            mid = heapq.heappop(big_h)
        elif mid >= A and mid >= B:
            heapq.heappush(small_h, (-A, A))
            heapq.heappush(small_h, (-B, B))
            heapq.heappush(big_h, mid)
            mid = heapq.heappop(small_h)[1]
        else:
            if A > B:
                heapq.heappush(big_h, A)
                heapq.heappush(small_h, (-B, B))
            else:
                heapq.heappush(big_h, B)
                heapq.heappush(small_h, (-A, A))
        ans += mid%20171109
    print(f'#{case_num} {ans%20171109}')