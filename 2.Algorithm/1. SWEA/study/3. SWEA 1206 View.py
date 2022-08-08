for i in range(10):
    numbers = int(input())
    apartment_list = map(int,input().split())
    view_list = [0]*(numbers+4)
    for i in range(2,len(apartment_list)-2):
        if apartment_list[i] > apartment_list[i-1]&apartment_list[i-2]&apartment_list[i+1]&apartment_list[i+2]:
            for check in [i-2,i-1,i+1,i+2]:
                view_count = int(255)
                if apartment_list[i] - apartment_list[check] < view_count:
                    view_count = apartment_list[i] - apartment_list[check]
                view_list[i] = view_count
    all_checked = int(0)
    for counts in view_list:
        all_checked += int(counts)
    print(f'#{i+1} {all_checked}')
    