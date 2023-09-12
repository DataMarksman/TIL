# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
chess_dict = {".":0,
              "K": 0,
              "k": 0,
              "P": 1,
              "p": -1,
              "N": 3,
              "n": -3,
              "B": 3,
              "b": -3,
              "R": 5,
              "r": -5,
              "Q": 9,
              "q": -9
              }

answer = 0
for case in range(8):
    chess_list = input()
    for check in chess_list:
        answer += chess_dict[check]
print(answer)