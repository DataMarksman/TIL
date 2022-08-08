for case_num in range(10):
    numbers = int(input())
    apartment_list = list(map(int,input().split()))
    all_checked = int(0)
    for i in range(2,numbers+2):
        if apartment_list[i] > (apartment_list[i-1] and apartment_list[i-2] and apartment_list[i+1] and apartment_list[i+2]):
            for compare_num in i-1,i+1,i+2:
                view_count= apartment_list[i] - apartment_list[i-2]
                if apartment_list[i] - apartment_list[compare_num] < view_count:
                    view_count = apartment_list[i] - apartment_list[compare_num]
                all_checked += view_count
    print(f'#{case_num+1} {all_checked}')