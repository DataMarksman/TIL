# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")

def price(depth, visited, money):
    global min_price
    visited = set(visited)
    if depth == N:
        if money < min_price:
            min_price = int(money)
    for checking in range(N):
        if checking not in visited and money + num_list[depth][checking] < min_price:
            price(depth+1, visited | {checking, }, money + num_list[depth][checking])


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    min_price = 99999999999999999
    price(0, set(), 0)
    print(f'#{case_num} {min_price}')