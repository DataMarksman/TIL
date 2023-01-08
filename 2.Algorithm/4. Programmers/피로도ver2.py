# PRG. 피로도

# 설계 의도: 던전의 등장 패턴을 모두 구하면 내가 원하는 결과도 얻을 수 있다.

# 로직의 Main 개념: 순열, 패턴 나열

# 개선점: 이 문제는 8개라서 이런 꼼수가 가능하다. 던전의 개수가 더 많아지면 다음의 방법을 활용해보자.
# DFS(재귀) + union-find + 백트래킹 :
# 요컨데, 가장 높은 피로도 수치를 요구하는 던전에서 소모 피로도 만큼 사용하는 방식이라면,
# 해당 요구치에서 소모치만큼 내려온 값을 연결해준다. 그리고 재귀에 진입하며, 이번 던전을 통과하지 않는 케이스도 재귀로 진입한다.
# 다음 던전에서 요구치에 따라

from itertools import permutations

# 요컨데 최적의 케이스를 찾는 것은 모든 던전의 순서를 나열하면 캐치할 수 있다.
# ex) 6개의 던전 중에서 1 3 2 4 순으로 공략하는게 최대 4개를 반환하는 케이스라면
# -> 1 3 2 4 5 6 도 맞는 패턴이 된다. 또한, 6을 나중에 깰수 없다면, 1 3 2 6 4 5도 맞는 케이스가 된다.

def solution(k, dungeons):
    # 던전의 총 개수를 저장해준다. 최대 8개 이므로 순열로 풀 수 있다.
    # [Tip!] 만약 던전 개수가 훨씬 많아진다면, 탐색 과정의 백트래킹과, union-find 알고리즘을 활용해야한다.
    length = len(dungeons)

    # 갱신해줄 초기 answer 값이다.
    answer = 0

    # 나올 수 있는 던전의 순서 패턴을 전부 저장해준다.
    pattern_cases = set(permutations([i for i in range(length)], length))

    # 하나씩 뽑으면서 전체 케이스를 확인한다.
    while pattern_cases:
        pick_case = pattern_cases.pop()

        # 이번 패턴에서의 클리어한 던전 개수를 저장할 변수.
        clear_count = 0

        # 남은 체력을 의미한다.
        remain_HP = int(k)

        # idx 기반으로 탐색해준다.
        for check in range(length):

            # 이번 던전을 진입 가능하면 무조건 진입한다.
            # 이번 던전을 진입하지 않는것이 효율적이라고 해도, 그 케이스는 다른 패턴에서 다뤄 줄 것이다.
            if dungeons[pick_case[check]][0] <= remain_HP:
                # 피로도를 소모해주고 던전 클리어 카운트를 한개 늘려준다.
                remain_HP -= dungeons[pick_case[check]][1]
                clear_count += 1

                # 만약 남은 체력이 없으면 바로 종료시킨다.
                if remain_HP <= 0:
                    break

        # answer 를 경신시켜준다.
        answer = max(clear_count, answer)
    return answer