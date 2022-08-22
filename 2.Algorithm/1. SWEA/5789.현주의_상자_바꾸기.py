# SWEA. 5789 현주의 상자 바꾸기
# 설계 목적:
# 1. 0을 비워두고 숫자 값 = 좌표로 인식하고 풀 도록 함.
# 2.
# 개선점: 있나요?

T = int(input())
for case_num in range(1,T+1):
    N, Q = map(int, input().split())
    ans_list = [0]*(N+1)
    for count_up in range(1, Q+1):
        L, R = map(int, input().split())
        for write_down in range(L, R+1):
            ans_list[write_down] = count_up
    print(f'#{case_num}', *ans_list[1:])
