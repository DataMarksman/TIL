# 기본 설계: 주어진 6개 숫자로 베이비 진 정답 조건으로 쓸 수 있는 조합을 전부 구해서 짜맞추기 하기.
# 설계 이유
# 1. 만약 111111 혹은 123123처럼 같은 조건으로 두번 빼야되는 경우는 어떻게 케어하는가?
# 2. 123234 처럼 우선순위 문제는 어떻게 해결하는가?
# 이 두 문제점을 한번에 해결하기 위한 방법.

# 인풋: 테스트 케이스 T, 6자리 숫자
T = int(input())
for case_num in range(T):
    num_list = list(map(str,input()))

		# 0~9의 각 숫자 카운트를 저장해놓을 [0] 10개와 [i+2] 까지 계산하기 위한 공백 2자리 추가
    count_list = [0]*12
    for num in num_list:
        count_list[int(num)] += int(1)
		# 베이비 진을 위한 조건을 달성한 조합들이 들어갈 자리
    answer_list = []

		# 같은 숫자 3개가 등장하는 조건부터 찾고
    for i in list(range(0,10)):
        if count_list[i] >= 3:
            answer_list += [[i,i,i]]
		# 이후에 연속된 숫자가 3개 등장하는 조건으로 찾는다.
    for j in list(range(0,10)):       
        if count_list[j]*count_list[j+1]*count_list[j+2] > 0 :
            answer_list += [[j,j+1,j+2]]
    
    # 먼저 출력 조건을 꺼놓는다.
    answer = False
    
    # tmp 리스트를 만들어서 앞서 뽑아놓은 조합들을 하나씩 조합해본다.
    # 이 경우 6자리 이므로, 2가지 조합만 조합하면 되므로 편하다.
    for x in answer_list:
      for y in answer_list:
        tmp_list = []
        compare_count_list = [0]*12
        tmp_list = x + y
        # 이렇게 뽑힌 tmp_list를 sort로 정렬하면 편하겠지만, 금지를 먹었으므로
        # 하나하나 다시 뽑아서 count_list를 만들어준다.
        # 이 카운트 리스트가 원래의 카운트 리스트와 일치하면 빙고!
        # 베이비 진 달성 조건을 2개 달성한 조합이 등장하고, 출력 조건을 True로 반환한다.
        for numbers in tmp_list:
          compare_count_list[int(numbers)] += int(1)
        if compare_count_list == count_list:
          answer = True
          
    if answer == True:
      print("Baby-Gin")
    else:
      print("Lose")
        