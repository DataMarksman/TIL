T = int(input())

for i in range(T):
    alp_list = list("abcdefghijklmnopqrstuvwxyz")   # 알파벳 str을 리스트 형식으로 받아줍니다. = 알파벳을 좌표로 받아오기 위함
    count_list = list([0]*26)                       # 각 좌표별 알파벳의 개수를 카운팅하는 리스트 입니다.
    case_num = int(input())                         # 단어를 몇개 받을 건지 먼저 선언해줍니다.
    word_stock = []                                 # 받는 단어들을 저장해둘 장소이고,
    alp_stock = []                                  # 해당 단어들의 알파벳만 빼서 넣어둘 장소입니다.
    for j in range(case_num):                       # 받는 단어 개수만큼 반복하는데,
        inp_word = str(input())                     # 단어를 받아서 inp_word에 임시저장하고
        word_stock += [str(inp_word)]               # 단어 저장소에는 str로 저장하며
        alp_stock += list(str(inp_word))            # 알파벳 저장소에는 알파벳으로 저장합니다. (list로 분해하여)
    for k, alp in enumerate(alp_list):              # 앞서 만들어놓은 알파벳 좌표 리스트를 이뉴머레이트로 (좌표,알파벳)의 튜플로 구성된 리스트로 뽑아오고 for문을 돌립니다.
        count_list[k] = alp_stock.count(alp)        # 이렇게 돌린 for문에서 각 A부터 Z까지 하나하나의 알파벳 개수를 알파벳 저장소에서 카운팅하여 카운트 리스트에 순서대로 저장합니다.
    if count_list.count(int(0)) != 0:               # 이렇게 저장되면, A의 개수가 count_list[0]에 저장되는 방식으로 저장되는데, 이를 통해 요소 중에 0이 없으면 적어도 한번씩 들어간 것으로 간주합니다.
        print('이 단어들은 알파벳을 전부 포함하고 있지 않습니다.')
        continue
    
    # 여기까지가 알파벳 별 출현 빈도 구한 리스트 도출하는 과정.
    
    picked_word = []                                # 이를 기반으로 2번 이상 등장한 알파벳으로 조합할 수 있는 단어들만 추려내는 과정을 밟습니다.
    for word in word_stock:                                 # 자, 여기서 부터 메인입니다. 아까 받았던 단어 저장소에서 단어들을 하나씩 가져옵니다.
        if set(list(word)) & picked_alp == len(list(word)): # 그 단어들을 분해하여 각 알파벳이 아까 한번 걸렀던 2번 이상 등장한 알파벳 집합에 들어있는지 확인합니다.
            picked_word += [word]                           # 자, 단어들이 전부 알파벳 조합에 들어가 있으면, 해당 단어를 픽 단어에 넣습니다. 일단 여기에서는 중복 알파벳은 고려하지 않습니다.
    
    for i in range(len(count_list)):
        count_list[i] -= 1

    for case_rutin in range(len(picked_word)):
        tmp_count = count_list[:]
    #    if list(str(picked_word[case_rutin]))

    # 각 뽑은 위치값을 저장하는 코드 제작하여 set()으로 묶으면 쉽게 계산 가능
    # word_list를 sort로 정렬 후, 해당 단어의 좌표를 뽑아서 리스트의 [0]*len(wordlist)에서 해당 값을 바꿈
    # 예를 들어 5개의 단어를 조합하는 문제에서 10010 10101과 같이 join을 통해 리스트 값을 하나의 코드로 바꾸고 동질성 검사로 바로 추적 가능 



# 아이디어 1: 일단 모든 단어를 분해하여 알파벳을 스톡에 저장, a~z 까지의 위치 값을 생각하여 count_list 리스트를 만들고
#           모든 단어들을 전부 집어넣은 다음 카운트 리스트에 0이 있는지 확인하여 없으면 다음 단계로 진행.
#           그렇다면 모든 알파벳이 한번씩은 나왔다는 이야기 이므로, 반대로 모든 리스트의 값에서 1을 빼줌.
#           남은 알파벳들로 만들 수 있는 단어를 역추적하는 방식으로 만들 수 있는 단어집 케이스 도출.
#           이걸 그냥 조합 돌리면 되는 부분이라고 생각합니다.