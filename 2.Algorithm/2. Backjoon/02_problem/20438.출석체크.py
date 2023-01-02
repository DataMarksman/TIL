# BOJ. 20438 출석체크
# 설계 의도: 도출 답안의 구조화
# 1. 뭔가 여러번 출력 시킬 거라고 대놓고 말하는 듯한 input 이다.
# 2. 잠자는 학생들을 위한 체크용 set을 만든다.
# 3. 뽑힌 학생들을 위한 리스트를 오름차순으로 정렬하고, 하나씩 뽑는다.
# 4. 뽑힌 값을 N+2 까지 배증 하면서 밟는거 전부 출결 표기 ( = 0 ) 해준다.
# 5. 이 때, 뽑힐 예정인 아이 중에 sending 값이 있다면, 가뿐하게 지워준다.
# 6. 이렇게 전부 마킹해주고, 다시 check_list를 돌면서 누적합을 해준다.

# 개선점:
# 1. 현재 속도 148ms 더 빠르게 안되나? 싶은 마음이 있다.
import sys
N, K, Q, M = map(int, sys.stdin.readline().split())
check_list = [0, 0, 0] + [1]*(N)
sleeping_set = set(map(int, sys.stdin.readline().split()))
sending_set = sorted(list(map(int, sys.stdin.readline().split())))
while sending_set:
    pick = sending_set.pop(0)
    if pick not in sleeping_set:
        sending = int(pick)
        while sending <= N + 2:
            if sending not in sleeping_set:
                check_list[sending] = 0
            elif sending in sending_set:
                sending_set.remove(sending)
            sending += pick
for summing in range(4, N+3):
    check_list[summing] += check_list[summing-1]
for checking in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(check_list[end] - check_list[start-1])
"""
50 4 5 2
24 15 27 43
3 4 6 20 25
3 52
10 20

5 1 1 1
3
3
3 7

50 4 5 2
24 15 27 43
3 4 6 20 25
3 25
26 52
"""