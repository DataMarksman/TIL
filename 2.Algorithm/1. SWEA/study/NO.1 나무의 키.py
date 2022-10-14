
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    full_stack = 0
    switching = 0
    one_left = 0
    two_left = 0
    ans = 0
    tree_list = sorted(list(map(int, input().split())))
    goal = max(tree_list)
    for checking in range(N):
        if tree_list[checking] < goal:
            aim = goal - tree_list[checking]
            full_stack += aim//3

            if aim % 3 == 1:
                one_left += 1
            elif aim % 3 == 2:
                two_left += 1
    ans += full_stack*2
    if one_left == two_left:
        ans += one_left*2

    # 1 남으면 어쩔 수 없지. 그냥 하루 건너 물 줘야함.
    elif one_left > two_left:
        ans += two_left * 2
        one_left = one_left - two_left
        ans += (one_left-1)*2 + 1

    # 2 남으면 찢고 비집고 해서 어떻게든 줄여볼 수 있지.
    else:
        ans += one_left * 2
        ans += (((two_left - one_left)*2)//3 * 2) + (((two_left - one_left)*2) % 3)
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
# 이거 틀림
#10 21

"""