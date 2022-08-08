# 기본 설계: 앞에서 부터 같은 숫자 3개 있나? 확인 이후 다시 앞에서부터 연속 숫자 3개 있나? 확인
# 만약! 둘중 하나만 있다면, 혹시라도 먼저 갈무리 한 것 때문에 나머지 하나가 안될 수도 있으니
# answer_list에서 빼놓은 값이 한개라면, 이번에는 순서를 바꿔서 해본다.

# 인풋: 테스트 케이스 T, 6자리 숫자
T = int(input())
for case_num in range(T):
    num_list = list(map(str,input()))

		# 0~9의 각 숫자 카운트를 저장해놓을 [0] 10개와 [i+2] 까지 계산하기 위한 공백 2자리 추가
    count_list = [0]*12
    for num in num_list:
        count_list[int(num)] += 1

		# 베이비 진 조건이 들어갈 자리. len(answerlist)는 베이비 진의 조건이 달성된 개수를 뜻함
    answer_list = []

		# 같은 숫자 3개가 등장하는 조건부터 찾고
    for i in range(0,10):
        if count_list[i] >= 3:
            count_list[i] -= 3
            answer_list += [[[i]*3]]
		# 이후에 연속된 숫자가 3개 등장하는 조건으로 찾는다.
    for j in range(0,10):       
        if count_list[j]*count_list[j+1]*count_list[j+2] == True:
            count_list[j] -= 1
            count_list[j+1] -= 1
            count_list[j+2] -= 1
            answer_list += [[[j],[j+1],[j+2]]]

		# 만약 답안이 1개라면, 한쪽을 받는 것 때문에 둘다 받을 수 있었는데도 못받는 경우를 고려하여
    if len(answer_list) ==1 :
        count_list = [0]*12
        answer_list = []
				# 이번에는 연속된 숫자부터 고려한 다음 같은 숫자 3번을 검색한다.
        for k in range(0,10):
            if count_list[k]*count_list[k+1]*count_list[k+2] == True:
                count_list[k] -= 1
                count_list[k+1] -= 1
                count_list[k+2] -= 1
                answer_list += [[[k],[k+1],[k+2]]]
        for t in range(0,10):
            if count_list[t] >= 3:
                count_list[t] -= 3
                answer_list += [[[t]*3]]

		# 조건이 2개 달성 되었다면, Baby Gin을 출력한다.
		# 리스트 값을 도출하는 것은 내가 확인하기 위함으로, 원래 필요하지는 않다.
    if len(answer_list) == 2:
        print(f'Baby Gin: {answer_list}')
    else:
        print("Lose")
