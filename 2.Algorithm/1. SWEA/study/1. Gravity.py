T = int(input())
for case_num in range(T):
    N, M = map(int,input().split())
    box_list = list(map(int,input().split()))
    drop_list = [0]*N
    max_drop = int(0)
    for i in range(N):
        for compare_box in box_list[i:len(box_list)]:
            if box_list[i] > compare_box:
                drop_list[i] += 1
        if drop_list[i] > max_drop:
            max_drop = drop_list[i]
    print(f'#{case_num+1} {max_drop}')
    
