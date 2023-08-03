# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
import numpy as np
import math
input = lambda: sys.stdin.readline().rstrip('\r\n')



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
    # 일단, 점들을 y축 좌표를 기준으로 정렬합니다.
    # 같은 y축 좌표를 가진 점들은 x축 좌표를 기준으로 정렬합니다.
    points.sort(key=lambda p: (p[1], p[0]))
    origin = points[0]
    rest = points[1:]

    # 시작점을 기준으로 다른 점들을 각도 순으로 정렬합니다.
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

    # 초기에 가장 왼쪽과 오른쪽의 점을 찾습니다.
    p_left = min(enumerate(hull), key=lambda p: p[1])
    p_right = max(enumerate(hull), key=lambda p: p[1])

    i = p_left[0]
    j = p_right[0]

    # 최소 사각형의 폭을 초기화합니다.
    min_width = float('inf')

    while i != p_right[0] or j != p_left[0]:
        width = dist(hull[i], hull[j])
        if width < min_width:
            min_width = width

        # i와 j를 각각 증가시킵니다.
        if (hull[(i + 1) % n][1] - hull[i][1]) * (hull[(j + 1) % n][0] - hull[j][0]) > (
                hull[(j + 1) % n][1] - hull[j][1]) * (hull[(i + 1) % n][0] - hull[i][0]):
            i = (i + 1) % n
        else:
            j = (j + 1) % n

    return min_width
turn = 0
while True:
    turn += 1
    N = int(input())
    if N == 0:
        break
    points = []
    for get_points in range(N):
        A, B = map(int, input().split())
        points.append((A,B))
    min_wide = "{:.2f}".format(math.ceil(rotating_calipers(points)*100)/100)
    print(f"Case {turn}: {min_wide}")
