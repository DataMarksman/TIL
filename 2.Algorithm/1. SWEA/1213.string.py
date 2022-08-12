# 1213. string

T = 10
for tc in range(1, T+1):                                   #
    case_num = int(input())                                #
    target_word = list(str(input()))                       #
    check_list = list(str(input().split()))                #
    ans_count = 0                                          # 최종 값 스톡
    for start in range(len(check_list)-len(target_word)):  # 전체 텍스트 길이 - 비교 텍스트 길이
        check_count = 0                                    # 비교해서 몇개나 맞는지 산출
        for checking in range(len(target_word)):           # 비교 텍스트 길이만큼 탐색
            if check_list[start+checking]\
                    == target_word[checking]:              # 현재 위치에서 비교 텍스트 길이만큼 맞으면
                check_count += 1                           # 체크 스택 +1
        if check_count == len(target_word):                # 체크 스택이 비교 텍스트 길이와 일치하면
            ans_count += 1                                 # 최종 값 +1
    print(f'#{case_num} {ans_count}')                      #





