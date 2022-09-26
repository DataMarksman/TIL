# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

N = int(input())
alp_set = set()
ans = []
for tc in range(1, N+1):
    lines = list(map(str, input().split()))
    for first_check in range(len(lines)):
        if lines[first_check][0].upper() not in alp_set:
            alp_set.add(lines[first_check][0].upper())
            lines[first_check]. replace(lines[first_check][0], '[' + lines[first_check][0] + ']')
            ans += lines
            break
    else:
        for second_check in range(len(lines)):
            for double_check in range(1, len(lines[second_check])):
                if lines[second_check][double_check].upper() not in alp_set:
                    lines[second_check].replace(lines[second_check][double_check],
                                                '[' + lines[second_check][double_check] + ']')
                    ans += lines
        else:
            ans += [lines]
for printing in range(len(ans)):
    print(ans[printing])
