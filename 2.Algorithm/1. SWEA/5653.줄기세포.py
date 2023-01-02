# SWEA. 5653. 줄기세포
# 설계 목적: SET 10개 만들지 뭐 까이꺼 쉬부레
# 1. 이미 밟은건 visited에 넣고 다시 안밟음
# 2. 활성화 되어 살아있는건 그냥 카운팅 리스트로 만들고 .pop(0)로 시간 가는걸 구현하자.
# 3. 그리고 마지막에 카운팅 리스트 스톡에 남아있는거 + 비활성화 된 아해들 합치면 답
# 개선점:
# 1. 현재 속도 682ms 더 빠르게 가능할까? 최적화 진행중

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for case_num in range(1, T + 1):
    N, M, K = map(int, input().split())
    cell_set = [set() for _ in range(11)]        # 미생물 생명력이 1~10 이므로 만들어준다.
    visited = set()                              # 이미 밟았던 좌표를 넣어주는 용도
    for put_in in range(N):
        line = list(map(int, input().split()))
        for first in range(M):
            if line[first] > 0:
                cell_set[line[first]].add((put_in, first))   # 미생물 생명력 별로 넣어줌
                visited.add((put_in, first))                 # 일단 있으니까 밟았다 판정

    time_table = [0]*(K + 11)                     # K 시간 지났을때 생명력 10 들어올 때 생각해서 + 11
    for time in range(1, K+1):                    # K 시간까지 진행해야죵

        # 같은 시간대에서 생명력 높은 쪽이 우선 된다? 그러면 생명력 높은 거부터 넣겠슴다
        for multiple in range(10, 0, -1):

            # 해당 생명력을 가진 아해들이 있니? + 해당 미생물들이 활동할 시간이니? 판단
            if cell_set[multiple] and time % (multiple+1) == 0:
                temp_cell = set()                      # 임시 셋 만들기
                while cell_set[multiple]:              # 현재 미생물 set 가져오기
                    pick = cell_set[multiple].pop()    # 하나씩 빼서 델타 탐색
                    time_table[multiple-1] += 1        # 활성화 되었으니, 시간 테이블에 넣기
                    X = pick[0]
                    Y = pick[1]
                    for direction in range(4):
                        PX = X + dx[direction]
                        PY = Y + dy[direction]
                        if (PX, PY) not in visited:
                            temp_cell.add((PX, PY))
                            visited.add((PX, PY))
                cell_set[multiple] = set(temp_cell)
        time_table.pop(0)               # 시간이 1 갈 때마다 미생물 리스트 pop(0)해서 지워준다.
    ans = sum(time_table)               # 아직 생존한 활성화 미생물 개수로 시작
    for answer in range(1, 11):         # 각 비활성화 된 미생물들 합계 넣어주면 끝
        ans += len(cell_set[answer])
    print(f'#{case_num} {ans}')