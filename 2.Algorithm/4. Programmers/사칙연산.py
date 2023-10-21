# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:


def solution(arr):
    nums, ops = [], []
    for idx, element in enumerate(arr):
        if idx % 2:
            ops.append(element)
        else:
            nums.append(element)

    N = len(nums)
    dp_max = [[-100000] * N for _ in range(N)]
    dp_min = [[+100000] * N for _ in range(N)]

    for scope in range(N):
        for start in range(N - scope):
            end = start + scope
            if start == end:
                dp_max[start][start] = dp_min[start][start] = int(nums[start])
            else:
                for mid in range(start, end):
                    if ops[mid] == '+':
                        dp_max[start][end] = max(dp_max[start][mid] + dp_max[mid + 1][end], dp_max[start][end])
                        dp_min[start][end] = min(dp_min[start][mid] + dp_min[mid + 1][end], dp_min[start][end])
                    else:
                        dp_max[start][end] = max(dp_max[start][mid] - dp_min[mid + 1][end], dp_max[start][end])
                        dp_min[start][end] = min(dp_min[start][mid] - dp_max[mid + 1][end], dp_min[start][end])

    return dp_max[0][-1]
expression = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]
result = solution(expression)
print(result)