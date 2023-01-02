# PRG. [PCCP 모의고사 #1] 체육대회

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

def solution(ability):
    def recur(idx, visited, ability_sum):
        nonlocal answer
        visited = visited[:]
        if sum(visited) == length:
            answer = max(ability_sum, answer)
            return
        elif idx == members:
            return
        else:
            for check in range(length):
                if visited[check] == 0:
                    visited[check] = 1
                    recur(idx+1, visited, ability_sum + ability[idx][check])
                    visited[check] = 0
            recur(idx+1, visited, ability_sum)
    length = len(ability[0])
    members = len(ability)
    answer = 0
    recur(0, [0]*length, 0)
    return answer


print(solution(list(map(int, input().split()))))