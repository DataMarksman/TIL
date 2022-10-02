# BOJ.
# 설계 의도:
# [파기] [0]*(math.ceil(10000/T)) 로 만들어서 최적화 하자 -> 중간에라도 운송 가능하면 해야함. 파기.
# [파기] 
# 1.
# 개선점:
import sys
import math
input = sys.stdin.readline


N, M, T = map(int, input().split())
zero_list = [0]*(math.ceil(10000/T))
one_list = [0]*(math.ceil(10000/T))
for put_in in range(N):
    line = list(map(int, input().split()))
    if line[0] == 0:
        zero_list[math.ceil(line[2]/T)] += line[1]
    else:
        one_list[math.ceil(line[2]/T)] += line[1]
