def solution(subway, start, end):
    answer = 0
    length = len(subway)
    subway_list = []
    start = str(start)
    end = str(end)
    for put_in in range(length):
        subway_list.append(set(subway[put_in].split(' ')))
    visited = set()
    passing = set()
    for first_riding in range(length):
        if start in subway_list[first_riding]:
            passing |= subway_list[first_riding]
            visited.add(first_riding)

    while end not in passing:
        answer += 1
        for checking in range(length):
            if checking not in visited and passing & subway_list[checking]:
                passing |= set(subway_list[checking])
                visited.add(checking)
        if end in passing:
            break
    return answer


print(solution(["1 2 4 5", "2 3 4 5 6", "1 2 6"], 1, 3))