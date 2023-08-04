# BOJ.14696 딱지 놀이
# 설계 의도: 간략 코딩
# 개선점: 재귀함수, return 빼먹지 말자!
def game(x):
    if x <= 0:
        return 'D'
    if cnt_list[0][x] == cnt_list[1][x]:
        return game(x-1)
    return 'A' if cnt_list[0][x] > cnt_list[1][x] else 'B'


for case_num in range(1, int(input())+1):
    cnt_list = [[0]*5 for _ in range(2)]
    for AB in range(2):
        for num in list(map(int, input().split()))[1:]:
            cnt_list[AB][num] += 1
    print(game(4))
