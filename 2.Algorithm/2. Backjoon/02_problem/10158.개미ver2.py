# BOJ.10158 개미
# 설계 의도:
# 1. 그냥 계산 문제.
#    시작점에 t 더해주고 각각 W,H 로 나눈 (//)몫으로 + - 정하고 (%)나머지 출력하면 끝
# 개선점:
# 1. 변수 N개 (N>1)를 받을 때, int 로 받되, map 처럼 휘발성 없게 받으려면?

W, H = map(int, input().split())
wide = int(W)
height = int(H)

p, q = map(int, input().split())
now_idx = [int(p), int(q)]
t = int(input())

now_idx[0] = (now_idx[0]+t) % wide if ((now_idx[0]+t) // wide) % 2 == 0 else wide - ((now_idx[0]+t) % wide)
now_idx[1] = (now_idx[1]+t) % height if ((now_idx[1]+t) // height) % 2 == 0 else height - ((now_idx[1]+t) % height)
print(*now_idx)