# Rooted Binary Tree

T = int(input())

for i in range(T):
    K = int(input())
    input_list = list(map(int,input().split()))
    po_list = []
    tmp_list = []
    print(f'#{i+1} {input_list[int((2**K-2)/2)]}')
    for j in range(K):
        if j == 0:
            po_list = [int((2**K-2)/2)]
        else:
            tmp_list = []
            po_list, tmp_list = tmp_list, po_list
            for tmp in tmp_list:
                po_list += [tmp-2**(K-j-1),tmp+2**(K-j-1)]
            answer_list = []
            for position in po_list:
                answer_list += [input_list[position]]
            print(answer_list)