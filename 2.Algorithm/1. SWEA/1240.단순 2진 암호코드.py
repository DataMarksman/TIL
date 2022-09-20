# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

ans_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
            '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
            '0110111': 8, '0001011': 9, }

T = int(input())
for case_num in range(1, T + 1):
    N, K = map(int, input().split())
    ans = 0
    for checking in range(N):
        line = input()
        if ('1' not in line) and (ans != 0):
            continue
        elif '1' in line:
            decode_list = []
            for decoding in range(len(line)//7):
                print(decoding, '번째 라인:', line[decoding*7:(decoding*7)+7])
                if line[decoding*7:(decoding*7)+7] in ans_dict:
                    decode_list.append(ans_dict[line[decoding*7:(decoding*7)+7]])
            print(decode_list)
            temp_ans = 0
            for i in range(len(decode_list)):
                if i % 2 == 0:
                    temp_ans += decode_list[i]*3
                else:
                    temp_ans += decode_list[i]
            else:
                if temp_ans % 10 == 0 and temp_ans > 0:
                    ans = sum(decode_list)

    print(f'#{case_num} {ans}')