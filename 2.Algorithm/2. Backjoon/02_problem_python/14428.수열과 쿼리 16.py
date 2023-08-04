# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
from math import *
input = lambda: sys.stdin.readline().rstrip('\r\n')
INF = float('inf')

# 세그먼트 트리 초기화 함수
def init(node, start, end):
    if start == end:
        tree[node] = lst[start]
        return tree[node]
    else:
        tree[node] = min(init(node*2, start, (start+end)//2),
                        init(node*2+1, (start+end)//2+1, end))
        return tree[node]

# 세그먼트 트리에서 값 변경 함수
def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = diff
        return
    else:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)
        tree[node] = min(tree[node*2], tree[node*2+1])
        return

# 구간 최소값 쿼리 처리 함수
def query(node, start, end, left, right):
    if left > end or right < start:
        return INF, 0
    if left <= start and end <= right:
        return tree[node]
    return min(query(node*2, start, (start+end)//2, left, right),
                query(node*2+1, (start+end)//2+1, end, left, right))

# 입력
N = int(input())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())

# 세그먼트 트리 생성
h = int(ceil(log2(N)))
tree_size = 1 << (h+1)
tree = [0]*tree_size

init(1, 0, N-1)

# 쿼리 처리
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 1:
        b = b - 1
        lst[b] = c
        update(1, 0, N-1, b, c)
    elif a == 2:
        print(query(1, 0, N-1, b-1, c-1))
