# 4831. 전기버스
# 문제 설계: 재귀함수로 드라이빙 하자

def driving(current_position, drive_count):             # driving 함수를 정의합니다.
    for find in range(fuel, 0, -1):                     # 한번에 이동 가능한 영역을 범위로, 멀리서부터 탐색.
        if int(current_position + find) >= int(goal):   # 만약 지금 위치에서 충전없이 한번에 골이면 
            return print(f'#{case_num} {drive_count}')  # return print로 답 도출
        elif station_list[current_position + find] == 1:# 아니라면, 앞선 범위에서 1을 찾기(충전소 = 1)
            current_position += find                    # 범위 내 가장 멀리 있는 충전소를 찾았으면,
            drive_count += 1                            # 이동 후, 현재 위치 수정 및 충전 횟수 +1
            return driving(current_position,drive_count)# 재귀
    return print(f'#{case_num} 0')                      # for문 다 돌아갔는데 return 안났으면,
                                                        # 범위 내에 충전소가 없다는 것이므로, 사고난것.


T = int(input())
for case_num in range(1, T + 1):
    K, N, M = map(int, input().split())
    fuel = K                                            # 알아보기 쉽게 변수명 변경 
    goal = N
    station_count = M
    station_list = [0] * (goal + fuel)                  # 당초 N의 길이와 거기에서 K 만큼의 길이까지 더함
    charger_list = list(map(int, input().split()))      # 충전기의 위치 데이터를 받아서
    for charger in charger_list:                        # 이 데이터를 좌표 삼아 station_list에 저장
        station_list[charger] += 1                      # Station 리스트는, 충전소가 있는 곳에 1을 배치함.
    driving(0, 0)                                       # 현재 위치 0, 충전횟수 0회로 driving 함수를 개시
