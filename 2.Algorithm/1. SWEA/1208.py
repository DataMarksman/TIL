# 1208.Flatten
# 이건 누적합 문제
# 카운팅 리스트 작성하고 앞에서 뒤로 가면서 누적합을 채워주면 된다.
# 반대도 동시에 진행하면 좋겠지만, 따로 진행.
#
T = 1
for case_num in range(1, T+1):
    N = int(input())
    box_list = map(int, input().split())
    count_list_1 = [0] * 101
    count_list_2 = [0] * 101
    for box in box_list:
        count_list_1[box] += 1
        count_list_2[box] += 1

    print(count_list_2)
    # 조건은 3개.
    # 1. 앞에서 가는 moving
    # 2. 뒤에서 가는 moving
    # 3. 그 두 moving 이 만나는가의 여부

    moving_1 = 0
    count_1 = 0
    while moving_1 < N and count_1 != 101:
        moving_1 += count_list_1[count_1]
        count_list_1[count_1 + 1] += count_list_1[count_1]
        count_1 += 1
        print(moving_1)
    low_box = count_1

    moving_2 = 0
    count_2 = 100
    while moving_2 < N and count_2 != 0:
        moving_2 += count_list_2[count_2]
        count_list_2[count_2 - 1] += count_list_2[count_2]
        count_2 -= 1
        print(moving_2)
    high_box = count_2

    if low_box >= high_box:
        ans = 1
    else:
        ans = high_box - low_box
    print(f'#{case_num} {ans}')


