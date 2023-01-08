# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

def solution(gems):

    length = len(gems)
    min_length = int(length)
    answer = [1, length]
    check_set = set(gems)
    if length == len(check_set):
        return answer
    elif len(check_set) == 1:
        return [1, 1]

    check_dict = {}
    idx = 0
    for gem in list(check_set):
        check_dict[gem] = idx
        idx += 1

    pointers = [length-1]*len(check_set)
    pointers[check_dict[gems[0]]] = 0
    max_idx = max(pointers)
    min_idx = min(pointers)
    for top in range(len(gems)):
        if pointers[check_dict[gems[top]]] == min_idx:
            pointers[check_dict[gems[top]]] = top
            min_idx = min(pointers)
            this_length = max_idx - min_idx
            if this_length < min_length:
                min_length = this_length
                answer = [min(pointers)+1, max(pointers)+1]
                if min_length == length:
                    return answer
        if pointers[check_dict[gems[top]]] == max_idx:
            pointers[check_dict[gems[top]]] = top
            max_idx = max(pointers)
            this_length = max_idx - min_idx
            if this_length < min_length:
                min_length = this_length
                answer = [min(pointers)+1, max(pointers)+1]
                if min_length == length:
                    return answer
        else:
            pointers[check_dict[gems[top]]] = top
        top += 1
    return answer