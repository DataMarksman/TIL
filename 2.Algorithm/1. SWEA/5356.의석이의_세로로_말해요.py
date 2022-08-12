# 5356. 의석이의 세로로 말해요

T = int(input())
for case_num in range(1,T+1):
    str_list = []
    line_list = []
    for lines in range(5):
        str_list += [list(map(str,input()))]
    for check in range(5):
        tmp_word = []
        for filling in range(15):
            try:
                tmp_word += [str_list[check][filling]]
            except:
                tmp_word += ['']
        line_list += [tmp_word]
    zipped_list = []
    for i in zip(line_list[0],line_list[1],line_list[2],line_list[3],line_list[4]):
        zipped_list += list(i)
    ans = f'#{case_num}'
    print(ans,''.join(zipped_list))