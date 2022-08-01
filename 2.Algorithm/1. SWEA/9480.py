T = int(input())

for i in range(T):
    alp_list = list("abcdefghijklmnopqrstuvwxyz")
    count_list = list([0]*26)
    case_num = int(input())
    word_stock = []
    alp_stock = []
    for j in range(case_num):
        word_stock += [str(j)]
        alp_stock += list(str(j))
    


# 아이디어 1: 일단 모든 단어를 분해하여 알파벳을 스톡에 저장, a~z 까지의 위치 값을 생각하여 count_list 리스트를 만들고
#           모든 단어들을 전부 집어넣은 다음 카운트 리스트에 0이 있는지 확인하여 없으면 다음 단계로 진행.
#           그렇다면 모든 알파벳이 한번씩은 나왔다는 이야기 이므로, 반대로 모든 리스트의 값에서 1을 빼줌.
#           남은 알파벳들로 만들 수 있는 단어를 역추적하는 방식으로 만들 수 있는 단어집 케이스 도출.