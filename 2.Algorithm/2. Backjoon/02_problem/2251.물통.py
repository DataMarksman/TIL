# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
sys.setrecursionlimit(10**8)

# y 에서 x로 물을 이동 시키는 함수
def water_dist(X, x, y):
    if X-x < y:
        px = int(X)
        py = y - (X - x)
    else:
        px = x + y
        py = 0
    result = (px, py)
    return result


# 한번 사이클 돌리면서 모든 경우의 수를 보려는 함수
def pulling(a, b, c):
    global ans_set
    global visited
    if a == 0:
        ans_set.add(c)
    water_list = [a, b, c]
    for w_d in range(3):
        wd_list = [int(a), int(b), int(c)]
        wd_list[w_d], wd_list[(w_d+1)%3] = water_dist(limit_list[w_d], water_list[w_d], water_list[(w_d+1)%3])
        da, db, dc = wd_list[0], wd_list[1], wd_list[2]
        if 0 <= da <= A and 0 <= db <= B and 0 <= dc <= C and (da, db, dc) not in visited:
            visited.add((da, db, dc))
            pulling(da, db, dc)
    for w_p in range(3):
        wp_list = [int(a), int(b), int(c)]
        wp_list[w_p], wp_list[(w_p + 2) % 3] = water_dist(limit_list[w_p], water_list[w_p], water_list[(w_p + 2) % 3])
        pa, pb, pc = wp_list[0], wp_list[1], wp_list[2]
        if 0 <= pa <= A and 0 <= pb <= B and 0 <= pc <= C and (pa, pb, pc) not in visited:
            visited.add((pa, pb, pc))
            pulling(pa, pb, pc)


ans_set = set()
visited = set()
A, B, C = map(int, input().split())
A, B, C = int(A), int(B), int(C)
limit_list = [A, B, C]
pulling(0, 0, int(C))
# ans_set.remove(0)
ans_list = sorted(list(ans_set))
print(*ans_list)