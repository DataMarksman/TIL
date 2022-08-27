# SWEA.4613. 러시아 국기 같은 깃발
# 설계 목적: 보드 만들 필요 없이, 그냥 칠하는 데 필요한 횟수 빼내자.
# 1. 자료 받을 때, 각 행의 W B R 개수 받아서 각각 리스트에 저장하기
# 2. 이렇게 저장된 리스트를 for 문으로 불러오면, 슬라이싱으로 필요한 값만 빼올 수 있음.
# 개선점:
# 1.


T = int(input())
for case_num in range(1, T + 1):
    N, M = tuple(map(int, input().split()))
    W_count = [0]*N
    B_count = [0]*N
    R_count = [0]*N
    ans_set = set()
    for put_in in range(N):
        write_in = list(input())
        for check in range(M):
            if write_in[check] == 'W':
                W_count[put_in] += 1
            elif write_in[check] == 'B':
                B_count[put_in] += 1
            else:
                R_count[put_in] += 1
    for coloring in range(1, N-1):
        for lining in range(coloring, N-1):
            sum_W = sum(W_count[:coloring])
            sum_B = sum(B_count[coloring:lining+1])
            sum_R = sum(R_count[lining + 1:])
            ans = M*N - int(sum_W + sum_B + sum_R)
            ans_set.add(ans)
    print(f'#{case_num} {min(ans_set)}')
