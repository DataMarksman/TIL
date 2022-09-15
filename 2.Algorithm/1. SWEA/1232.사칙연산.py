# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

def rooting(point):
    if 0 < point <= N:
        if CC[point].isnumeric():
            return int(CC[point])
        else:
            if CC[point] == '*':
                result = rooting(left[point]) * rooting(right[point])
            elif CC[point] == '/':
                result = rooting(left[point]) // rooting(right[point])
            elif CC[point] == '+':
                result = rooting(left[point]) + rooting(right[point])
            elif CC[point] == '-':
                result = rooting(left[point]) - rooting(right[point])
            return result
    else:
        return 0


T = 10
for case_num in range(1, T + 1):
    N = int(input())
    left = [0]*(N+1)
    right = [0] * (N + 1)
    CC = ['0']*(N+1)
    for put_in in range(N):
        line = list(map(str, input().split()))
        if len(line) == 4:
            left[int(line[0])] = int(line[2])
            right[int(line[0])] = int(line[3])
            CC[int(line[0])] = line[1]
        elif len(line) == 2:
            CC[int(line[0])] = line[1]
    ans = rooting(1)
    print(f'#{case_num} {ans}')

