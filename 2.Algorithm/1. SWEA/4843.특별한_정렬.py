T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort(reverse=True)
    ans_list = []
    for idx in range(5):
        ans_list += [num_list[idx]]
        ans_list += [num_list[(N-1)-idx]]
    ans = f'#{case_num}'
    print(ans, *ans_list)