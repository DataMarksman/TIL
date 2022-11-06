# SWEA. 5550. 나는 개구리로소이다.
# 설계 목적:
# 1. 뽑으면서, 앞의 글자들이 이미 내 순번의 글자보다 많이 나왔는지 체크해주기
# 2. 일단 C가 나오면 top을 += 1 해줘서 최대값을 늘려주고
# 3. K가 나오면 top -= 1 해줘서 이론상 최대값을 낮춰준다.
# 4. C가 나올 때마다 ans 값을 갱신해주면, ANS는 이론상 나올 수 있는 최솟값을 가져간다.
# 개선점:
# 1. 처음에 문제를 잘못 이해해서 croak가 서로 겹칠 수 있다는 줄 알고 풀었다가 틀렸다. 로직 바꾸니 바로 풀림

T = int(input())
for case_num in range(1, T + 1):
    line = list(input())
    croak_dict = {'c':0, 'r':1, 'o':2, 'a':3, 'k':4}
    count_list = [0, 0, 0, 0, 0]
    top = 0
    ans = 0
    flag = True
    if len(line)%5 != 0:
        flag = False
    for checking in range(len(line)):
        if flag:
            pick = croak_dict[line[checking]]
            count_list[pick] += 1
            if line[checking] == 'c':
                top += 1
                ans = max(ans, top)
            else:
                if line[checking] == 'k':
                    top -= 1
                if max(count_list[:pick]) < count_list[pick]:
                    flag = False
                    break
        else:
            break
    else:
        if min(count_list) != max(count_list):
            flag = False
    if flag:
        print(f'#{case_num} {ans}')
    else:
        print(f'#{case_num} {-1}')

"""

8
crcoarkcoroakak
ccccrrrrooooaaaakkkk
karoc
croakcorakcroak
ccroak
croakcroakcroakcroakcroakcroakcroakcroakcroakcroak
ccccccccccrrrrrrrrrrooooooooooaaaaaaaaaakkkkkkkkkk
crcocrroaokacakkrocrakcorakoak
"""