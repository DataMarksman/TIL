# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
from math import *
input = lambda: sys.stdin.readline().rstrip('\r\n')


# 구간 최소값 쿼리 처리 함수
def query(node, start, end, left, right, flag):
    if flag:
        if left > end or right < start:
            return 1
        if left <= start and end <= right:
            return max_seg_tree[node]
        return max(query(node*2, start, (start+end)//2, left, right, flag),
                    query(node*2+1, (start+end)//2+1, end, left, right, flag))
    else:
        if left > end or right < start:
            return 1000000000
        if left <= start and end <= right:
            return min_seg_tree[node]
        return min(query(node * 2, start, (start + end) // 2, left, right, flag),
                   query(node * 2 + 1, (start + end) // 2 + 1, end, left, right, flag))


# 세그먼트 트리 작성
def init(node, start, end, flag):
    if flag:
        if start == end:
            max_seg_tree[node] = tree[start]
            return max_seg_tree[node]
        else:
            max_seg_tree[node] = max(init(node*2, start, (start+end)//2, flag),
                            init(node*2+1, (start+end)//2+1, end, flag))
            return max_seg_tree[node]
    else:
        if start == end:
            min_seg_tree[node] = tree[start]
            return min_seg_tree[node]
        else:
            min_seg_tree[node] = min(init(node*2, start, (start+end)//2, flag),
                            init(node*2+1, (start+end)//2+1, end, flag))
            return min_seg_tree[node]


# 입력
N, M = map(int, input().split())
h = int(ceil(log2(N)))
tree_size = 1 << (h+1)
tree = [0]*tree_size
min_seg_tree = [0]*tree_size
max_seg_tree = [0]*tree_size

for get_data in range(1, N+1):
    alpha = int(input())
    tree[get_data] = alpha
    min_seg_tree[get_data] = alpha
    max_seg_tree[get_data] = alpha
else:
    init(1, 1, N, 1)
    init(1, 1, N, 0)

for start_query in range(M):
    start, end = map(int, input().split())
    min_answer, max_answer = query(1, 1, N, start, end, 0), query(1, 1, N, start, end, 1)
    print(min_answer, max_answer)
