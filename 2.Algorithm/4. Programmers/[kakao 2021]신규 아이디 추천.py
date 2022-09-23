# def solution(new_id):
#     new_id = str(new_id).lower()
#
#
#     answer = ''
#     return answer
check_set = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             '0','1','2','3','4','5','6','7','8','9','-','_','.','-',}

def solution(new_id):
    new_id = str(new_id).lower()
    dot_flag = True
    first_id = ''
    for first_check in range(len(new_id)):
        if new_id[first_check] in check_set:
            if new_id[first_check] == '.':
                if dot_flag:
                    first_id += '.'
                    dot_flag = False
            else:
                first_id += new_id[first_check]
                dot_flag = True
    if first_id:
        if first_id[len(first_id)-1] == '.':
            first_id = first_id[:len(first_id)-1]
    if first_id:
        if first_id[0] == '.':
            first_id = first_id[1:]
    if not first_id:
        first_id = 'a'
    if len(first_id) >= 16:
        first_id = first_id[:15]
        while first_id[len(first_id)-1] == '.':
            first_id = first_id[:len(first_id)-1]
    while len(first_id) < 3:
         first_id += first_id[len(first_id)-1]
    answer = first_id
    return answer


A = ['...!@BaT#*..y.abcdefghijklm', 'z-+.^.', '=.=', '123_.def', 'abcdefghijklmn.p']
for printing in range(len(A)):
    print(solution(A[printing]))