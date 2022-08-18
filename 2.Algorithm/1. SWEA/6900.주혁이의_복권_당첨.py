# 6900. 주혁이의 복권 당첨
# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
for case_num in range(1,T+1):
    N, M = map(int,input().split())
    match_list = []                                                        # 당첨 종목 기입할 리스트야!
    check_list = []                                                        # 내가 기입한 용지 넣을 리스트야!
    prize_sum = 0                                                          # 당첨금 총합계야!
    for dict_input in range(N):                                            # 당첨 종목 N개를 불러오는거야!
        lotto, prize = input().split()
        match_list += [{'code': list(str(lotto)),'prize': int(prize)}]
    for check_input in range(M):                                           # 내가 산 복권 용지 M개를 불러오는거야!
        check_list += [list(str(input()))]
    
    for lotto_check in range(M):                                           # M개의 용지를 하나씩 뽑아서 대조할거야
        for prize_check in range(N):                                       # N개의 종목이랑 말이지!
            prize_count = 0                                                # 각 종목별 8개 카운트 다 올라가야 당첨이야! *는 무조건 +1 해줘!
            for idx in range(8):                                           # M번째 용지를 N번째 종목과 비교하는데 8개 숫자야.
                if match_list[prize_check]['code'][idx] == str('*'):       # 만약 당첨 조건에 숫자 대신 * 기입되어있으면 카운트 +1
                    prize_count += 1
                elif match_list[prize_check]['code'][idx] ==  check_list[lotto_check][idx]:
                    prize_count += 1                                       # 만약 당첨 조건이 맞아도 당연히 카운트 +1
            if prize_count == 8:
                prize_sum += match_list[prize_check]['prize']              # 카운팅이 8개 일때만, 상금을 상금 합계에 추가해야해!
    print(f'#{case_num} {prize_sum}')
