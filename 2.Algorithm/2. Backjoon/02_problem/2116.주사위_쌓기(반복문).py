# BOJ. 2116 주사위 쌓기
# 설계 의도: 길찾기와 동일.
# 1. 길 지나가면서, 내가 지나지 않은 길들 중 큰 값 같이 빼오기.
# 개선점: 리커전 한계치 올려줘야 한다.
# import sys
# sys.setrecursionlimit(10**6)


def dice_up(n, k, stock):
    global sum_list
    if n >= N:
        sum_list += [sum(stock)]

    elif n == 0:
        stock = []
        for idx in range(6):
            start = dice_list[n][idx%3][idx%2]
            stock += [max(max(dice_list[n][(idx+1)%3]), max(dice_list[n][(idx+2)%3]))]
            dice_up(n+1, start, stock)
            stock = []

    else:
        for idx in range(6):
            if dice_list[n][idx%3][idx%2] == k:
                start = dice_list[n][idx%3][(idx+1)%2]
                stock += [max(max(dice_list[n][(idx+1)%3]), max(dice_list[n][(idx+2)%3]))]
                return dice_up(n + 1, start, stock)


N = int(input())
dice_list = [[] for _ in range(N)]
sum_list = []
# sum_list = [28, 27, 27, 25, 28, 25]
for put_in in range(N):
    num_list = list(map(int, input().split()))
    dice_list[put_in] += [[num_list[0], num_list[5]]]
    dice_list[put_in] += [[num_list[1], num_list[3]]]
    dice_list[put_in] += [[num_list[2], num_list[4]]]
# dice_list = [[[2, 4], [3, 6], [1, 5]], [[3, 5], [1, 4]...
dice_up(0, 0, [])
print(max(sum_list))

"""
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
"""