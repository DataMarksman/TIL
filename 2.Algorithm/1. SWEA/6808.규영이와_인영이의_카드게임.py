# 6808. 규영이와 인영이의 카드게임

# 조건 정리
# 총점이 171점이기 때문에 비기는 경우도 없다.
# 그렇다면 한쪽이 이기기 위해서는 86점 이상 취득하는 것이 목표
# 점수가 86점 이상인 것들만 카운팅 하면 된다.
def permutation(remain):                                # 순열 처럼 보이는 함수를 제작합니다.
    global win_count                                    # 함수 속 글로벌 변수인 win_count 선언
    if len(remain) == 9:                                # 인풋된 리스트 길이가 9라면 검증 시작
        sum_stack = 0                                   # 검증용 합산 스택
        for i in range(9):                              # 앞에서부터 하나씩 빼오면서
            if remain[i] - enemy_cards[i] > 0:          # 내 카드와 상대카드 비교
                sum_stack += remain[i] + enemy_cards[i]
        if sum_stack >= 86:                             # 그 차이의 합계가 86 이상이면 승리
            win_count += 1                              # win_count +1 합니다
    else:
        for chcking in range(9):                        # 이쪽이 재귀 본체. 총 9! 회 시행
            if my_cards[chcking] not in remain:         # 앞에서부터 카드 리스트에 있는 카드가
                remain += [my_cards[chcking]]           # 함수에 넣은 리스트에 없으면
                permutation(remain)                     # 그거 넣은 리스트를 다시 함수에 넣기
                del remain[len(remain)-1]               # 다음 checking을 위해서 필요함


T = int(input())                                        # 
for case_num in range(1, T+1):                          #
    board = [0]*19                                      # 카운팅 소트 용 스톡
    enemy_cards = list(map(int, input().split()))
    my_cards = []                                       # 내 카드 저장용 스톡
    win_count = 0                                       # 답안 제출용 win_count 스톡  
    for enemy_card in enemy_cards:                      # 상대 카드를 카운트 소트 스톡에 저장
        board[enemy_card] = 1                           # 
    for mycard in range(len(board)):                    # 상대 카드 기반으로 내 카드 추출
        if board[mycard] == 0 and mycard != 0:          #
            my_cards += [mycard]                        #
    permutation([])                                     # [] 아무것도 없는 상태에서 재귀 시작
    print(f'#{case_num} {362880-win_count} {win_count}')# 출력
