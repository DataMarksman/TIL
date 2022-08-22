# SWEA. 14559. 배수 그래프
# 설계 목적:
# 1. 서로가 공약수가 있거나 서로를 곱한 수가 N 이하의 범위에 있다면, 두 점은 이어진다.
# 2. 그러므로 이렇게 이어지는 다리를 매 순간 직접 찾아가면서 정답까지 찾는다.
# 3. 단, 각 다리를 두번 이상 사용하는 것은 패턴 반복일 수 있으므로, 각 다리는 한번씩만 사용한다.
# 4. 중간에 이미 나왔던 종점까지의 길이보다 길게 나오게 되면 백트래킹으로 컷.
# 5. 출력시, ans_list에 들어간 값 들 중 가낭 작은 값, 즉 최단 거리 혹은 값이 없을 경우 -1 출력
# 개선점:
# 1. 현재 시간초과 발생. -> 값이 커서 그렇다면, 단순하게 이어지냐 여부만 추리려고 ver2 제작.
def lining(check_list, n, k):
    global ans_list
    if n >= M:
        pass
    elif ans_list is True and n >= min(ans_list):
        pass
    elif n == 0:
        for checking in range(M):
            if start % multiple_list[checking][0] == 0:
                if end % multiple_list[checking][1] == 0:
                    ans_list += [1]
                else:
                    check_list[checking] = 1
                    k = multiple_list[checking][1]
                    lining(check_list, n+1, k)
                    check_list[checking] = 0
    else:
        for checking in range(M):
            if check_list[checking] == 0:
                t = multiple_list[checking][0]
                if k % t == 0 or t % k == 0 or N >= t*k:
                    if end % multiple_list[checking][1] == 0:
                        ans_list += [n + 1]
                    else:
                        check_list[checking] = 1
                        k = multiple_list[checking][1]
                        lining(check_list, n + 1, k)
                        check_list[checking] = 0


T = int(input())
for case_num in range(1,T+1):
    N, S, E = map(int, input().split())
    N = int(N)
    start = int(S)
    end = int(E)
    M = int(input())
    multiple_list = []
    ans_list = []
    for write_in in range(M):
        multiple_list += [list(map(int, input().split()))]
    lining([0]*M, 0, 0)
    if ans_list:
        print(f'#{case_num} {min(ans_list)}')
    else:
        print(f'#{case_num} {-1}')
