# 5648. 원자 소멸 시뮬레이션
# 쉽게 생각하자. 이전에 코드 짜놨던거 다 날아가서 약간 빡친 상태로 작성 시작
# 예전에는 굉장히 어렵게 어렵게 풀었는데, 지금은 오히려 이렇게 쉬운 문제를? 이라고 생각하며 풀었다.

# 이전 설계:
# 1. 이전 좌표들의 셋과 이번 시행 좌표들의 셋 개수가 다르면? 중복되는 좌표에 있는걸 터뜨리자.
# 2. 2차원 배열로 놓고 자기가 진행하는 반대 방향에서 오는 것들을 0.5턴에 찍어내서 죽이자.
# 저장 형식 예시: dict_A = ({'rocation': (500,100),'move':1,'energy':10},{'rocation': (500,100),'move':0,'energy':10})

# 이번 설계:
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
        removed_list = atom_list[::]
        rm_count = 0
        for explosion in range(len(atom_list)):
            if atom_list[explosion][3] == 0:
                del removed_list[explosion-rm_count]
                rm_count += 1
        atom_list = removed_list[::]
    print(f'#{case_num} {sum_power}')
