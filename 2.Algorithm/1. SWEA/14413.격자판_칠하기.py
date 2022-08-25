# SWEA.
# 설계 목적:
# 1. 예전에 풀어본 문제랑 비슷하네... x+y 좌표가 짝수냐 홀수냐로 체스판 만들 수 있음. 이거 응용
#   하지만 같은 문제를 같게 풀면 노잼이니까... 이번에는 그냥 받으면서 구조화 시킬께엽
# 개선점:
# 1.
T = int(input())
for case_num in range(1, T+1):
    N, M = tuple(map(int, input().split()))
    set_A = set()
    set_B = set()
    for put_in in range(N):
        write_in = list(input())
        for pick in range(M):
            set_A.add(write_in[pick]) if (put_in + pick) % 2 == 0 else set_B.add(write_in[pick])
    set_A.discard('?')
    set_B.discard('?')
    print(f'#{case_num} {"impossible" if set_A & set_B or len(set_B) > 1  or len(set_A) > 1  else "possible"}')

"""
3
3 1
#
?
.
6 1
?
?
?
?
?
?
2 1
.
.
"""