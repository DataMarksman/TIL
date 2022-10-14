
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    two_stack = 0
    one_stack = 0
    ans = 0
    tree_list = sorted(list(map(int, input().split())))
    goal = max(tree_list)
    for checking in range(N):
        if tree_list[checking] < goal:
            aim = goal - tree_list[checking]
            two_stack += aim//2
            one_stack += aim%2

    # 1 남으면 어쩔 수 없지. 죄다 분류해서 엣지 커버 해주자.
    if one_stack > two_stack:
        ans += two_stack * 2
        one_stack -= two_stack
        ans += (one_stack - 1)*2 + 1

    # 2 남으면 찢고 비집고 해서 어떻게든 줄여볼 수 있지.
    else:
        ans += one_stack * 2
        ans += (((two_stack - one_stack)*2)//3 * 2) + (((two_stack - one_stack)*2) % 3)
    print(f'#{tc} {ans}')




"""

5
2
5 5
2
4 2
2
3 4
4
2 3 10 5
4
1 2 3 4


10
10
9 9 9 9 9 9 9 9 9 10
10
8 9 9 9 9 9 9 9 9 10
10
7 9 9 9 9 9 9 9 9 10
10
7 7 7 7 7 7 9 9 9 10
10
8 8 8 8 8 8 8 8 8 10
2
1 1
3
1 1 100
100
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 3
10
1 2 1 2 1 2 1 2 1 3
10
1 9 9 9 9 9 9 9 9 10


#1 17
#2 15
#3 17
#4 17
#5 12
#6 0
#7 132
#8 132
#9 10
#10 17
"""