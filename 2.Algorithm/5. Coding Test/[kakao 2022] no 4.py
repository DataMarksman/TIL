def inorder(K, c):
    global check_list
    global result_list
    if c <= K:
        inorder(K, 2 * c)
        result_list[c] = int(check_list.pop(0))
        inorder(K, (2 * c) + 1)


def solution(numbers):
    answer = []
    for checking in range(len(numbers)):
        str_bin = bin(numbers[checking])[2:]
        length = len(str_bin)
        global check_list
        global result_list
        check_list = list(str_bin)
        result_list = [0] * (length + 1)
        inorder(length, 1)

        flag = True
        for rechecking in range(length, 1, -1):
            if result_list[rechecking] and flag:
                P = rechecking
                while P > 1:
                    P //= 2
                    if not result_list[P]:
                        flag = False
                        break

        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer

"""
        print('=====', checking + 1, '======')
        print('str_bin:', str_bin)
        print('check_list:', check_list)
        print('result_list:', result_list)
"""
print(solution([8, 100000, 102, 1]))