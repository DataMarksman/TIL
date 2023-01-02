# BOJ.15661. 링크와 스타트
# 설계 의도: 반을 보면 뒤의 반은 안봐도 됩니당.
# 1. 원래 홀수/짝수 나눠서, 짝수일 경우에는 N//2 길이의 조합의 경우 visited로 연산 반으로 줄이려고 했는데...
#     -> 이게 시간 두배로 걸린다 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 왜지???????????????
# 개선점:
# 1. 시간이 너어어어어어무 느리다. 조건 분절해서 나누면 시간이 두배가 되는 기적...
#     -> 홀/짝 조건 분절 = 4096ms / 분절 X 깡 계산 = 2104ms ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
import sys
from itertools import combinations
input = sys.stdin.readline


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
num_list = [p for p in range(N)]
num_dict = {}
for x in range(N):
    for y in range(N):
        if x < y:
            num_dict[(x, y)] = int(board[x][y] + board[y][x])

iter_set = set()
for put_in in range((N//2)+1):
    iter_set |= set(combinations(num_list, put_in))
original = set(num_list)
ans = 9999999999999999999
while iter_set:
    temp_A = 0
    temp_B = 0
    pick = set(iter_set.pop())
    anti_pick = original - pick
    temp_list = sorted(pick)
    anti_list = sorted(anti_pick)
    for pick_X in range(len(temp_list)-1):
        for pick_Y in range(pick_X+1, len(temp_list)):
            temp_A += num_dict[(temp_list[pick_X], temp_list[pick_Y])]
    for anti_X in range(len(anti_list)-1):
        for anti_Y in range(anti_X+1, len(anti_list)):
            temp_B += num_dict[(anti_list[anti_X], anti_list[anti_Y])]
    if abs(temp_A - temp_B) < ans:
        ans = abs(temp_A - temp_B)
        if ans == 0:
            break
print(ans)