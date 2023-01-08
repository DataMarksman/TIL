# PRG.
# https://school.programmers.co.kr/learn/courses/30/lessons/67258
# 설계 의도: 앞에서부터 딱 한 번씩만 체크해서 최적의 답을 보자구요!

# 로직의 Main 개념: semi DP

# 개선점:

# 각 값이 등장할때마다 해당 값의 좌표를 경신 시켜줍니다.
# 각 보석이 등장하는 위치 값의 min 값과 max 값을 빼준 값이 가장 작은 위치를 반환합니다.
# 앞에서부터 딱 한번 탐색하면 도출 가능하게 했습니다.

# 탐색 로직:
# 각 보석이 전부 등장했을 경우, 해당 최소, 최대 위치를 계속 갱신 시켜주면 됩니다.
# 특정 보석이 최소 idx를 가지고 있을 경우 그 보석이 다른 보석의 집합에서 가장 먼 거리에 있음을 의미합니다.
# 그러므로, 해당 보석을 다시 뽑았을 때, 해당 idx를 최대 idx로 갱신 시켜주면 해당 위치에서의 최소 길이를 도출 가능합니다.


def solution(gems):
    length = len(gems)                                  # 보석의 총 길이를 변수에 넣어줍니다.
    min_length = int(length)                            # 계속 경신 시켜줄 answer 판단용 최소 길이 값 입니다.
    answer = [1, length]                                # answer로 반환 시킬, [시작 idx, 끝 idx] 의 초기값 입니다.
    check_set = set(gems)                               # 보석의 종류가 몇 개인지 확인하기 위해 set을 사용합니다.
    count_length = len(check_set)

    if length == count_length:                          # 빠르게 특정 케이스를 토스해주기 위한 로직입니다.
        return answer                                   # 전체 보석들이 한번 씩만 등장한다면, 바로 answer를 반환합니다.
    elif count_length == 1:                             # 한 종류의 보석으로만 구성되어있을 경우,
        return [1, 1]                                   # 바로 [1, 1]에서 완결이 나므로 반환합니다.

    check_dict = {}                                     # 각 스트링의 값마다 특정한 id를 배정해줍니다.
    idx = 0                                             # 이는 나중에 idx로 활용됩니다.
    for gem in check_set:                               # 보석의 종류 별로 idx를 0부터 하나씩 배정해줍니다.
        check_dict[gem] = idx
        idx += 1

    pointers = [length-1]*count_length                  # 각 보석별 인덱스를 넣어줄 리스트 입니다. 기본값 = 최대값
    max_idx = length-1                                  # 초기 최대 idx 값은 최후미의 값을 배정합니다.
    min_idx = 0                                         # 초기 최소 idx 값은 0을 배정합니다.

    visited = set()                                     # 효율화 용 visited 입니다. 모든 보석이 한번씩 등장해야 길이를 측정 시작합니다.
    count_flag = False                                  # 보석이 한번씩 다 나왔을 때부터 로직에 들어갈 flag 변수입니다.

    for top in range(length):                           # 보석을 한번씩 확인하는 반복문입니다. O(N) 만큼의 연산이 소요됩니다.
        if not count_flag:                              # 아직 모든 보석들이 한번씩 나오지 않았다면
            if gems[top] not in visited:                # 등장한 보석이 등장한 적 있는지 확인하고
                visited.add(gems[top])                  # 없었다면 visited에 넣어줍니다.
                if len(visited) == count_length:        # 만약 보석들이 한번씩 다 등장했다면,
                    count_flag = True                   # Flag를 활성화 시키고 로직에 진입합니다.

        picked_gem = check_dict[gems[top]]              # 각 보석을 뽑을 때마다 적어주기 편하게 하기 위해 변수에 배정해줍니다.
        picked_gem_idx = pointers[picked_gem]           # 안해도 되지만, 가독성을 위해 변수로 할당해줍니다.

        pointers[picked_gem] = top                      # 현재 뽑은 위치로 보석의 위치를 갱신 시켜줍니다.

        if picked_gem_idx == max_idx:                   # 뽑은 보석의 이전 위치가 max_idx, 즉 최대값과 일치했다면
            if count_flag:                              # flag가 True 일때 로직에 진입합니다.
                max_idx = top                           # 최대값은 현재 위치가 됩니다.
                min_idx = min(pointers)                 # 최소값은 갱신 되었을 수 있으므로 min으로 한번 확인해줍니다.
                current_length = max_idx - min_idx      # 현재 진열장의 길이를 계산해줍니다.
                if current_length < min_length:         # 현재의 진열장 거리가 최소값보다 작다면,
                    min_length = current_length         # 최솟값과 answer 을 갱신해줍니다.
                    answer = [min(pointers) + 1, max(pointers) + 1]

        elif picked_gem_idx == min_idx:                 # 뽑은 보석의 이전 위치가 max_idx, 즉 최소값과 일치했다면
            if count_flag:                              # 로직에 진입합니다.
                max_idx = top                           # 세부 로직은 위와 일치합니다.
                min_idx = min(pointers)
                current_length = max_idx - min_idx
                if current_length < min_length:
                    min_length = current_length
                    answer = [min(pointers) + 1, max(pointers) + 1]

    return answer

print(solution(["AA", "AB", "AC", "AA", "AC"]))