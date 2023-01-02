# 먼 거리에서부터 회수, 배달 같이 하자. 어짜피 가면서 배달 -> 수거 하나 수거 -> 배달하나 순서만 다를 뿐이다.
# 효율화 목적으로 idx 기입해주자. 해당 부분에 배달 or 수거 할 것이 남았으면 거기서 부터다.
# 물론 더 먼곳을 기준으로 x2 해주는 것이 각 루틴에서 더해줄 distance의 값이다.

# [해결] 현재 버전: 테스트 2번 실패: 0.01ms/ 10.2MB. 순수하게 로직 에러인듯 함
# 처음 제한 사항에서 모든 집이 최소한 1개의 수량을 가지고 있다는 조건이 없으므로,
# n을 처음 값으로 주면 안되었던 것임

def solution(cap, n, deliveries, pickups):
    del_idx = 0
    col_idx = 0
    deliveries = [0] + deliveries[:]
    pickups = [0] + pickups[:]
    for first_check in range(n, -1, -1):
        if deliveries[first_check] > 0 and not del_idx:
            del_idx = int(first_check)
        if pickups[first_check] > 0 and not col_idx:
            col_idx = int(first_check)
    answer = 0
    while True:
        capa_del = int(cap)
        capa_col = int(cap)
        if max(del_idx, col_idx) == 0:
            break
        else:
            answer += int(max(del_idx, col_idx))*2
            for deli in range(del_idx, -1, -1):
                if deli == 0:
                    del_idx = 0

                elif deliveries[deli] > 0:
                    if deliveries[deli] <= capa_del:
                        capa_del -= deliveries[deli]
                        deliveries[deli] = 0
                    else:
                        deliveries[deli] -= capa_del
                        del_idx = int(deli)
                        break


            for col in range(col_idx, -1, -1):
                if col == 0:
                    col_idx = 0

                elif pickups[col]:
                    if pickups[col] <= capa_col:
                        capa_col -= pickups[col]
                        pickups[col] = 0
                    else:
                        pickups[col] -= capa_col
                        col_idx = int(col)
                        break
    return answer


print(solution(2, 5, [2,0,0,0,0], [0,0,1,0,0]))
