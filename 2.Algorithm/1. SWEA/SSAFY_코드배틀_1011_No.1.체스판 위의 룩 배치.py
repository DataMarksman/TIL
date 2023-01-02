

T = int(input())
ans_list = []
for tc in range(T):
    row_set = set()
    column_set = set()
    flag = True
    for p in range(8):
        line = list(input())
        if flag:
            for t in range(8):
                if line[t] == 'O':
                    if p in row_set or t in column_set:
                        flag = False
                        break
                    else:
                        row_set.add(p)
                        column_set.add(t)
    if flag and len(row_set) == 8 and len(column_set) == 8:
        ans_list.append(1)
    else:
        ans_list.append(0)
for answer in range(T):
    print(f'#{answer+1} {"yes" if ans_list[answer] else "no"}')