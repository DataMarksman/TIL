T = int(input())
for case_num in range(1, T+1):
    N, min_k, max_k = tuple(map(int, input().split()))
    score_list = list(map(int, input().split()))
    score_list.sort()
    min_score = min(score_list)
    max_score = max(score_list)
    score_count = [0]*101
    for check in range(N):
        score_count[score_list[check]] += 1
    diff_set = set()
    for cut_a in range(min_score+1, max_score):
        for cut_b in range(cut_a+1, max_score+1):
            C = sum(score_count[min_score:cut_a])
            B = sum(score_count[cut_a:cut_b])
            A = sum(score_count[cut_b:max_score+1])
            if min_k <= A <= max_k and min_k <= B <= max_k and min_k <= C <= max_k:
                diff = max(A, B, C)-min(A, B, C)
                diff_set.add(int(diff))
    if diff_set:
        print(f'#{case_num} {min(diff_set)}')
    else:
        print(f'#{case_num} {-1}')





