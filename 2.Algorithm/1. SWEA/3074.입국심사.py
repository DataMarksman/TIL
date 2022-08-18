# 3074 입국심사
# 수가 정말 커졌을 때, 효율적으로 탐색 가능한 방법을 찾아보자.

T = int(input())
for case_num in range(1, T+1):                                    #
    N, M = map(int, input().split())                              #
    box_list = []                                                 #
    for _ in range(N):                                            #
        box_list.append(int(input()))                             #
    count_step = 10000000000                                      # 10의 자리수까지가 범위이므로 11의 자리부터 시작한다.
    current_sec = 0                                               # 현재 진행중인 시간대를 저장해놓는 곳
    while count_step > 0:                                         # 한자리수의 step, 즉 1이 //10 당해서 0으로 바뀌면 종료
        chek_point = 0                                            # M에 도달했는지 여부를 판단하기 위한 스톡
        for boxes in box_list:                                    # 각 심사소에서 인원들이 몇명이나 처리했는지 저장
            chek_point += ((current_sec + count_step) // boxes)   # 시간당 입국처리 총합을 구하여
        if chek_point >= M:                                       # 처리한 인원수가 목표치를 넘었으면
            count_step = count_step//10                           # step 변수를 10으로 나누고 다시 돌리기
        else:                                                     #
            current_sec += count_step                             # 목표치보다 작을 경우, 현재 step 을 찾는 값에 저장
    print(f'#{case_num} {current_sec+1}')                         #
