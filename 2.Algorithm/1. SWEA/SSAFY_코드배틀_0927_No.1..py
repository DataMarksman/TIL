

T = int(input())
for tc in range(1, T+1):
    height, wide = map(int, input().split())
    R_list = []
    G_list = []
    B_list = []
    ans_set = set()
    for c in range(height):
        lines = list(input())
        for r in range(wide):
            if lines[r] == 'R':
                R_list.append((c, r))
            elif lines[r] == 'G':
                G_list.append((c, r))
            elif lines[r] == 'B':
                B_list.append((c, r))
    for R in range(len(R_list)):
        for G in range(len(G_list)):
            max_wide = 0
            max_triangle = 0
            for B in range(len(B_list)):
                R1, R2 = R_list[R][0], R_list[R][1]
                G1, G2 = G_list[G][0], G_list[G][1]
                B1, B2 = B_list[B][0], B_list[B][1]
                if (R2-G2)*(R2-B2) != 0:
                    if abs((R1-G1)/(R2-G2)) != abs((R1-B1)/(R2-B2)):
                        tri_wide = abs((R1*G2 + G1*B2 + B1*R2)-(R1*B2 + G1*R2 + B1*G2))/2
                        if tri_wide > max_wide:
                            max_wide = float(tri_wide)
                            max_triangle = (max_wide, R, G*100, B*10000)

                elif (R2-G2)*(G2-B2) != 0:
                    if abs((R1-G1)/(R2-G2)) != abs((G1-B1)/(G2-B2)):
                        tri_wide = abs((R1*G2 + G1*B2 + B1*R2)-(R1*B2 + G1*R2 + B1*G2))/2
                        if tri_wide > max_wide:
                            max_wide = float(tri_wide)
                            max_triangle = (max_wide, R, G*100, B*10000)

                elif (B2-G2)*(R2-B2) != 0:
                    if abs((B1-G1)/(B2-G2)) != abs((R1-B1)/(R2-B2)):
                        tri_wide = abs((R1*G2 + G1*B2 + B1*R2)-(R1*B2 + G1*R2 + B1*G2))/2
                        if tri_wide > max_wide:
                            max_wide = float(tri_wide)
                            max_triangle = (max_wide, R, G*100, B*10000)
            if max_wide > 0:
                ans_set.add(max_triangle)

    for R_2 in range(len(R_list)):
        for B_2 in range(len(B_list)):
            max_wide = 0
            max_triangle = 0
            for G_2 in range(len(G_list)):
                R1, R2 = R_list[R_2][0], R_list[R_2][1]
                G1, G2 = G_list[G_2][0], G_list[G_2][1]
                B1, B2 = B_list[B_2][0], B_list[B_2][1]
                if (R2 - G2) * (R2 - B2) != 0:
                    if abs((R1 - G1) / (R2 - G2)) != abs((R1 - B1) / (R2 - B2)):
                        tri_wide = abs((R1 * G2 + G1 * B2 + B1 * R2) - (R1 * B2 + G1 * R2 + B1 * G2)) / 2
                        if tri_wide > max_wide:
                            max_wide = float(tri_wide)
                            max_triangle = (max_wide, R_2, G_2*100, B_2*10000)

                elif (R2 - G2) * (G2 - B2) != 0:
                    if abs((R1 - G1) / (R2 - G2)) != abs((G1 - B1) / (G2 - B2)):
                        tri_wide = abs((R1 * G2 + G1 * B2 + B1 * R2) - (R1 * B2 + G1 * R2 + B1 * G2)) / 2
                        if tri_wide > max_wide:
                            max_wide = float(tri_wide)
                            max_triangle = (max_wide, R_2, G_2*100, B_2*10000)

                elif (B2 - G2) * (R2 - B2) != 0:
                    if abs((B1 - G1) / (B2 - G2)) != abs((R1 - B1) / (R2 - B2)):
                        tri_wide = abs((R1 * G2 + G1 * B2 + B1 * R2) - (R1 * B2 + G1 * R2 + B1 * G2)) / 2
                        if tri_wide > max_wide:
                            max_wide = float(tri_wide)
                            max_triangle = (max_wide, R_2, G_2*100, B_2*10000)
            if max_wide > 0:
                ans_set.add(max_triangle)

    for G_3 in range(len(G_list)):
        for B_3 in range(len(B_list)):
            max_wide = 0
            max_triangle = 0
            for R_3 in range(len(R_list)):
                R1, R2 = R_list[R_3][0], R_list[R_3][1]
                G1, G2 = G_list[G_3][0], G_list[G_3][1]
                B1, B2 = B_list[B_3][0], B_list[B_3][1]
                if (R2 - G2) * (R2 - B2) != 0:
                    if abs((R1 - G1) / (R2 - G2)) != abs((R1 - B1) / (R2 - B2)):
                        tri_wide = abs((R1 * G2 + G1 * B2 + B1 * R2) - (R1 * B2 + G1 * R2 + B1 * G2)) / 2
                        if tri_wide > max_wide:
                            max_wide = float(tri_wide)
                            max_triangle = (max_wide, R_3, G_3*100, B_3*10000)

                elif (R2 - G2) * (G2 - B2) != 0:
                    if abs((R1 - G1) / (R2 - G2)) != abs((G1 - B1) / (G2 - B2)):
                        tri_wide = abs((R1 * G2 + G1 * B2 + B1 * R2) - (R1 * B2 + G1 * R2 + B1 * G2)) / 2
                        if tri_wide > max_wide:
                            max_wide = float(tri_wide)
                            max_triangle = (max_wide, R_3, G_3*100, B_3*10000)

                elif (B2 - G2) * (R2 - B2) != 0:
                    if abs((B1 - G1) / (B2 - G2)) != abs((R1 - B1) / (R2 - B2)):
                        tri_wide = abs((R1 * G2 + G1 * B2 + B1 * R2) - (R1 * B2 + G1 * R2 + B1 * G2)) / 2
                        if tri_wide > max_wide:
                            max_wide = float(tri_wide)
                            max_triangle = (max_wide, R_3, G_3*100, B_3*10000)
            if max_wide > 0:
                ans_set.add(max_triangle)
    print(ans_set)
    count_set = set()
    ans_list = sorted(list(ans_set))
    while ans_list:
        pick = ans_list.pop(0)
        for checking in range(len(ans_list)):
            if pick
    print(f'#{tc} {len(ans_set)}')
