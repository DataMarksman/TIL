# 1208.Flatten
# 이건 누적합 문제
# 카운팅 리스트 작성하고 앞에서 뒤로 가면서 누적합을 채워주면 된다.
# 반대도 동시에 진행하면 좋겠지만, 따로 진행.
#
T = 10
for case_num in range(1, T+1):
    N = int(input())
    box_list = list(map(int, input().split()))
    dump_up_list = [0] * 101
    dump_down_list = [0] * 101
    for box in box_list:
        dump_up_list[box] += 1
        dump_down_list[box] += 1
    # 생각해야할 부분은 3개.
    # 1. 밑에서 위로 가는 dump
    # 2. 위에서 아래로 내려오는 dump
    # 3. 그 두 dump가 만나는가의 여부

    dump_up = 0                                             # dump_up -> 아래층 부터 누적합을 쌓아가는 덤프 시행횟수
    up_count = 0                                            # UP_count -> 몇번 밟았나 = 현재 공사 진행중인 층 수
    
    while dump_up < N and up_count != 101:                  # <반복> 아래층부터 한층씩 누적합을 쌓아가며 올라가기
        dump_up += dump_up_list[up_count]                   # 해당 층의 모든 박스 개수 만큼 덤프 횟수에 추가하고
        dump_up_list[up_count + 1] += dump_up_list[up_count]# 다음 층에 그 박스 개수만큼 더해줌
        up_count += 1                                       # 한 층 올라감
    low_box = up_count-1                                    # dump_up이 N을 넘어갈 경우 멈추기 때문에,
                                                            # -> 실제로 공사 중인 층은 현재 층보다 한칸 아래임.
    dump_down = 0
    down_count = 100
    while dump_down < N and down_count != 0:                # dump_down -> 최상층 부터 누적합을 쌓아가는 덤프 시행횟수
        dump_down += dump_down_list[down_count]             # down_count -> 몇번 밟았나 = 현재 공사 진행중인 층 수
        dump_down_list[down_count - 1] += dump_down_list[down_count]
        down_count -= 1                                     # 한 층 내려감
    high_box = down_count+1                                 # dump_down이 N을 넘어갈 경우 멈추기 때문에,
                                                            # -> 실제로 공사 중인 층은 현재 층보다 한칸 위임.
    if low_box >= high_box:                                 # 덤프를 너무 많이 해서 서로 중간에 지나쳐가게 되면, 
        ans = 1                                             # 최하층이 최상층보다 같거나 높게 나오므로 1을 반환
    else:
        ans = high_box - low_box
    print(f'#{case_num} {ans}')
