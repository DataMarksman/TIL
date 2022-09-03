# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T + 1):
    num_list = list(map(int, input().split()))
    num_list.sort(reverse=True)
    answer_set = set()
    min_number = 0
    for i in range(5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                if i < j < k:
                    answer_set.add(int(num_list[i]+num_list[j]+num_list[k]))
    answer_list = list(answer_set)
    answer_list.sort(reverse=True)
    ans = answer_list[4]
    print(f'#{case_num} {ans}')