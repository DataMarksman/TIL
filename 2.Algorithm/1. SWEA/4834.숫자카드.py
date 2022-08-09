# 4834.숫자카드

T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    origin_num = int(input())
    count_list = [0]*12
    num_list = []
    for i in range(N):
        num_list += [origin_num % 10]
        origin_num = origin_num // 10
    for number in num_list:
        count_list[number] += 1
    max_count = 0
    max_number = 0
    for count in range(len(count_list)):
        if count_list[count] > max_count:
            max_count = count_list[count]
            max_number = count
    print(f'#{case_num} {max_number} {max_count}')
