memo = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}


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
        if B < max(memo):
            if B in memo:
                answer += 1
        else:
            C = [i for i in range(B)]
            for checking in range(B):
                if C[checking] > 2:
                    memo.add(checking)
                    if B % C[checking] == 0:
                        break
                    else:
                        P = C[checking] * 2
                        while P < B:
                            C[P] = 0
                            P += C[checking]
            else:
                answer += 1
    return answer


print(solution(437674, 3))