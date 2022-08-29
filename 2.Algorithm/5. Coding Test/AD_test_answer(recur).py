# 1. 전기자동차 충전소
# 설계 의도:
# 0.
# 1. 맨하탄 거리 기준으로 충전소를 설치함.
#    이 때 고려해야 할 부분은 최대 2개라는 점.
#   우선적으로 1개로 고려해야하므로, 첫루트는 1개 완전 탐색
# 2. 1개로 완전 탐색이 불가능할 경우,
#    set에 차이의 합을 저장하는 순열 조합으로 간다.


def locating(location, check_set, dist_sum):
    global first_check
    px = location[0]
    py = location[1]
    for checking in range(N):
        dist = abs(px - houses[checking][0]) + abs(py - houses[checking][1])
        if dist <= houses[checking][2]:
            check_set.add(int(checking))
            dist_sum += dist
    if len(check_set) == N:
        first_check.append(dist_sum)
    elif len(check_set) >= 1:
        location_list.append([location, check_set, dist_sum])


T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    houses = [list(map(int, input().split())) for _ in range(N)]
    board = [[set()]*31 for dk in range(31)]
    ans = -1
    for put_in in range(N):
        houses[put_in][0] += 15
        houses[put_in][1] += 15
    first_check = []
    location_list = []

    for x in range(32):
        for y in range(32):
            locating([x, y], set(), 0)
    if first_check:
        ans = min(first_check)
    else:
        second_check = set()
        for i in range(len(location_list)):
            for j in range(len(location_list)):
                if i < j:
                    if len(location_list[i][1] | location_list[j][1]) == N and \
                            not location_list[i][1] & location_list[j][1]:
                        distance = location_list[i][2] + location_list[j][2]
                        # if location_list[i][1] & location_list[j][1]:
                        #     set_check = location_list[i][1] | location_list[j][1]
                        #     for re_poping in range(len(set_check)):
                        #         re_pop = set_check.pop()
                        #         A_d = abs(location_list[i][0][0] - houses[re_pop][0]) + \
                        #               abs(location_list[i][0][1] - houses[re_pop][1])
                        #         B_d = abs(location_list[j][0][0] - houses[re_pop][0]) + \
                        #               abs(location_list[j][0][1] - houses[re_pop][1])
                        #         dist -= A_d if A_d >= B_d else B_d
                        second_check.add(distance)
        if second_check:
            second_check.discard('0')
            ans = min(second_check)

    print(f'#{case_num} {ans}')







