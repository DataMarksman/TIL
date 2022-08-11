# 2차원 배열 연습 문제

T = int(input())
for case_num in range(1,T+1):
    num_list = list(map(int,input().split()))
    ans_count = 0
    ans = 0
    for check in range(1<<len(num_list)):
        pick_list = []
        for pick in range(len(num_list)):
            if check & (1 << pick):
                pick_list.append(num_list[pick])
                
        if sum(pick_list) == 0:
            ans_count += 1
    if ans_count == 1:
        ans = 0
    else:
        ans = 1
            
    print(f'#{case_num} {ans}')