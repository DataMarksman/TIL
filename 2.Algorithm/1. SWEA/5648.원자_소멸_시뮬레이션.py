# 5648. 원자 소멸 시뮬레이션

# 1. 그냥 dx dy로 0.5씩 이동시키고, 겹치는거 있으면 일단 점수 부터 받고 한번에 조져.
# 2. 임시 리스트 제작하고, rm_count 쌓아서 지우는게 포인트. 다 지운 후에 본체에 덮어 쓰기.

# 조타용 좌표
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    atom_list = [list(map(int, input().split())) for _ in range(N)]
    turn = 0
    sum_power = 0
    while turn < 4000 and len(atom_list) > 1:
        turn += 1
        for atoms in atom_list:
            atoms[0] += dx[atoms[2]]/2
            atoms[1] += dy[atoms[2]]/2
        atom_list.sort()
        for idx in range(len(atom_list)-1):
            if atom_list[idx][0] == atom_list[idx+1][0] and atom_list[idx][1] == atom_list[idx+1][1]:
                sum_power += atom_list[idx][3] + atom_list[idx+1][3]
                atom_list[idx][3] = 0
                atom_list[idx + 1][3] = 0

        rm_count = 0
        for explosion in range(len(atom_list)):
            if atom_list[explosion-rm_count][3] == 0 or\
                    atom_list[explosion-rm_count][0] > 1000 or atom_list[explosion-rm_count][0] < -1000 or \
                    atom_list[explosion-rm_count][1] > 1000 or atom_list[explosion-rm_count][1] < -1000:
                del atom_list[explosion-rm_count]
                rm_count += 1
    print(f'#{case_num} {sum_power}')