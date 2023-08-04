# BOJ. 11403 경로 찾기
# 설계 의도: 이거 진짜 배수 그래프 열화버전이군요 백트 안해도 102ms 나옵니다.
# 1. 일단 set()으로 스택을 만듭니다. 괜찮습니다.
# 2. visited도 set()으로 만들어 주시구요.
# 3. 각 행을 돌면서 그 행에서 갈 수 있는 모든 행선지를 stack에 넣습니다.
# 4. 그리고 그렇게 넣은 행선지에서도 같은 작업을 반복해줍니다. 물론 지나간 곳은 visited에 넣구요.
# 5. 죄다 set 이라서 연산 효율이 굉장합니다.
# 6. 그렇게 stack이 바닥나면, 해당 행에서 출발해서 갈 수 있는 모든 곳을 찾아본 것이므로
# 7. visited에서 하나씩 좌표를 빼와서 해당 열에서 갈 수 있는 곳들을 마킹해줍니다.
# 8. 이걸 행만큼 반복하고 출력하면 끝.

N = int(input())
root_list = [list(map(int, input().split())) for _ in range(N)]
ans_list = [[0]*N for i in range(N)]
for x in range(N):
    stack = set()
    visited = set()
    stack.add(x)
    flag = True
    while flag and stack:
        start = stack.pop()
        for y in range(N):
            if root_list[start][y] == 1 and y not in visited:
                stack.add(y)
                visited.add(y)
        if len(visited) >= N:
            flag = False
    while visited:
        put_in = visited.pop()
        ans_list[x][put_in] = 1
for print_on in range(N):
    print(*ans_list[print_on])

