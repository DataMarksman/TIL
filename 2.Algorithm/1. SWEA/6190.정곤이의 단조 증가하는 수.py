# SWEA.6190. 정곤이의 단조 증가하는 수
# 실행시간: 408ms
# 설계 목적: 백트래킹 + set() 연산자 활용
# 1. 먼저 백트래킹을 위해 원본 숫자 리스트를 내림차순으로 정렬한다.
#   -> 큰수들 끼리 곱한 것들 중에 답이 나오면 이후 나올 답들이 걸러질 확률이 높다.
# 2. answer의 기본값을 -1로 책정하여, 증가하는 수가 갱신되지 않으면 그대로 -1이 출력되도록 한다.
# 3. str로 바꾸고 리스트.pop()을 하면 시간적으로 손해가 많으므로, %10 연산을 활용한다.
# 4. 조건을 통과한 수가 이미 나왔던 answer 보다 크다면 answer을 갱신한다.
# 5. 이후 부터는 곱한 값이 answer보다 작으면 바로 거른다.
# 개선점:
# 1.

T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort(reverse=True)
    multiple_set = set()
    answer = -1
    for i in range(N):
        for j in range(N):
            flag = True
            if i < j and num_list[i] * num_list[j] > answer:
                C = num_list[i] * num_list[j]
                A = 9
                while C > 0:
                    B = C % 10
                    if A >= B:
                        A = int(B)
                        C = C//10
                    else:
                        flag = False
                        break
                if flag and num_list[i] * num_list[j] > answer:
                    answer = num_list[i] * num_list[j]

    print(f'#{case_num} {answer}')
