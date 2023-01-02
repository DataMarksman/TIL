# PRG. [PCCP 모의고사 #1] 체육대회

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점: 단순 BFS 로 하면 파이썬에서는 시간초과 난다.
# 1.

# def solution(ability):
#     def recur(idx, K, ability_sum):
#         nonlocal answer
#         if K == sports or idx >= students:
#             answer = max(ability_sum, answer)
#         else:
#             recur(idx+1, K, ability_sum)
#             for check in range(sports):
#                 if visited[check] == 0:
#                     visited[check] = 1
#                     recur(idx+1, K+1, ability_sum + ability[idx][check])
#                     visited[check] = 0
#
#     sports = len(ability[0])
#     students = len(ability)
#     visited = [0]*sports
#     answer = 0
#     recur(0, 0, 0)
#     return answer

def solution(ability):
    def recur(idx, visited, ability_sum):
        nonlocal answer
        visited = set(visited)
        if len(visited) == sports:
            answer = max(ability_sum, answer)
        else:
            for check in range(students):
                if check not in visited:
                    recur(idx+1, visited | {check, }, ability_sum + ability[check][idx])
    sports = len(ability[0])
    students = len(ability)
    answer = 0
    recur(0, set(), 0)
    return answer

"""
# 이터툴즈 활용
from itertools import combinations


def solution(ability):
    answer = 0
    people = len(ability)
    sports = len(ability[0])
    check_set = set(combinations(list(i for i in range(sports)), sports))
    while check_set:
        pick = check_set.pop()




    return answer
"""

"""
# DFS 코드
answer = 0
def DFS(L, s, ability, check):
    global answer
    n = len(ability)        # 학생 수
    m = len(ability[0])     # 종목 개수
    
    if L == m:
        answer = max(answer, s)   # 능력치 합의 최댓값을 구함
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                DFS(L+1, s + ability[i][L], ability, check)
                check[i] = 0


def solution(ability):
    global answer
    check = [0]*len(ability)
    DFS(0, 0, ability, check)      
    # Level, sum, ability, check
    # L : level (고를 수 있는 학생 수 중 몇 명째 선택한 것인지), sum : 능력치의 합
    
    return answer

"""


def solution(ability):
    answer = 0
    check = [0] * len(ability)

    def DFS(L, s, ability, check):
        nonlocal answer
        n = len(ability)  # 학생 수
        m = len(ability[0])  # 종목 개수

        if L == m:
            answer = max(answer, s)  # 능력치 합의 최댓값을 구함
        else:
            for i in range(n):
                if check[i] == 0:
                    check[i] = 1
                    DFS(L + 1, s + ability[i][L], ability, check)
                    check[i] = 0

    DFS(0, 0, ability, check)

    return answer