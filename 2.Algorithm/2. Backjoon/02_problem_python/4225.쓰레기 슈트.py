# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
import numpy as np
import math

# 함수: 점들 간의 각도를 계산
def get_angle(p1, p0):
    dy = p1[1] - p0[1]
    dx = p1[0] - p0[0]
    return np.arctan2(dy, dx)

# 함수: 두 벡터 간의 외적을 계산
def cross_product(p1, p2):
    return p1[0] * p2[1] - p2[0] * p1[1]

# 함수: 두 점 사이의 거리를 계산
def dist(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# 함수: 점들로부터 Convex Hull을 찾는 Graham's Scan 알고리즘
def graham_scan(points):
    points.sort(key=lambda p: (p[1], p[0]))
    origin = points[0]
    rest = points[1:]
    rest.sort(key=lambda p: get_angle(p, origin))
    hull = [origin, rest[0]]
    for r in rest[1:]:
        while len(hull) > 1 and cross_product((hull[-1][0] - hull[-2][0], hull[-1][1] - hull[-2][1]),
                                              (r[0] - hull[-1][0], r[1] - hull[-1][1])) <= 0:
            hull.pop()
        hull.append(r)
    return hull

# 함수: Rotating Calipers 알고리즘을 적용하여 최소 사각형을 찾습니다.
def rotating_calipers(points):
    hull = graham_scan(points)
    n = len(hull)
    min_width = float('inf')
    for i in range(n):
        p1 = hull[i]
        p2 = hull[(i+1)%n]
        # edge vector
        edge = [p2[0]-p1[0], p2[1]-p1[1]]
        # perpendicular vector
        perp = [-edge[1], edge[0]]
        for p in hull:
            diff = [p[0]-p1[0], p[1]-p1[1]]
            # projection of diff onto perp
            proj = abs(diff[0]*perp[0] + diff[1]*perp[1]) / math.sqrt(perp[0]**2 + perp[1]**2)
            if proj < min_width:
                min_width = proj
    return min_width

turn = 0
while True:
    turn += 1
    N = int(input())
    if N == 0:
        break
    points = []
    for _ in range(N):
        A, B = map(int, input().split())
        points.append((A, B))
    print(rotating_calipers(points))
    min_wide = "{:.2f}".format(rotating_calipers(points))
    print(f"Case {turn}: {min_wide}")
