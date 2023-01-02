# SWEA. 5658 보물상자 비밀번호
# 설계 목적: 그냥 구현
# 1. 각 4개의 스트링을 뒤에서 빼서 다음거 앞에 넣어주기
# 2. 이렇게 만들어지는 수를 set에 넣기
# 3. 만들어진 set을 sorted 리스트로 만들어서, 원하는 순번의 요소 출력
# 개선점:
# 1. 중간에 패턴 같은거 나오면 뺄까 했는데, 애초에 시간이 그렇게 타이트 하지 않아서 패스함.

T = int(input())
for case_num in range(1, T + 1):
    N, M = map(int, input().split())
    length = N//4
    lines = input()
    pass_word = []
    for rearrange in range(4):
        pass_word += [lines[rearrange*length:(rearrange+1)*length]]
    pass_word_set = set()
    count = 0
    while count < length+2:
        for making in range(4):
            pick = pass_word[making][-1]
            pass_word[making] = pass_word[making][:len(pass_word[making])-1]
            pass_word[(making+1) % 4] = pick + pass_word[(making + 1) % 4]
            pass_word_set.add(int(pass_word[(making+1) % 4][:length], 16))
        count += 1
    ans_list = sorted(list(pass_word_set), reverse=True)
    print(f'#{case_num} {ans_list[M-1]}')