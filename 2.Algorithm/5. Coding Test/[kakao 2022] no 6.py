import sys

# 재귀로 풀기 때문에 리커전 리미트를 올려줍니다.
sys.setrecursionlimit(10 ** 8)

# 델타 탐색용 좌표계입니다.
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

# 델타 탐색과 연동되는 탐색 방향별 할당 알파벳
alpha = ['d', 'l', 'r', 'u']

# Answer 저장용 변수
ans_string = ''

# 가로 50 X 세로 50 의 최대 idx 개수가 2500개 이므로, 2500개의 Set을 생성해줍니다.
visited_set = [set() for _ in range(2500)]


# 메인 Solution 함수입니다.
def solution(n, m, x, y, r, c, k):
    # 델타 탐색 간 좌표는 0부터 시작이므로, 각 시작점과 끝점의 좌표에서 1씩 빼준 값으로 배정해줍니다.
    start = (x - 1, y - 1)
    end = (r - 1, c - 1)

    # DFS용 재귀 함수 입니다.
    # dfs(현재 좌표, 지금까지 밟았던 기록, 진입 차수) 변수를 가지고 진행합니다.
    def dfs(idx, words, top):

        # global 스코프로 밖으로 던져준 변수에 visited 와 answer 를 저장해줍니다.
        global ans_string
        global visited_set

        # ans_string이 True 라면, 이미 답이 나온 상태이므로, Return 으로 백트래킹 해줍니다.
        if ans_string:
            return

        # 그렇지 않을 경우, 로직에 들어갑니다.
        else:

            # 백트래킹 용 조건문입니다.
            # 진입 차수가 탈출까지 진행해야하는 차수 -1, 즉 이번 진입 차수가 마지막 차수일 경우 마지막 로직을 진행합니다.
            if top == k - 1:

                # 재귀 함수 진입시 받아온 idx 튜플에서 idx 0 인 값을 X 좌표 값으로, idx 1 인 값을 Y 좌표 값으로 배정합니다.
                X = idx[0]
                Y = idx[1]

                # 델타 탐색을 진행합니다.
                for direction in range(4):
                    PX = X + dx[direction]
                    PY = Y + dy[direction]

                    # 만약 현재 좌표가 끝 지점과 일치한다면, ans_string을 채워주고 로직을 종료합니다.
                    if (PX, PY) == end:
                        ans_string = words + alpha[direction]
                        return

            # 마지막 차수가 아닐 경우, 일반 로직으로 진입합니다. 종료 로직만 없을 뿐 동일하게 델타 탐색 로직을 진행합니다.
            else:
                X = idx[0]
                Y = idx[1]
                for direction in range(4):
                    PX = X + dx[direction]
                    PY = Y + dy[direction]

                    # 델타 탐색으로 파악한 좌표가 미로의 범위 안에 있다면, 해당 좌표를 visited 에 넣어주고
                    # 해당 좌표를 기반으로 재귀용 dfs 함수를 진행합니다.
                    if 0 <= PX < n and 0 <= PY < m and (PX, PY) not in visited_set[top]:
                        dfs((PX, PY), words + alpha[direction], top + 1)
                        visited_set[top].add((PX, PY))

    # 재귀 함수를 실행하는 명령어입니다.
    dfs(start, '', 0)

    # 만약 ans_string이 존재한다면, 즉 k 만큼 진행한 함수에서 값이 나올 수 있을 경우, 답을 도출합니다.
    if ans_string:
        answer = ans_string

    # K 만큼 진행한 이후에 답이 없다면, impossible을 answer에 넣어줍니다.
    else:
        answer = 'impossible'

    # answer를 반환합니다.
    return answer