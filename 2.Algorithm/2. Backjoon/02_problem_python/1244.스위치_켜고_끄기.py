# 1244. 스위치 켜고 끄기
# 설계 의도: 조건에 맞는 실행
# 개선점: 20줄씩 프린트 하는 방법을 좀 더 세련되게 할 수 없을까?

N = int(input())
switch_list = list(map(int, input().split()))                                                    #
p_count = int(input())                                                                           #
p_list = [list(map(int, input().split())) for _ in range(p_count)]                               #
for playing in range(p_count):                                                                   # 각 사람 수 만큼 시행
    for switch in range(len(switch_list)):                                                       # 스위치 순회하면서 시행

        if p_list[playing][0] == 1 and (switch+1) % p_list[playing][1] == 0:                     # 남자고, 조건 부합하면
            switch_list[switch] = (switch_list[switch] + 1) % 2                                  # 0은 1로, 1은 0으로 바꿈

        elif p_list[playing][0] == 2 and p_list[playing][1] == (switch+1):                       # 여자고, 조건 부합하면
            switch_list[switch] = (switch_list[switch] + 1) % 2                                  # 지금 자리 0->1, 1->0

            tmp_range = 1                                                                        # 일단 1칸 옆부터 탐색
            while switch - tmp_range >= 0 and len(switch_list) > (switch + tmp_range):           # 범위 안쪽인지 확인하고
                if switch_list[switch-tmp_range] == switch_list[switch+tmp_range]:               # 양쪽이 똑같으면
                    switch_list[switch - tmp_range] = (switch_list[switch - tmp_range] + 1) % 2  # 앞의 것 0->1, 1->0
                    switch_list[switch + tmp_range] = (switch_list[switch + tmp_range] + 1) % 2  # 뒤의 것 0->1, 1->0
                else:                                                                            #
                    break                                                                        #
                tmp_range += 1                                                                   # 다음 것도 확인하기

for print_idx in range(len(switch_list)):                                                        # 프린트를 해야하는데..
    if print_idx % 20 == 0 and print_idx//20 < len(switch_list)//20:                             # 20줄 넘게 남았으면
        print(*switch_list[print_idx:print_idx+20])                                              # 20줄 프린트 하기
    elif print_idx % 20 == 0:                                                                    # 20줄 아래로 남았으면
        print(*switch_list[print_idx:len(switch_list)])                                          # 나머지 전부 프린트 하기
