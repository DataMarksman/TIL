# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:
import heapq

def solution(alp, cop, problems):
    alp_heapQ = []
    cop_heapQ = []
    visited = set()
    time = 0
    # HeapQ 로 올리는 정보 (alp, cop, alp_rew, cop_rew, id, time)
    for get_problem in range(len(problems)):
        heapq.heappush(alp_heapQ, (problems[get_problem][0], problems[get_problem][1], problems[get_problem][2], problems[get_problem][3], get_problem, problems[get_problem][4]))
        heapq.heappush(cop_heapQ, (problems[get_problem][1], problems[get_problem][0], problems[get_problem][2], problems[get_problem][3], get_problem, problems[get_problem][4]))

    while len(alp_heapQ) > 0 and len(cop_heapQ) > 0:
        print(alp)
        print(cop)
        print(time)
        print('==============================')
        if alp >= alp_heapQ[0][0] and cop >= alp_heapQ[0][1]:
            if alp_heapQ[0][4] in visited:
                heapq.heappop(alp_heapQ)
            else:
                pick = heapq.heappop(alp_heapQ)
                visited.add(pick[4])
                alp += pick[2]
                cop += pick[3]
                time += pick[5]
        elif alp >= cop_heapQ[0][1] and cop >= cop_heapQ[0][0]:
            if cop_heapQ[0][4] in visited:
                heapq.heappop(cop_heapQ)
            else:
                pick = heapq.heappop(cop_heapQ)
                visited.add(pick[4])
                alp += pick[2]
                cop += pick[3]
                time += pick[5]
        else:
            alp_check = max(alp_heapQ[0][0] - alp, alp_heapQ[0][1] - cop)
            cop_check = max(cop_heapQ[0][1] - alp, cop_heapQ[0][0] - cop)
            if alp_check <= cop_check:
                time += alp_check
                if alp_heapQ[0][0] - alp > alp_heapQ[0][1] - cop:
                    alp += alp_check
                else:
                    cop += alp_check
            else:
                time += cop_check
                if cop_heapQ[0][0] - alp > cop_heapQ[0][1] - cop:
                    alp += cop_check
                else:
                    cop += cop_check
    answer = time
    return answer

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))