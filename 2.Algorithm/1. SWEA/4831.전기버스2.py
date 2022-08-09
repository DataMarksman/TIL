# 4831. 전기버스

def driving(current_position, drive_count):
    for find in range(fuel, 0, -1):
        if int(current_position + find) >= int(goal):
            return print(f'#{case_num} {drive_count}')
        elif station_list[current_position + find] == 1:
            current_position += find
            drive_count += 1
            return driving(current_position, drive_count)
    return print(f'#{case_num} 0')


T = int(input())
for case_num in range(1, T + 1):
    K, N, M = map(int, input().split())
    fuel = K
    goal = N
    station_count = M
    station_list = [0] * (goal + fuel)
    charger_list = list(map(int, input().split()))
    for charger in charger_list:
        station_list[charger] += 1
    driving(0, 0)
