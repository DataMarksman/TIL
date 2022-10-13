# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    even_list = [[] for _ in range(N-1)]
    odd_list = [[] for _ in range(N)]
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if (i + j) % 2 == 0:
                odd_list[(i+j)//2].append(line[j])
            else:
                even_list[(i+j)//2].append(line[j])
    odd_list.pop(0)
    odd_list.pop()

    for ped1 in range(len(even_list)):
        if len(even_list[ped1]) < N-1:
            even_list[ped1] = [0]*(((N-1)-len(even_list[ped1]))//2) \
                              + even_list[ped1] + [0]*(((N-1)-len(even_list[ped1]))//2)
    even_list = [[0] * (N - 1)] + even_list + [[0] * (N - 1)]

    for ped2 in range(len(odd_list)):
        if len(odd_list[ped2]) < N:
            odd_list[ped2] = [0] * ((N - len(odd_list[ped2])) // 2) \
                             + odd_list[ped2] + [0] * ((N - len(odd_list[ped2])) // 2)
    odd_list = [[0] * N] + odd_list + [[0] * N]
    print(even_list)
    print(odd_list)
    ans = 0
    for EX in range(1, len(even_list)-1):
        for EY in range(len(even_list[EX])-1):
            for length_E in range(1, len(even_list)-2-EX):
                visited = set()
                for picking in range(length_E + 1):
                    visited.add(even_list[EX + picking][EY])
                    visited.add(even_list[EX + picking][EY + 1])
                if len(visited) == (length_E + 1) * 2 and 0 not in visited:
                    wide = 2
                    while 0 not in visited:
                        if len(visited) > ans:
                            ans = len(visited)
                        if EY + wide == len(even_list[EX]):
                            break
                        if even_list[EX][EY+wide] not in visited and\
                                even_list[EX+length_E][EY+wide] not in visited:
                            visited.add(even_list[EX][EY+wide])
                            visited.add(even_list[EX+length_E][EY+wide])
                        wide += 1

    for OX in range(1, len(odd_list)-1):
        for OY in range(1, len(odd_list[OX])-1):
            for length_O in range(1, len(odd_list)-2-OX):
                visited = set()
                for picking in range(length_O+1):
                    visited.add(odd_list[OX+picking][OY])
                    visited.add(odd_list[OX+picking][OY+1])
                if len(visited) == (length_O+1)*2 and 0 not in visited:
                    wide = 2
                    while 0 not in visited:
                        if len(visited) > ans:
                            ans = len(visited)
                        if OY + wide == len(even_list[OX]):
                            break
                        if odd_list[OX][OY+wide] not in visited and\
                                odd_list[OX+length_O][OY+wide] not in visited:
                            visited.add(odd_list[OX][OY+wide])
                            visited.add(odd_list[OX+length_O][OY+wide])
                        wide += 1

    print(f'#{case_num} {ans}')