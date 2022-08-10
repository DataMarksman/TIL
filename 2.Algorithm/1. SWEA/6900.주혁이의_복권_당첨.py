# 6900. 주혁이의 복권 당첨

T = int(input())
for case_num in range(1,T+1):
    N, M = map(int,input().split())
    match_dict = []
    for dict_input in range(N):
        lotto, prize = input().split()
        match_dict += [{'code': lotto,'prize': int(prize)}]
    print(match_dict)