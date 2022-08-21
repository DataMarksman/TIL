# 1267. 작업 순서
# 설계 의도: 이 문제는 조건부 BFS 문제다.
# 0. 처음에는 역으로 가는 것을 생각했으나, 정방향으로 가면서 카운트를 모으고, 스택을 쌓아서 조건에 맞으면 진입하는 것으로 바꾸었다.
# 1. 받은 값들 중에, 해당 정점으로 가는 길이 없는 정점은, 최상단 시작점,
#   받은 값들 중에, 해당 정점에서 시작하는 길이 없는 정점은, 최하단 끝점.
#   즉, 최상단 시작점 부터 시작하고, 각 정점을 갈 때에는 해당 정점으로 갈 수 있는 모든 길을 다 밟은 다음에 갈 수 있다.
# 2. 그러므로, 일단 stack 에 V개의 숫자를 다 넣어놓고 길의 목적지를 보드에 기입 + stack 에서도 제외
#   for 문을 돌릴 때, 목적지에 해당하는 좌표를 카운팅 리스트에서 += 1 해줌 (해당 정점으로 가는 길을 다 갔는지 체크)
#   for 문 돌릴 때, 해당 좌표 값이 1이라면 기본적으로 해당 좌표의 카운트를 -= 1하여,
#   기존의 카운트가 0이 될 대, 스택에 넣는다. (거기로 가는 길 전부 다 밟았니?)
# 3. 이렇게 되면, (original 최하단)현 최상단 좌표들부터 스택에 넣고
#   조건을 만족한 정점들이 순차적으로 스택에 추가된다.
#   이를 앞에서부터 하나씩 뽑아가면서 지나간 정점의 수가 전체 정점의 수와 동일해질 때 까지 반복한다.
#

def work_up(check, k):                                               # (제가 이 정점을 들렸었나요?, 이번 시작점은 k 부터예요~)
    global ans_list
    if len(ans_list) >= V:                                           # 반환할 조건은, 지나간 좌표 개수가 V에 도달했을 때
        return print(f'#{case_num}', *ans_list)                      # 아예 함수 내에서 프린트 해버리기~

    else:                                                            #
        for i in range(1, V+1):                                      # 밟을 좌표를 그냥 정점과 일치 시켜버림
            if board[k][i] == 1:                                     # 이 시작점에서 갈 수 있는 모든 도착점 에서
                num_count[i] -= 1                                    # 해당 좌표의 카운트를 -= 1하기
                if i not in check and num_count[i] == 0 and i not in stack:
                    stack.append(i)                                  # 해당 좌표 밟을 수 있는 조건 전부 충족시 스택에 넣기
        # print(k,stack, check, ans_list)                            #
        if len(stack) >= 1:                                          # 스택 길이가 1 이상일 때만 시행 (이 문제는 괜찮음)
            k = stack.pop(0)                                         # 가장 앞에서 하나 뽑아서
            check.append(k)                                          # k 정점 지나갔었다고 체크 해주고
            ans_list.append(k)                                       # 밟은 목록에도 추가하기
            # print(k, check, ans_list)                              #
            return work_up(check, k)                                 # 밟은 곳 추가하고 스택에서 뽑은 좌표로 다음 재귀 시작

for case_num in range(1, 11):                                        #
    V, E = map(int, input().split())                                 #
    num_list = list(map(int, input().split()))                       #
    num_count = [0]*(V+1)                                            # 정점으로 가는 모든 길을 밟아야 진입 가능하므로 조건 체크용
    board = [[0]*(V+1) for j in range(V+1)]                          # 0 제외하고 V개 만큼 주려고 + 1 해줌
    stack = [t for t in range(1, V+1)]                               #
    for put_in in range(E):                                          #
        board[num_list[2*put_in]][num_list[2*put_in + 1]] = 1        # VxV (0 제외) 보드 에서 시작점 -> 도착점 정보 반영
        num_count[num_list[2*put_in + 1]] += 1                       # 해당 정점으로 가는 길 카운팅해서 반영
        if num_list[2 * put_in + 1] in stack:                        # 1부터 V까지 만들어놓은 리스트에서 도착점으로 나온 것 제외
            stack.remove(num_list[2 * put_in + 1])                   # 그쪽으로 가는 길이 없다? -> 최상위 시작점.
    # print(stack)
    start = stack.pop(0)                                             # 처음 시작점 후보 중에 하나 뽑아서
    ans_list = [start]                                               # 이미 밟은 곳 저장하는 리스트에다가도 넣고
    work_up([start], start)                                          # 정점 visited 체크용 리스트에다가도 넣은 다음 재귀 시작