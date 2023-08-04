# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# input = lambda: sys.stdin.readline().rstrip('\r\n')

N, goal = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
answer = 0
if goal < 0:
    num_list = sorted(num_list,reverse=True)
def bf_recur_solution_minus(idx, k, N, goal, visit_string):
    global answer
    if idx >= N:
        if k == goal and visit_string not in visited:
            visited.add(visit_string)
            if visit_string[-1] == '1':
                answer += 1
        return
    elif k < goal:
        return
    elif k == goal and visit_string not in visited:
        if visit_string[-1] == '1':
            answer += 1
        visited.add(visit_string)
        bf_recur_solution_minus(idx + 1, k + num_list[idx], N, goal, visit_string+'1')
        bf_recur_solution_minus(idx + 1, k, N, goal, visit_string+'0')
    else:
        bf_recur_solution_minus(idx + 1, k + num_list[idx], N, goal, visit_string+'1')
        bf_recur_solution_minus(idx + 1, k, N, goal, visit_string+'0')


def bf_recur_solution_plus(idx, k, N, goal, visit_string):
    global answer
    if idx >= N:
        if k == goal and visit_string not in visited:
            visited.add(visit_string)
            if visit_string[-1] == '1':
                answer += 1
        return
    elif k > goal:
        return
    elif k == goal and visit_string not in visited:
        if visit_string[-1] == '1':
            answer += 1
        visited.add(visit_string)
        bf_recur_solution_plus(idx + 1, k + num_list[idx], N, goal, visit_string+'1')
        bf_recur_solution_plus(idx + 1, k, N, goal, visit_string+'0')
    else:
        bf_recur_solution_plus(idx + 1, k + num_list[idx], N, goal, visit_string+'1')
        bf_recur_solution_plus(idx + 1, k, N, goal, visit_string+'0')


if goal < 0:
    for check in range(N):
        visited = set()
        if num_list[check] < goal:
            break
        bf_recur_solution_minus(check+1, num_list[check], N, goal, '1')
else:
    for check in range(N):
        visited = set()
        if num_list[check] > goal:
            break
        bf_recur_solution_plus(check + 1, num_list[check], N, goal, '1')
print(answer)

"""
15 -7
6 -4 1 3 -8 5 -4 -3 7 -4 9 -9 -3 -4 -4

정답: 1203
출력: 1201


15 17
9 -2 2 -2 1 -3 5 -3 -4 1 0 -9 0 7 1

정답: 328
출력: 327


19 6
-8 2 -8 -8 -7 -8 -5 2 1 4 5 7 -6 7 4 8 -3 -5 -4

정답: 6921
출력: 6918
"""

