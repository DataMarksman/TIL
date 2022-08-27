# 자주 쓰는 기법들을 정리해놓은 곳

# 1. 2차원 배열, 출력 형식에 맞게 join으로 풀어내기

my_list = [['1', '100', '33'], ['2', '100', '33'], ['3', '100', '33']]
for i in range(3):
    answer = ' '.join(my_list[i])
    print(answer)

# 2. 2차원 배열 zip으로 전치하기

re_board = list(map(list, zip(*my_list)))
for j in range(3):
    answer = ' '.join(re_board[j])
    print(answer)
