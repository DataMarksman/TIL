# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())
num_list = list(map(int, input().split()))
seg_plus = [0 for _ in range(4*N)]
seg_cross = [0 for _ in range(4*N)]
answer = 0
def plus(seg_plus, node, left, right):
    global answer
    if left == right:
        seg_plus[node] = num_list[left]
        return seg_plus[node]
    mid = left + (right - left)//2
    left = plus(seg_plus, 2*node, left, mid)
    right = plus(seg_plus, 2*node + 1, mid + 1, right)
    seg_plus[node] = right + left
    return seg_plus[node]


def cross(seg_cross, node, left, right):
    global answer
    if left == right:
        seg_cross[node] = num_list[left]
        return seg_cross[node]
    mid = left + (right - left)//2
    left = cross(seg_cross, 2*node, left, mid)
    right = cross(seg_cross, 2*node + 1, mid + 1, right)
    seg_cross[node] = right * left
    return seg_cross[node]

plus(seg_plus, 1, 0, N-1)
cross(seg_cross, 1, 0, N-1)

# def query(start, end, node, left, right, flag):
#     if end < left or start > right:
#         if flag:
#             return 1
#         else:
#             return 0
#
#     if start <= left and right <= end:
#         if flag:
#             return seg_cross[node]
#         else:
#             return seg_plus[node]
#
#     mid = left + (right - left)//2
#     left = query(start, end, 2 * node, left, mid, flag)
#     right = query(start, end, 2 * node + 1, mid + 1, right, flag)
#     if flag:
#         return left * right
#     else:
#         return left + right

def query_plus(node, left, right, start, end):
    if start > end or start > right or end < left:
        return 0
    if start <= left and right <= end:
        return seg_plus[node]
    mid = left + (right - left) // 2
    return query_plus(2 * node, left, mid, start, end) + query_plus(2 * node + 1, mid + 1, right, start, end)


def query_cross(node, left, right, start, end):
    if start > end or start > right or end < left:
        return 1
    if start <= left and right <= end:
        return seg_cross[node]
    mid = left + (right - left) // 2
    return query_cross(2 * node, left, mid, start, end) * query_cross(2 * node + 1, mid + 1, right, start, end)


for x in range(N-1):
    for y in range(x+1, N):
        if query_plus(1, 0, N-1, x, y) == query_cross(1, 0, N-1, x, y):
            answer += 1
print(answer+N)