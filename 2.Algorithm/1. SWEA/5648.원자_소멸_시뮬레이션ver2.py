T = int(input())

for t in range(T):
    N = int(input())
    atom = {0: [], 1: [], 2: [], 3: []}
    energy = 0
    collision_info = {}
    time = []

    for _ in range(N):
        X, Y, direction, K = map(int, input().split())
        atom[direction] += [((X, Y), K, direction)]

    # 몇 초 후에 충돌하는지, 어느 방향으로 이동하는 것의 몇번째인지 (키, 밸류)로 저장
		# 중간에 크로스되는 애들 굳이 //2)+0.5로 처리한 건
    for v_0 in atom[0]:
        for v_1 in atom[1]:
            if v_0[0][0] == v_1[0][0] and v_0[0][1] < v_1[0][1]:
                if (v_1[0][1]-v_0[0][1]) % 2==0:
                    if (v_1[0][1]-v_0[0][1])//2 not in collision_info:
                        collision_info[(v_1[0][1]-v_0[0][1])//2] = set()
                        time.append((v_1[0][1]-v_0[0][1])//2)
                    collision_info[(v_1[0][1]-v_0[0][1])//2].add((0, v_0))
                    collision_info[(v_1[0][1]-v_0[0][1])//2].add((1, v_1))
                else:
                    if ((v_1[0][1]-v_0[0][1])//2)+0.5 not in collision_info:
                        collision_info[((v_1[0][1]-v_0[0][1])//2)+0.5] = set()
                        time.append(((v_1[0][1]-v_0[0][1])//2)+0.5)
                    collision_info[((v_1[0][1]-v_0[0][1])//2)+0.5].add((0, v_0))
                    collision_info[((v_1[0][1]-v_0[0][1])//2)+0.5].add((1, v_1))
        for v_2 in atom[2]:
            if v_0[0][0] < v_2[0][0] and (v_0[0][0]-v_2[0][0]) == (v_0[0][1]-v_2[0][1]):
                if v_2[0][0]-v_0[0][0] not in collision_info:
                    collision_info[v_2[0][0]-v_0[0][0]] = set()
                    time.append(v_2[0][0]-v_0[0][0])
                collision_info[v_2[0][0] - v_0[0][0]].add((0, v_0))
                collision_info[v_2[0][0] - v_0[0][0]].add((2, v_2))
        for v_3 in atom[3]:
            if v_0[0][0] > v_3[0][0] and (v_0[0][0]+v_0[0][1]) == (v_3[0][0]+v_3[0][1]):
                if v_0[0][0]-v_3[0][0] not in collision_info:
                    collision_info[v_0[0][0]-v_3[0][0]] = set()
                    time.append(v_0[0][0]-v_3[0][0])
                collision_info[v_0[0][0]-v_3[0][0]].add((0, v_0))
                collision_info[v_0[0][0]-v_3[0][0]].add((3, v_3))

    for v_1 in atom[1]:
        for v_2 in atom[2]:
            if v_1[0][0] < v_2[0][0] and (v_1[0][0]+v_1[0][1]) == (v_2[0][0]+v_2[0][1]):
                if v_2[0][0]-v_1[0][0] not in collision_info:
                    collision_info[v_2[0][0]-v_1[0][0]] = set()
                    time.append(v_2[0][0]-v_1[0][0])
                collision_info[v_2[0][0]-v_1[0][0]].add((1, v_1))
                collision_info[v_2[0][0]-v_1[0][0]].add((2, v_2))
        for v_3 in atom[3]:
            if v_1[0][0] > v_3[0][0] and (v_1[0][0]-v_1[0][1]) == (v_3[0][0]-v_3[0][1]):
                if v_1[0][0]-v_3[0][0] not in collision_info:
                    collision_info[v_1[0][0]-v_3[0][0]] = set()
                    time.append(v_1[0][0]-v_3[0][0])
                collision_info[v_1[0][0]-v_3[0][0]].add((1, v_1))
                collision_info[v_1[0][0]-v_3[0][0]].add((3, v_3))

    for v_2 in atom[2]:
        for v_3 in atom[3]:
            if v_2[0][1] == v_3[0][1] and v_2[0][0] > v_3[0][0]:
                if (v_2[0][0]-v_3[0][0]) % 2 == 0:
                    if (v_2[0][0]-v_3[0][0])//2 not in collision_info:
                        collision_info[(v_2[0][0]-v_3[0][0])//2] = set()
                        time.append((v_2[0][0]-v_3[0][0])//2)
                    collision_info[(v_2[0][0]-v_3[0][0])//2].add((2, v_2))
                    collision_info[(v_2[0][0]-v_3[0][0])//2].add((3, v_3))
                else:
                    if ((v_2[0][0]-v_3[0][0])//2)+0.5 not in collision_info:
                        collision_info[((v_2[0][0]-v_3[0][0])//2)+0.5] = set()
                        time.append(((v_2[0][0]-v_3[0][0])//2)+0.5)
                    collision_info[((v_2[0][0]-v_3[0][0])//2)+0.5].add((2, v_2))
                    collision_info[((v_2[0][0]-v_3[0][0])//2)+0.5].add((3, v_3))

    time.sort()

    for min in time:
        flag = 0
        for p in collision_info[min]:
            if p[1] in atom[p[0]]:
                flag += 1
        if flag >= 2:
            for p in collision_info[min]:
                if p[1] in atom[p[0]]:
                    energy += p[1][1]
                    atom[p[0]].remove(p[1])

    print(f'#{t+1}', energy)
