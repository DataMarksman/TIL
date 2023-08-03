# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:


import sys
from math import *
input = lambda: sys.stdin.readline().rstrip('\r\n')

# 세그먼트 트리에서 값 변경 함수
def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    if start == end:
        seg_tree[node] = diff
        return
    else:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)
        seg_tree[node] = seg_tree[node*2] + seg_tree[node*2+1]
        return

def query(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return seg_tree[node]
    return query(node*2, start, (start+end)//2, left, right) + \
        query(node*2+1, (start+end)//2+1, end, left, right)


# 세그먼트 트리 작성
def init(node, start, end):
    if start == end:
        seg_tree[node] = tree[start]
        return seg_tree[node]
    else:
        seg_tree[node] = init(node*2, start, (start+end)//2) +\
                         init(node*2+1, (start+end)//2+1, end)
        return seg_tree[node]


# 입력
N, M, T = map(int, input().split())
h = int(ceil(log2(N)))
tree_size = 1 << (h+1)
tree = [0]*tree_size
seg_tree = [0]*tree_size

for get_data in range(1, N+1):
    alpha = int(input())
    tree[get_data] = alpha
    seg_tree[get_data] = alpha

init(1, 1, N)

for start_query in range(M+T):
    query_type, start, end = map(int, input().split())
    if query_type == 1:
        update(1, 1, N, start, end)
    else:
        print(query(1, 1, N, start, end))
