def solution(reference, track):
    N = len(track)
    T = len(reference)
    answer = N
    idx_dict = {0: [], }
    check_list = [set() for _ in range(N)]
    for indexing in range(T):
        if idx_dict.get(reference[indexing]):
            idx_dict[reference[indexing]] += [indexing]
        else:
            idx_dict[reference[indexing]] = [indexing, ]


    for checking in range(N):
        start_set = set(idx_dict[track[checking]])
        while start_set:
            pick = start_set.pop()
            now_idx = 0
            for counting in range(pick, T):
                if now_idx + checking <= N-1 and reference[counting] == track[now_idx+checking]:
                    check_list[now_idx].add(now_idx+1)
                    now_idx += 1
                else:
                    answer = min(answer, (now_idx + 1))
                    break

    for rechecking in range(N):
        if len(check_list[rechecking]) == 1:
            check_idx = rechecking - check_list[rechecking].pop()
            if check_idx >= 0:
                answer = min(answer, max(check_list[rechecking]))

    print(idx_dict)
    return answer

edges = "abc"
roots = "bcab"
print(solution(edges, roots))