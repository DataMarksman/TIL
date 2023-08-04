# 13300 방 배정
# 100점을 위해 모든 조건을 고려해보자~

N, K = map(int, input().split())                    # 사람수와 방에 들어갈 인원을 받아요!
member_stock = []                                   # 일단 모든 값들을 저장할 공간을 만들어요!
N = int(N)                                          # 사람 수 다시 받고
K = int(K)                                          # 방별 최대 인원 다시 받아요!
for entering in range(N):                           # 사람 수만큼 수련장에 입장하십니다!
    gender, cls_num = map(int, input().split())     # 성별과 학년을 받아서
    member_stock += [[cls_num, gender]]             # 학년과 성별로 순서를 바꿔서 리스트에 저장
# member_stock = [[1, 1], [1, 0], [1, 1], [2, 0], [2, 1], [2, 0] ...

max_class = max(map(max, member_stock))             # 가장 높은 학년을 받아요! (이건 100점을 위함임)
class_count = [[0, 0] for _ in range(max_class+1)]  # 위치좌표의[0] 값 = 학년이 될 수 있도록 가장 높은 학년의 값 +1

for members in member_stock:                        # 이제 저장해둔 맴버 목록을 읽어서
    class_count[members[0]][members[1]] += 1        # 해당 위치좌표에 넣어요. 위치좌표[0] = 학년 / 위치좌표[1]
# class_count = [[0, 0], [1, 2], [2, 1], [1, 3], [0, 1], [1, 2], [1, 1]]
# 정리하면 이 경우에는 첫 [0,0]은 더미. 1학년은 [1, 2] 즉, 여학생이 1명, 남학생이 2명이다.

room_count = 0                                      # 필요한 방의 개수 변수화
for rooming in class_count:                         # 방배정 해주기~
    if rooming[0] != 0 and rooming[0] % K != 0:     # 학년, 성별 별로 죄다 찢어지므로 각 인원 수를 K로 나눈 만큼 몫에
        room_count += (rooming[0]//K) + 1           # 초과하는 분량은 K가 안되더라도 방 1칸 차지하므로 +1을 더해준다.
    elif rooming[0] != 0 and rooming[0] % K == 0:   # 그런데 만약 K로 나눠지는 수일 경우, 딱 들어맞으므로, +1을 안한다.
        room_count += (rooming[0] // K)             #
    if rooming[1] != 0 and rooming[1] % K != 0:     # 남학생도 똑같이 배정~
        room_count += (rooming[1]//K) + 1           #
    elif rooming[1] != 0 and rooming[1] % K == 0:   #
        room_count += (rooming[1] // K)             #
print(room_count)                                   # 출력!
