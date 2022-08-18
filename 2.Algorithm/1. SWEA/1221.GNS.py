# 1221. GNS

T = int(input())
for tc in range(1, T+1):
    word_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN" ]
    case_num, N = map(str, input().split())             #
    input_list = list(map(str, input().split()))        #
    count_list = [0]*10                                 # 카운트할 스톡 제작
    answer_list = []                                    # 답안 저장용 스톡 제작
    for words in range(len(input_list)):                # 각 글자에 해당하는
        for check in range(len(word_list)):             # 카운팅 스톡에
            if input_list[words] == word_list[check]:   # 글자 일치여부 확인해서
                count_list[check] += 1                  # +1씩 저장해주기
    for writing in range(len(count_list)):              # 카운트에 저장해둔 값 만큼
        answer_list +=\
            [word_list[writing]] * count_list[writing]  # 해당 글자 복사해서 붙여넣기
    print(case_num)                                     # 한줄 띄어야 해서 따로 print
    print(*answer_list)                                 # *로 언패킹해서 print
