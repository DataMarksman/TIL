# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:


# A = 65, Z = 90
def preorder(a):
    global pre_ans
    if exist[a]:
        pre_ans += chr(a)
        preorder(left[a])
        preorder(right[a])

def inorder(b):
    global in_ans
    if exist[b]:
        inorder(left[b])
        in_ans += chr(b)
        inorder(right[b])

def postorder(c):
    global post_ans
    if exist[c]:
        postorder(left[c])
        postorder(right[c])
        post_ans += chr(c)


import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
exist = [0] * 100
left = [0] * 100
right = [0] * 100
pre_ans = ''
in_ans = ''
post_ans = ''
for edges in range(N):
    A, B, C = input().split()
    exist[ord(A)] = 1
    if B != '.':
        left[ord(A)] = ord(B)
    if C != '.':
        right[ord(A)] = ord(C)
preorder(65)
inorder(65)
postorder(65)
print(pre_ans)
print(in_ans)
print(post_ans)