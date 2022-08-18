# 9386. 연속한 1의 개수

T = int(input())
for case_num in range(1,T+1):
    L = int(input())
    list_A = list(str(input()))
    count_digit = 0
    max_digit = 0
    for digit in list_A:
        if int(digit) == 1:
            count_digit += 1
            if count_digit > max_digit:
                max_digit = count_digit
        elif int(digit) == 0:
            count_digit = 0
    print(f'#{case_num} {max_digit}')

    """_int() 쓰지 않는 방법_
    T = int(input())
    for case_num in range(1,T+1):
    L = int(input())
    list_A = list(str(input()))
    count_digit = 0
    max_digit = 0
    for digit in list_A:
        if digit == '1':
            count_digit += 1
            if count_digit > max_digit:
                max_digit = count_digit
        elif digit == '0':
            count_digit = 0
    print(f'#{case_num} {max_digit}')
    """