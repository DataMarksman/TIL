# SWEA. 1952 수영장
# 설계 목적: DP
# 1. 처음에 1~12월의 값을 받고 각 달의 값 * 일일 이용권 가격과 월간 이용권 가격을 비교.
# 2. 더 싼곳으로 리스트를 채워놓은 다음 본격적으로 DP 필드를 작성한다.
# 3.

T = int(input())
for case_num in range(1, T + 1):
    D, M, TM, Y = map(int, input().split())
    month_list = list(map(int, input().split()))
    for summing in range(12):
        cost_list =

    print(f'#{case_num} {ans}')
