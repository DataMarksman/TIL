# SWEA. 14559. 배수 그래프
# 설계 목적: set() 연산으로 Q 서칭 시간을 단축한 BFS
# 사용 개념: BFS / Q -> set()으로 구현 / 백트래킹(visited) / set()연산: 교집합, 합집합 / input 최적화(M**2 -> (M**2)/2)
# 0. 이전까지 했던거 일단 킵하고, 갈수 있는 정점들 끼리의 2차 배열을 만들자.
# 1. <요약> : 이 문제의 조건들은 아래와 같다.
#   가. 출발하는 정점의 끝 수와 진입하려는 정점의 시작 수의 최소 공배수가 N의 범위 안에 있어야 이어진다.
#   나. 궁극적인 시작점과 끝점의 경우 배가 하는것이 불가능하므로, 각각 시작점의 수와 끝점의 수로 나눠질 때만 진입 가능하다.
#       tip: 헷갈리기 쉬운게,
#           일반 정점 두개를 이어주는 끝점: 17 -> 시작점 2 / N 36 이면, 34로 만날 수 있지만,
#           일반 정점 끝점 17 -> 궁극의 끝점이 2 / N 36 이면, 둘은 만날 수가 없다.

# 2. 도착점으로 갈 수 있는 경로의 집합들을 구하고
# 3. (커팅1) 앞에서부터 나올 수 있는 모든 경로들을 set에 저장해서 뒤의 집합과 교집합 구하기
# 4. (백트1) n차 시도에서 실패시, 전열의 집합 내 모든 정점에서 갈 수 있는 정점을 다시 뽑아내고 돌리기
#   -> 이 때, 전열에서 갈 수 있는 정점을 다 뽑아낸 뒤에, 이전 정점들을 visited set에 저장.
#   -> 즉, 해당 정점을 밟고 2턴 뒤부터는 그 정점을 쓸 수 없게 된다.

# 개선점:
# 1. 현재는 한질의 set을 제작하기 위해서 2차원 배열을 현재의 compare_set의 요소 개수만큼 탐색하고 있다.
#    -> 이를, 현재 좌표를 기입하면 바로 거기에서 이어지는 좌표들을 반환하는 dict의 방식으로 전환하면 빨라지지 않을까?
#
# 2. 가능한 최적화 한 것 같지만, 분명 시간을 많이 잡아먹는 부분이 있을 것이다.
#    의심가는 부분:
#        i) M이 미친듯이 많다 (백트 조건을 추가로 줘야하나?)
#        ii) 각 간선들의 시작 조건과 끝 조건의 수가 너무 커서 LCM 재귀가 오래 걸린다. (이건 해결 불가능)
#        iii) 일부러 문제를 꼬아놔서 더미 루트들이 많다. (커팅할 방법을 고안해야한다.)
#    -> 요는 i과 iii에서 말하는 M의 탐색 범위를 좁히는 방법을 고안해볼 필요가 있음.

# < 최소 공배수 함수 >
def lcm(a, b):
    multiple = a * b                                               # 일단 a*b를 빼놓지 않으면 나중에 사라진다. 미리 빼놓자.
    while b > 0:                                                   # 이하는 최대 공약수를 구하는 식이다.
        a, b = b, a % b                                            # 유클리드 호제법을 사용했다.
    return multiple / a                                            # a*b의 곱에서 최대 공약수를 나눠주면 최소 공배수이다.


# < 데이터 받기 & 구조화 >
T = int(input())
for case_num in range(1, T+1):
    N, S, E = map(int, input().split())
    N = int(N)                                                     # N은 각 숫자들이 갈 수 있는 최대값이다.
    start = int(S)                                                 # start는 궁극의 첫 시작점이다. 이 정점에서 시작한다.
    end = int(E)                                                   # end는 궁극의 끝점이다. 이 정점에서 끝난다.

    M = int(input())                                               # 궁극의 정점을 제외한 일반 정점의 개수이다.
    board = [[0]*(M+1) for _ in range(M+1)]                        # visited를 찍기 위한 2차 배열이다.

    first_set = set()                                              # 이후 while 비교문을 위한 첫 set
    last_set = set()                                               # 이후 while 비교문을 위한 마지막 set
    multi_list = []                                                # 각 정점의 시작점과 끝점 데이터를 저장할 리스트

    for write_in in range(M):                                      # 값을 받음과 동시에 위의 첫/마지막 set, 정점 리스트 기입
        multiple_factor = list(map(int, input().split()))          # 값을 리스트로 받고, 일단 factor에 저장
        r = multiple_factor[0]                                     # 이번에 입력 받은 정점의 시작점이다.
        c = multiple_factor[1]                                     # 이번에 입력 받은 정점의 끝점이다.

        if start % r == 0:                                         # 이번 정점의 시작점이 궁극의 시작점과 이어지는가?
            first_set.add(write_in)                                # first set에도 입력하자.
        if end % c == 0:                                           # 이번 정점의 시작점이 궁극의 끝점과 이어지는가?)
            last_set.add(write_in)                                 # last set에도 입력하자.

        for comp_multi in range(len(multi_list)):                  # 이미 입력된 정점의 데이터와 현재 입력된 정점을 비교하여 기입
            # 각 정점과 비교하여, 해당 정점의 시작점과 지금 입력한 정점의 끝점의 최소공배수가 N의 범위 안에 있나요?
            if N >= lcm(c, multi_list[comp_multi][0]):
                board[write_in][comp_multi] = 1                    # 맞으면 두 정점이 이어지는 것이므로 체크.
            # 각 정점과 비교하여, 해당 정점의 끝점과 지금 입력한 정점의 시작점의 최소공배수가 N의 범위 안에 있나요?
            if N >= lcm(r, multi_list[comp_multi][1]):
                board[comp_multi][write_in] = 1                    # 맞으면 체크
        multi_list.append(multiple_factor)                         # 비교 끝났으면 이번 정점도 리스트에 기입

    n = 0                                                          # 깊이 = 0 부터 시작
    compare_set = set(first_set)                                   # 궁극의 시작점에서 갈 수 있는 좌표들(first set)을 먼저 배정
    visited = set()                                                # 백트래킹용 visited 제작
    flag = False                                                   # 궁극의 시작점과 끝점이 이어지는지 여부를 체크한 flag

    # < while 반복문: BFS 본체 >
    while compare_set:                                             # -> compare list가 True가 아니면 갈 곳이 없다.
        stock_set = set()                                          # 임시 저장용 스톡 set을 초기화
        n += 1                                                     # 깊이 += 1

        if compare_set & last_set:                                 # 비교하는 set에 궁극의 끝 정점으로 이어지는 요소들이 있나요?
            flag = True                                            # 있으면 flag = True 반환. 사이의 거리는 n, 즉 현재 깊이
            break                                                  # while 문 정지
        else:                                                      # 연결되는 정점 없어?
            visited = visited | compare_set                        # 지금 비교 set은 방문 목록에 넣고
            while compare_set:                                     #
                pick = compare_set.pop()                           # 현재 비교 set에서 요소 하나씩 꺼내서
                for setting in range(M):                           # 각 요소에서 갈 수 있는 정점들을 비교 set(임시)에 저장
                    if board[pick][setting] == 1 and setting not in visited:
                        stock_set.add(setting)
        compare_set = stock_set.copy()                             # 비교 set(임시)의 값을 비교 set에 복사하고 다음 while 진입

    # < 출력 >
    if flag:
        print(f'#{case_num} {n}')                                  # 앞서, 연결된다고 해서 flag 올렸으면 그 길이 출력.
    else:
        print(f'#{case_num} {-1}')                                 # flag 못 올렸으면 -1 출력
