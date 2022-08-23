# 이것은 간략하게 코드 돌려보기 위한 용도의 TEST.py 입니다.

# aa = {'0': 'AA','1': 'BB','2': 'CC'}

# print(aa.get('AA'))
A = set()
B = set()
A.add(5)
A.add(3)
A.add(7)
B.add(2)
B.add(9)
B.add(6)

print(1 if A&B else 0)