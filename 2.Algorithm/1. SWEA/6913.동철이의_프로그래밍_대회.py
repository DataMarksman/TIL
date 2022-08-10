# 동철이의 프로그래밍 대회!
T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    case_result = []
    result_count = []
    for case in range(N):
        case_result = map(int,input().split())
        result_count += [sum(case_result)]
    max_solv = max(result_count)
    num_people = result_count.count(max_solv)    
    print(f'{i+1}# {num_people} {max_solv}')