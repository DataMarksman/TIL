memo = {2, 3, 5, 7, 11, 13, 17, }


def solution(n, k):
    global memo
    String = ''
    answer = 0
    num_list = []
    while n > 0:
        A = str(n % k)
        if A == '0':
            if String:
                num_list.append(int(String[::-1]))
                String = ''
        else:
            String += A
        n //= k
    num_list.append(int(String[::-1]))
    while num_list:
        B = num_list.pop()
        if B == 2:
            answer += 1
        elif B > 2:
            if B < max(memo) and B not in memo:
                pass
            else:
                flag = True
                while flag:
                    C = [i for i in range(2*B)]
                    for checking in range(2, B):
                        if B % checking == 0:
                            flag = False
                            break
                        elif C[checking] >= 2 and checking not in memo:
                            memo.add(checking)
                            P = C[checking]
                            while P < B:
                                P += P
                                C[P] = 0

                answer += 1
    return answer

print(solution(110011, 10))