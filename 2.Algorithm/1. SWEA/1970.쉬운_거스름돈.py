# 1970. 쉬운 거스름돈

T = int(input())
for case_num in range(1, T+1):                                    #
    money = int(input())
    change_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change_count = [0]*8

    for changing in range(8):
        n = 0
        while money >= 0:
            n += 1
            money -= change_list[changing]
        money += change_list[changing]
        change_count[changing] = n - 1

    print(f'#{case_num}')
    print(*change_count)
