# 1928. Base64 Decoder D2

# 64 encoding 문제.
# 보통 인크립 할때, 프로그램을 써서 몰랐는데, 그 구조를 이해하는데 정말 도움이 많이 되었다.

dict_24bit = str('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')

case_number = int(input())
for i in range(case_number):
    encryp_24 = []
    original_24 = list(map(str,input()))
    for alp in original_24():
        

