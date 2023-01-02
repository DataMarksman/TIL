# BOJ. 17136.색종이 붙이기
# 설계 의도: 각 좌측 상단 1을 기준으로 가장 큰 사각형이 들어가는지 여부를 판단하자.
# 2차원 배열은 싫으니까, set 에서 넣어서 좌표 값으로 놀자.
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 색종이 개수 찾는 함수
def finding(start_X, start_Y, count_list, X_count, visited):
    global ans
    visited = set(visited)

    # 종료 조건: 전부 다 붙였을 때,
    if len(visited) == len(idx_set):
        if X_count < ans:
            ans = X_count
            # print(count_list)
        return

    # 안될 성 싶은 것은 미리미리 차단.
    elif X_count > ans:
        return

    else:
        # 첫 Y 값만 시작 값으로 가져가고 나머지는 그냥 0부터 시작하게 하는 flag
        start_flag = True
        for check_X in range(start_X, 10):
            if not start_flag:
                start_Y = 0
            for check_Y in range(start_Y, 10):
                start_flag = False

                # 각 좌표가 idx set 에는 들어가 있고, 이미 밟은 곳에는 안들어가 있으면 진입
                if (check_X, check_Y) in idx_set and (check_X, check_Y) not in visited:

                    # 큰 색종이 부터 붙여보기
                    for sizing in range(5, 0, -1):
                        if count_list[sizing-1] < 5:
                            temp_visited = set()
                            size_flag = True
                            for size_x in range(sizing):
                                if size_flag:
                                    for size_y in range(sizing):
                                        if (check_X + size_x, check_Y + size_y) in idx_set and (check_X + size_x, check_Y + size_y) not in visited:
                                            temp_visited.add((check_X + size_x, check_Y + size_y))
                                        else:
                                            size_flag = False
                                            break
                                else:
                                    break
                            else:
                                # 다 돌았으면 큰 색종이 붙인 상태로 재귀 함수 돌입
                                if size_flag:
                                    temp_count_list = count_list[:]
                                    temp_count_list[sizing-1] += 1
                                    finding(check_X, check_Y, temp_count_list, X_count + 1, visited | temp_visited)
                        else:
                            continue
                    else:
                        return


# 각 좌표값 받아서 넣어줄 idx_set 입니당
idx_set = set()
ans = 999999999999999999999999
for get_X in range(10):
    line = list(map(int, input().split()))
    for get_Y in range(10):
        if line[get_Y] == 1:
            idx_set.add((get_X, get_Y))
finding(0, 0, [0, 0, 0, 0, 0], 0, set())
if ans < 99999999999:
    print(ans)
else:
    print(-1)