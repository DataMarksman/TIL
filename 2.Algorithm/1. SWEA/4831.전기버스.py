# 4831. 전기버스


def driving(current_position, drive_count):
    for find in range(K, 0, -1):
        if current_position+find >= N:
            return f'#{case_num} {drive_count}'

        elif station_list[current_position+find] == 1:
            new_po = current_position + find
            new_count = drive_count + 1
            driving(new_po, new_count)
    else:
        return f'#{case_num} 0'


T = int(input())
for case_num in range(1, T + 1):
    K, N, M = input().split()
    print(K, N, M)
    charger_list = list(map(int, input().split()))
    station_list = [0] * (N + K)
    for charger in charger_list:
        station_list[charger] += 1
    cur_po = 0
    drive = 0
    print(driving(cur_po, drive))
