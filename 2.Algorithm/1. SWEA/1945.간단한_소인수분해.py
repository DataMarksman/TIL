# SWEA. 1945 간단한 소인수 분해
# 설계 목적:
# 1. 앞에서부터 나눠보고 될 것 같으면 그 몫을 다시 원본 값에 배정하고 계속 돌리기.
# 2. 안나눠질 때, 다음 숫자로 넘어가기.
# 개선점: 있나요?

T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    div_list = [2, 3, 5, 7, 11]
    div_count = [0]*5
    for div_num in range(5):
        while N % div_list[div_num] == 0:
            div_count[div_num] += 1
            N = N // div_list[div_num]
    print(f'#{case_num}', *div_count)





