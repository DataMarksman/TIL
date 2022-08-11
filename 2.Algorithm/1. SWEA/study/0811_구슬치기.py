# 구슬치기

T = int(input())
for case_num in range(1,T+1):
    num_list = list(map(int,input().split()))
    check_list = [0]*int(max(num_list)+1)
    
    for numbers in num_list:
        check_list[numbers] += 1
    for check in range(len(check_list)):
        if check_list[check] == 1:
            print(f'#{case_num} {check}')
            break
