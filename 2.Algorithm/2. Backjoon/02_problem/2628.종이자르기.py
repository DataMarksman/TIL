# 2628 종이자르기
C, R = map(int, input().split())                         # 종이의 크기를 받습니다.
C = int(C)
R = int(R)

N = int(input())                                          # N개를 받아
cutting_list = [list(map(int, input().split())) for _ in range(N)]
# cutting_list = [[0, 3], [1, 4], [0, 2]]                 # 잘라줄 위치 좌표를 저장

ans_list = [[0], [0]]                                     # 0부터 입력 시작
for cut_point in range(len(cutting_list)):                # 각 자를 위치를 입력
    if cutting_list[cut_point][0] == 0:                   # 가로 세로 구분해서 저장
        ans_list[0].append(cutting_list[cut_point][1])
    elif cutting_list[cut_point][0] == 1:
        ans_list[1].append(cutting_list[cut_point][1])
ans_list[0].append(R)                                     # 최대 크기도 입력
ans_list[1].append(C)
ans_list[0] = sorted(ans_list[0])                         # 정렬해주기
ans_list[1] = sorted(ans_list[1])
# ans_list = [[0, 2, 3, 8], [0, 4, 10]]

area_list = []
for dx in range(1, len(ans_list[0])):                     # 박스 x 좌표 별 반복문
    for dy in range(1, len(ans_list[1])):                 # 박스 y 좌표 별 반복분
        area_list += [(ans_list[0][dx]-ans_list[0][dx-1])*(ans_list[1][dy]-ans_list[1][dy-1])]
			# area_list에 각각의 넓이 저장하기.
# area_list = [8, 12, 4, 6, 20, 30]
ans = max(area_list)                                      # 가장 큰 값 도출
print(ans)