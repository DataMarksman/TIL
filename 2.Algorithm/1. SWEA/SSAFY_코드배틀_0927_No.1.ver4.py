

T = int(input())
for tc in range(1, T+1):
    height, wide = map(int, input().split())
    R_list = []
    G_list = []
    B_list = []
    ans_set = set()
    for c in range(height):
        lines = list(input())
        if c == 0 or c == height-1:
            for r in range(wide):
                if lines[r] == 'R':
                    R_list.append((c, r))
                elif lines[r] == 'G':
                    G_list.append((c, r))
                else:
                    B_list.append((c, r))
        else:
            hold_r = 0
            hold_g = 0
            hold_b = 0
            for r in range(wide):
                if lines[r] == 'R' and not hold_r:
                    R_list.append((c, r))
                    if r != height-1:
                        hold_r = r+1
                elif lines[r] == 'G' and not hold_g:
                    G_list.append((c, r))
                    if r != height-1:
                        hold_g = r+1
                elif lines[r] == 'B' and not hold_b:
                    B_list.append((c, r))
                    if r != height-1:
                        hold_b = r+1
            for back_r in range(wide-1, -1, -1):
                if hold_r + hold_g + hold_b == 0:
                    break
                else:
                    if lines[back_r] == 'R' and hold_r:
                        R_list.append((c, back_r))
                        hold_r = 0
                    elif lines[back_r] == 'G' and hold_g:
                        G_list.append((c, back_r))
                        hold_g = 0
                    elif lines[back_r] == 'B' and hold_b:
                        B_list.append((c, back_r))
                        hold_b = 0

    for R in range(len(R_list)):
        for G in range(len(G_list)):
            for B in range(len(B_list)):
                R1, R2 = R_list[R][0], R_list[R][1]
                G1, G2 = G_list[G][0], G_list[G][1]
                B1, B2 = B_list[B][0], B_list[B][1]
                if (R2-G2)*(R2-B2) != 0:
                    if abs((R1-G1)/(R2-G2)) != abs((R1-B1)/(R2-B2)):
                        tri_wide = abs((R1*G2 + G1*B2 + B1*R2)-(R1*B2 + G1*R2 + B1*G2))/2
                        ans_set.add((tri_wide, R, G, B))

                elif (R2-G2)*(G2-B2) != 0:
                    if abs((R1-G1)/(R2-G2)) != abs((G1-B1)/(G2-B2)):
                        tri_wide = abs((R1*G2 + G1*B2 + B1*R2)-(R1*B2 + G1*R2 + B1*G2))/2
                        ans_set.add((tri_wide, R, G, B))

                elif (B2-G2)*(R2-B2) != 0:
                    if abs((B1-G1)/(B2-G2)) != abs((R1-B1)/(R2-B2)):
                        tri_wide = abs((R1*G2 + G1*B2 + B1*R2)-(R1*B2 + G1*R2 + B1*G2))/2
                        ans_set.add((tri_wide, R, G, B))

    count_list = []
    ans_list = sorted(list(ans_set), reverse=True)
    for re_c in range(len(ans_list)):
        for comp in range(re_c):
            if ans_list[comp][1] == ans_list[re_c][1] and ans_list[comp][2] == ans_list[re_c][2]\
                    and ans_list[comp][0] > ans_list[re_c][0]:
                break
            elif ans_list[comp][2] == ans_list[re_c][2] and ans_list[comp][3] == ans_list[re_c][3]\
                    and ans_list[comp][0] > ans_list[re_c][0]:
                break
            elif ans_list[comp][1] == ans_list[re_c][1] and ans_list[comp][3] == ans_list[re_c][3]\
                    and ans_list[comp][0] > ans_list[re_c][0]:
                break
        else:
            count_list.append(ans_list[re_c])
    print(R_list)
    print(G_list)
    print(B_list)
    print(count_list)
    print(f'#{tc} {len(count_list)}')
"""
[[6.0, 14, 0, 20000], [6.0, 13, 0, 20000], [6.0, 11, 0, 20000], 
[6.0, 10, 0, 20000], [6.0, 4, 300, 30000], [6.0, 3, 300, 30000], 
[6.0, 1, 300, 30000], [6.0, 0, 300, 30000], [5.0, 10, 300, 0], 
[5.0, 4, 0, 50000], [4.5, 14, 100, 30000], [4.5, 12, 100, 20000], 
[4.5, 12, 0, 10000], [4.5, 2, 300, 40000], [4.5, 2, 200, 30000], 
[4.5, 0, 200, 20000], [3.5, 9, 0, 40000], [3.5, 5, 300, 10000], 
[3.0, 10, 100, 10000], [3.0, 4, 100, 40000], [2.5, 11, 200, 0], 
[2.5, 3, 100, 50000], [2.0, 1, 200, 10000], [1.0, 8, 0, 0], 
[1.0, 7, 0, 0], [1.0, 6, 300, 50000], [1.0, 2, 0, 0], [0.5, 1, 100, 0]]
#4 28

[[6.0, 14, 0, 2], [6.0, 4, 3, 3], [5.0, 10, 3, 0], [5.0, 4, 0, 5], 
[4.5, 14, 1, 3], [4.5, 13, 1, 2], [4.5, 13, 0, 1], [4.5, 3, 3, 4], 
[4.5, 3, 2, 3], [4.5, 0, 2, 2], [3.5, 9, 0, 4], [3.5, 5, 3, 1], 
[3.0, 12, 0, 0], [3.0, 10, 1, 1], [3.0, 4, 1, 4], [3.0, 1, 3, 5], 
[2.5, 11, 2, 0], [2.5, 3, 1, 5], [2.0, 1, 2, 1], [0.5, 1, 1, 0]]
#4 20

5
2 2
RR
GB
2 3
RGB
BGR
4 4
RRRR
RRRR
BBBB
BBBB
5 5
RRRRR
GGBBB
RRRRR
BBBGG
RRRRR
10 10
RGBRGBRGBB
RGBRGBRGBR
RBGBRBGBRB
GBGGRRBGBG
RBGBRGBGRG
BGRGBGRGBG
RGBGBGBRRR
BGBRBGBGRB
RGBGBBGGRG
BGRGBGRGBG


"""