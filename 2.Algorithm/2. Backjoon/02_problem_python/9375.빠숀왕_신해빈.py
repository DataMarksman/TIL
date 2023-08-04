# BOJ. 9375. 빠쑌왕 오연님
# ???: 내가 먹으면 슈넬치킨도 샤넬치킨
# 설계 의도: 딕셔너리 활용
# 1. 딕셔너리에 set()으로 옷들 정리해서 넣고
# 2. 해당 종목들은 따로 set에도 저장해서 그걸 하나하나 빼면서 len(set())으로 답 도출
# 개선점:
# 딕셔너리를 순회할 수 있는 방법이 있을까요? 그러면 굳이 Set 안만들어도 되는데...

T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    wear_dict = {'': set(), }
    wear_set = set()
    for numbers in range(N):
        clothes = list(map(str, input().split(' ')))
        if clothes[1] in wear_dict:
            wear_dict[clothes[1]].add(clothes[0])
        else:
            wear_dict[clothes[1]] = set()
            wear_set.add(clothes[1])
            wear_dict[clothes[1]].add(clothes[0])
    ans = 1
    while wear_set:
        A = wear_set.pop()
        ans *= (len(wear_dict[A])+1)
    print(ans - 1)
