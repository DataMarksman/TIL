# PRG. [PCCP 모의고사 #1] 체육대회

# 설계 의도: 어떤 것을 기준점으로 DFS를 돌려야 하는가?

# 로직의 Main 개념:DFS + 재귀 + visited SET의 id 개념 + 파이썬 스코프(nonlocal)

# 개선점:
# 1.

# DFS 기반 풀이
def solution(ability):

    # DFS용 재귀 함수 (n 번째 스포츠, 이미 선택한 선수 목록, 선수 능력 합계)
    def recur(idx, visited, ability_sum):

        # 바로 위의 스코프를 위해 nonlocal을 사용합니다.
        # [Tip!] global과 nonlocal의 차이점을 알아봅시다.
        nonlocal answer

        # visited의 id 값을 갱신해주지 않으면, 재귀 함수 과정에서 오류가 발생합니다.
        # [Tip!] 객체의 ID 값에 대해 알아봅시다.
        visited = set(visited)

        # 각 스포츠 별로 선수단을 다 뽑았으면, 함수를 종료합니다.
        if len(visited) == sports:
            # answer의 값을 최대값으로 갱신해줍니다.
            answer = max(ability_sum, answer)

        # 아직 뽑는 과정이 진행 중 이라면, 각 스포츠별 모든 선수들을 뽑아보는 과정을 진행합니다.
        else:

            # 각 학생들을 순회하면서
            for check in range(students):
                # 아직 뽑지 않은 학생들을
                if check not in visited:
                    # 각 스포츠 후보군으로 넣고 다음 스포츠의 선수를 뽑기 위해 다시 이 함수에 넣습니다.
                    # 이렇게 다시 자기 자신을 참고하는 함수를 재귀 함수라고 합니다.
                    recur(idx+1, visited | {check, }, ability_sum + ability[check][idx])
    # 스포츠의 개수는 각 선수들이 가지고 있는 능력치의 개수와 동일합니다.
    sports = len(ability[0])
    # 학생들의 전체 수는 제시된 리스트의 길이와 동일합니다.
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
