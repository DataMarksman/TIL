# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
from collections import defaultdict, deque


graph = defaultdict(list)
reGraph = defaultdict(list)
dfsNum = [0] * 2501
sccNum = [0] * 2501
finished = [False] * 2501
inDegree = [0] * 2501
cost = [0] * 2501
stack = []
queue = deque()
dfsCnt = 0
sccCnt = 0
edgeCnt = 0
hashMap = defaultdict()


N = int(input())
for site_data in range(N):
    site_name, link_cnt, *links = input().split()
    # 자료 받기 디버깅용
    # print("case ", sites)
    # print(site_name, link_cnt)
    # print(links)

    for sites in links:
        graph[]




target_site = input()
# print("target: ", target_site)

"""
4
A 2 B C
C 1 D
D 1 A
E 2 C D
C
"""