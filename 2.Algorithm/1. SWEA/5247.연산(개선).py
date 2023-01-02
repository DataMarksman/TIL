# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.
for case_num in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    visited = set()
    count = 0
    stack = {N, }
    while M not in visited:
        routine = set()
        while stack:
            pick = stack.pop()
            for rooting in [pick+1, pick-1, pick*2, pick-10]:
                if 0 < rooting <= 1000000 and rooting not in visited:
                    routine.add(rooting)
                    visited.add(rooting)
        stack = set(routine)
        count += 1
    print(f'#{case_num} {count}')