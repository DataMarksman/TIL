# 이것은 간략하게 코드 돌려보기 위한 용도의 TEST.py 입니다.

# aa = {'0': 'AA','1': 'BB','2': 'CC'}

# print(aa.get('AA'))
cards = [1, 2, 3]
new_list = []
def permutation(list_card):
    for chcking in range(3):
        if cards[chcking] not in 