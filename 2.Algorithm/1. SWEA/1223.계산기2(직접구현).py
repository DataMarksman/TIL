# SWEA.1224 계산기2
# 설계 목적: 후위연산 학습
# 1.
# 개선점:
# 1.

T = 1
for case_num in range(1,T+1):
    N = int(input())
    input_list = list(input())
    tag_stack = []
    tag_top = -1
    ans_list = []
    priority_c = {'*':2,'/':2,'+':1,'-':1,'(':3}
    priority_s = {'*':2,'/':2,'+':1,'-':1,'(':0}
    while input_list:
        pick = input_list.pop(0)
        if pick.isnumeric():
            ans_list += pick
        else:
            if tag_top == -1:
                tag_stack += pick
                tag_top += 1
            elif pick == ')':
                while pick != '(':
                    pick = tag_stack.pop()
                    tag_top -= 1
                    if pick != '(' and pick != ')':
                        ans_list += pick
            elif priority_c[pick] > priority_s[tag_stack[tag_top]]:
                tag_stack += pick
                tag_top += 1
            elif priority_c[pick] <= priority_s[tag_stack[tag_top]]:
                tmp_tag = str(pick)
                while priority_c[pick] <= priority_s[tag_stack[tag_top]] and tag_stack:
                    pick = tag_stack.pop()
                    tag_top -= 1
                    ans_list += pick
                    if not tag_stack:
                        break
                ans_list += tmp_tag
    while tag_stack:
        ans_list += [tag_stack.pop()]
    print(ans_list)



