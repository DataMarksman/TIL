R, C = map(int,input().split())
alp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
list_stock= []
for i in range(R):
    tmp_list = list(map(str,input()))
    list_stock += [tmp_list]
ans_list = []
for k in range(C):
    tmp_pileup = []
    for t in range(R):
        tmp_pileup += [list_stock[t][k]]
    ans_list += [tmp_pileup]
answer_word = str('')
for case_count in range(C):
    alp_count = [0]*26
    answer_alp = str('')
    for case_cal in range(R):
        alp_count[alp.index(ans_list[case_count][case_cal])] += 1
    for root in range(len(alp_count)):
        if root == 0 & alp_count[0] != 0:
            answer_alp = alp_count[root]
        elif alp_count[root] == 0:
            pass
        elif (alp_count[root] != 0) & (alp_count[root] < alp_count[root-1]):
            answer_alp = alp_count[root]
            print(answer_alp)
    answer_word += answer_alp
print(answer_word)
            
        
    
# 문제 구조 정리

# 먼저 이건 2차원 배열 문제로 풀고자 한다.
# 정확하게는 2차원 배열로 바라본 뒤에, 각 열을 케이스 하나씩으로 두고 풀고자 한다.
# 앞서 A~Z를 리스트로 출력하여 0~25의 수로 위치를 가져올 수 있도록 세팅하고
# 각 데이터를 받은 다음 X,Y 축을 뒤집어 새로운 리스트를 만든다.
# 해당 리스트의 각 요소를 alp와 대조하여 각 ans_list[0]~[25] 까지의 위치에 += 1을 하고
# 이를 통해 1번 이상 등장하였으나 가장 적은 빈도, 가장 높은 순서 (A에 가까운)를 가지는 알파벳을 도출 할 수 있다.
# 이 과정을 각 열만큼 시행하면 원 데이터의 각 행 데이터에서의 거리가 가장 가까운 중간 지점의 데이터를 작성 할 수 있게 된다.
#