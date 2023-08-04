# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip('\r\n')

T = int(input())
for case_num in range(1, T + 1):
    top = 0
    ans = 0
    end_list = [0]*123
    count_list = [0]*123
    visited = set()
    N = int(input())
    guest_list = list(input())
    for first_check in range(N-1, -1, -1):
        if count_list[ord(guest_list[first_check])] == 0:
            end_list[ord(guest_list[first_check])] = first_check
        count_list[ord(guest_list[first_check])] += 1

    for get_ans in range(N-1, -1, -1):
        if guest_list[get_ans] not in visited:
            visited.add(guest_list[get_ans])




