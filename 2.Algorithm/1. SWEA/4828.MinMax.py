# 4828. Min Max
# 기본 설계: MAX함수를 구현하는 과정에서 같이 Min도 구해서 차이 값을 도출

T = int(input())
for case_num in range(1,T+1):
    case = int(input())
    case_list = list(map(int,input().split()))        # 각 숫자를 리스트 형식으로 인풋
    max_num = int(case_list[0])                       # 최소값에 리스트 첫번째 값을 임시 배정
    min_num = int(case_list[0])                       # 최대값에도 첫번째 값을 임시 배정
    for find_num in range(1,len(case_list)):          # 이후 받은 리스트를 하나씩 돌면서
        if case_list[find_num] > max_num:             # 최대값 보다 크다면 최대값을 대치
            max_num = case_list[find_num]
        elif case_list[find_num] < min_num:           # 최소값 보다 작다면 최소값을 대치
            min_num = case_list[find_num]
    print(f'#{case_num} {max_num-min_num}')                # 이를 통해 구한 max - min 값을 출력
