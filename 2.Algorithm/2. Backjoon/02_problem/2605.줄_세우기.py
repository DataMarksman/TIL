# 2605 줄 세우기

N = int(input())                              # 사람 수를 받아서
list_pick = list(map(int, input().split()))   # 배치할 리스트를 받습니다.
ans_list = []                                 # 줄 세울 리스트를 도출하구요
for line in range(N):                         # 줄을 세워봅시다.
    ans_list.insert(list_pick[line], line+1)  # 해당 리스트 좌표에 끼워넣으면 됩니다.
print(*ans_list[::-1])                        # 이건 뽑은 것만큼 '앞으로' 가는거라 역순 출력
