# 1244. 스위치 켜고 끄기
# 설계 의도: 조건에 맞는 실행
# 개선점: 20줄씩 프린트 하는 방법을 좀 더 세련되게 할 수 없을까?

N = int(input())
switch_list = list(map(int, input().split()))
p_count = int(input())
p_list = [list(map(int, input().split())) for _ in range(p_count)]
for playing in range(p_count):
    for switch in range(len(switch_list)):
        if p_list[playing][0] == 1 and (switch+1) % p_list[playing][1] == 0:
            switch_list[switch] = (switch_list[switch] + 1) % 2
        elif p_list[playing][0] == 2 and p_list[playing][1] == (switch+1):
            switch_list[switch] = (switch_list[switch] + 1) % 2
            tmp_range = 1
            while switch - tmp_range >= 0 and len(switch_list) > (switch + tmp_range):
                if switch_list[switch-tmp_range] == switch_list[switch+tmp_range]:
                    switch_list[switch - tmp_range] = (switch_list[switch - tmp_range] + 1) % 2
                    switch_list[switch + tmp_range] = (switch_list[switch + tmp_range] + 1) % 2
                else:
                    break
                tmp_range += 1
for print_idx in range(len(switch_list)):
    if print_idx % 20 == 0 and print_idx//20 < len(switch_list)//20:
        print(*switch_list[print_idx:print_idx+20])
    elif print_idx % 20 == 0:
        print(*switch_list[print_idx:len(switch_list)])
