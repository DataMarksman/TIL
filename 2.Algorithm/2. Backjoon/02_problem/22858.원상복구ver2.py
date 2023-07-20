# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.setrecursionlimit(10**8)

N, k = map(int, input().split())
cards = list(map(int, input().split()))
origin_shuffle_idx = list(map(int, input().split()))
shuffle_idx = [0]*(N+1)
for shuffling in range(len(origin_shuffle_idx)):
    shuffle_idx[origin_shuffle_idx[shuffling]] = shuffling+1

visited = set()
shuffle_loop = []
loop_idx = [(0, 0) for _ in range(N+1)]

def find_loop(origin, idx, loop_number, loop_list_idx):
    global visited
    if idx == origin:
        return
    else:
        visited.add(idx)
        shuffle_loop[loop_number].append(idx)
        loop_idx[idx] = (loop_number, loop_list_idx)
        find_loop(origin, shuffle_idx[idx],loop_number, loop_list_idx + 1)

for loop_check in range(1, N+1):
    if loop_check not in visited:
        visited.add(loop_check)
        loop_number = len(shuffle_loop)
        loop_idx[loop_check] = (loop_number, 0)
        shuffle_loop.append([loop_check, ])
        find_loop(loop_check, shuffle_idx[loop_check], loop_number, 1)

new_deck = [0]*N

for shuffle in range(N):
    loop_set_idx, loop_index = loop_idx[shuffle+1]
    length = len(shuffle_loop[loop_set_idx])
    present_idx = shuffle_loop[loop_set_idx][( loop_index + k ) % length]
    new_deck[shuffle] = cards[present_idx-1]

print(*new_deck)

"""
5 2
4 1 3 5 2
4 3 1 2 5

1 4 5 3 2

5 1
4 1 3 5 2
4 3 1 2 5

3 5 1 4 2
"""
