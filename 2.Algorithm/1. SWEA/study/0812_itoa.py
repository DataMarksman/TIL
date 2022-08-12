# itoa
'''
while True:
    case_num = 1
    word = input()
    print(f'#{case_num} {word} {type(word)})')
    case_num += 1
'''
while True:
    case_num = 1
    digit = int(input())
    digit_list = []
    ans_list = []
    while digit > 0:
        digit_list += [digit % 10]
        digit = digit // 10
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for check in range(len(digit_list)-1, -1, -1):
        for numbers in range(len(num_list)):
            if digit_list[check] == int(num_list[numbers]):
                ans_list += [num_list[numbers]]
    ans = ''.join(ans_list)
    print(f'#{case_num} {ans} {type(ans)}')
