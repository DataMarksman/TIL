# BOJ. 2263 트리의 순회
# 설계 의도:
# 1. 중위 순회 리스트가 값 빼오는 본체
# 2. 후위 순회 리스트의 동일 범위 내 가장 끝 값이 해당 줒위 순회 서브 노드의 루트 노드.
# 3. 한번만 서칭해서 가져오기 위해서 position 리스트 만들고 in_list의 값들이 어디 있는지 idx와 역매칭
# 4. 시간 촉박, 메모리 촉박...
# 개선점:
# 겨우 통과해서, 시간도 메모리도 개선해야 할 곳이 한가득
import sys
sys.setrecursionlimit(10**5)


def preorder(start, end, count):
    if end > start:
        pick = post_list[end-count]
        idx = position[pick]
        ans.append(pick)
        if start < idx-1:
            preorder(start, idx-1, count)
        elif start == idx-1:
            ans.append(post_list[start - count])
        if idx + 1 < end:
            preorder(idx+1, end, count + 1)
        elif idx + 1 == end:
            ans.append(post_list[end - count - 1])
    elif end == start:
        ans.append(post_list[end-count])


N = int(sys.stdin.readline())
in_list = list(map(int, sys.stdin.readline().split()))
post_list = list(map(int, sys.stdin.readline().split()))
position = [0]*(N+1)
for positioning in range(N):
    position[in_list[positioning]] = positioning
ans = []

preorder(0, N-1, 0)
print(*ans)


"""
21
1 3 2 7 4 6 5 15 11 9 12 8 13 10 14 21 19 17 20 16 18
1 2 3 4 5 6 7 11 12 9 13 14 10 8 15 19 20 17 18 16 21
"""
