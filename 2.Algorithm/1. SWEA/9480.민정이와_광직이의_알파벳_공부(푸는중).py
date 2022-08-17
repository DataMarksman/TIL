# 9480. 민정이와 광직이의 알파벳 공부
# SWEA에 광직이 파이썬이 업데이트 된 것을 기념으로 재풀이 들어갑니다~
# 설계 의도:
# 1. 아스키 코드로 변환 후 -97을 하여 알파벳 소문자 카운팅 소트한다.
# 2. 카운팅 소트의 모든 원소가 1이상인 조합의 개수를 구하여 도출한다.
# 개선점
# 1.
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


T = int(input())

for i in range(T):









