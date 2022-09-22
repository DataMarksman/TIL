# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
ans_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
            '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
            '0110111': 8, '0001011': 9, }


T = int(input())
for case_num in range(1, T + 1):
    N, K = map(int, input().split())
    ans = 0
    for checking in range(N):
        lines = input()
        if '1' not in lines or ans != 0:
            continue
        else:
            decode_list = []
            idx = 0
            for first_check in range(len(lines)-55):
                if (lines[first_check:first_check+7] in ans_dict) and (lines[first_check+7:first_check+14] in ans_dict):
                    idx = first_check
                    break
            lines = lines[idx:]
            for decoding in range(8):
                if str(lines[decoding*7:(decoding*7)+7]) in ans_dict:
                    decode_list.append(ans_dict[str(lines[decoding*7:(decoding*7)+7])])
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