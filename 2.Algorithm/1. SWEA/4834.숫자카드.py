# 4834.숫자카드

T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    origin_num = int(input())                # 처리할 원본 숫자 뭉텅이를 받습니다.
    count_list = [0]*12                      # 0~9 까지의 숫자들을 카운팅할 공간 배정
    num_list = []                            # 원본에서 개별 숫자들을 뽑아낼 공간 배정 
    for i in range(N):                       # 10으로 나눠주면서 하나씩 빼주는 과정 반복
        num_list += [origin_num % 10]        # 10으로 나눈 나머지는 가장 뒤의 숫자 -> 추출
        origin_num = origin_num // 10        # 10으로 나눈 몫은 다음 숫자로 다시 배정
    for number in num_list:                  # 뽑아낸 숫자들을 위치좌표로 활용하여 
        count_list[number] += 1              # 카운팅 리스트에 +1씩 해줍니다.
    max_count = 0                            # 초기 MAX 값과 MAX 숫자를 0 0으로 배정.
    max_number = 0
    for count in range(len(count_list)):     # 0~9까지의 숫자들을 하나씩 탐색
        if count_list[count] >= max_count:   # 큰 수가 우선시 되므로 >= 를 사용합니다.
            max_count = count_list[count]    # 이렇게 등장 횟수와 해당 숫자를 추출하여
            max_number = count
    print(f'#{case_num} {max_number} {max_count}')  # 출력!
