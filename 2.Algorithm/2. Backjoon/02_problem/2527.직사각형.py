# BOJ.2527 직사각형
# 설계 의도:
# 1. 상태를 3단계로 나누어서 가로영역 * 세로영역으로 현 상태를 구함
# 1.1 가로 혹은 세로가 완전히 닿지 않으면 0 반환. 여기에 뭘 곱해도 0이므로, 둘은 접하지 않음
# 1.2 가로 혹은 세로 중에서 일치하는 점이 있으면 1 반환. 여기에 뭘 곱하냐에 따라 상태가 바뀜
# 1.3 가로 혹은 세로 중에서 범위가 겹치는 구간이 있으면 2 반환.
# 1.4 가로, 세로 판정을 곱한 값이
#       0: 완전 분리 / 1: 점 하나 만남 / 2: 선이 접함 / 4: 내부 직사각형 만들어짐
# 개선점: 찾아주세요~

idx_list = [list(map(int, input().split())) for _ in range(4)]
ans = ['d', 'c', 'b', '여기는 비워둘께요', 'a']
for boxes in idx_list:
    judge_xy = [0, 0]
    for xy in range(2):
        if boxes[0+xy] > boxes[6+xy] or boxes[2+xy] < boxes[4+xy]:
            judge_xy[xy] = 0
        elif boxes[0+xy] == boxes[6+xy] or boxes[2+xy] == boxes[4+xy]:
            judge_xy[xy] = 1
        else:
            judge_xy[xy] = 2
    print(ans[judge_xy[0]*judge_xy[1]])
