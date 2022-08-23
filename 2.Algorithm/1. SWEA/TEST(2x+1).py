# 이것은 간략하게 코드 돌려보기 위한 용도의 TEST.py 입니다.
ans_list_1 = []
ans_list_2 = []
ans_set = set()
for i in range(1, 101):
    for j in range(1, 101):
        if i < j:
            print(f'a:{j}, b:{i}: 몫:{j//i}, 나머지:{j%i}')
            ans_set.add((j//i, j%i))
print(len(ans_set))
