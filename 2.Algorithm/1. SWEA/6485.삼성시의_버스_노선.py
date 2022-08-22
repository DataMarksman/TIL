# SWEA.6485 삼성시의 버스 노선
# 설계 목적: 받자마자 체크할 수는 없을까?
# 1. 정류장 정보 받자마자 해당 범위에 += 1 입력
# 2. 위치 정보 받자마자 해당 위치 지나가는 정류장 개수 바로 반환 및 저장
# 개선점: 있나요?

T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    count_list = [0] * 5001
    for count_up in range(N):
        A, B = map(int, input().split())
        for write_down in range(A, B+1):
            count_list[write_down] += 1
    P = int(input())
    ans_list = []
    for check in range(P):
        C = int(input())
        ans_list += [count_list[C]]
    print(f'#{case_num}', *ans_list)
