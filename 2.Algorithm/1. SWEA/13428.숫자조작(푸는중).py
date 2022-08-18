# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T+1):
    number = list(input())
    max_num = [0, 0]
    second_max = [0, 0]
    min_num = [10, 0]
    second_min = [10, 0]
    for checking in range(len(number)):
        if number[::-1][checking] != 0:
            if number[::-1][checking] < second_max[0]:
                second_max[0] = number[::-1][checking]
                second_max[1] = checking
                if second_max > max_num:
                    second_max , max_num = max_num, second_max
            elif number[::-1][checking] < min_num[0]:
                second_max[0] = number[::-1][checking]

    print(f'#{}')










"""
4
12345
54321
142857
10000
"""