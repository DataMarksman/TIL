# Boj 2309 일곱난쟁이

midget_list = []                                      # 난쟁이 리스트 받기 용
for case_num in range(9):                             # 9마리 다 받아야죠
    midget_list.append(int(input()))                  # 바로 넣어줍시다.
aim_tall = sum(midget_list) - 100                     # 스파이 두놈 키 합이 넘치는 값과 동일
first_one = 0                                         # while 조건 겸 첫번째 놈 위치 변수
while first_one < 9:                                  # 9번 돌려야지~
    for second_one in range(9):                       # 두번째놈도 찾아봅시다.
        st_midget = int(midget_list[first_one])       # 그냥 첫번째 vs 두번째 비교해도 되는데
        nd_midget = int(midget_list[second_one])      # 뭔가 가독성을 위해....
        if (st_midget != nd_midget) and \
                (st_midget + nd_midget) == aim_tall:  # 이건 위치 데이터로 바로 비교해도 됩니다!
            midget_list.remove(st_midget)             # 아무튼 중복 값은 없으니 첫번째 놈 날리고
            midget_list.remove(nd_midget)             # 두번째 놈 날리고
            ans_list = sorted(midget_list)            # 리스트 재정렬
            for real_midget in ans_list:              # 진또배기를 작은 순서대로
                print(real_midget)                    # 출력해줍니다.
            first_one += 100                          # while 정지용
            break                                     # for 문 정지용
    first_one += 1                                    # while 돌리러 갑시다~
