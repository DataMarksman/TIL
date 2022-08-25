# 1928. Base64 Decoder D2

# 64 encoding 문제.
# 보통 인크립 할때, 프로그램을 써서 몰랐는데, 그 구조를 이해하는데 정말 도움이 많이 되었다.

dict_24bit = str('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')

case_number = int(input())
for i in range(case_number):
    encryp_24 = []
    original_24 = list(map(str,input()))
    for alp in original_24():
        

# 요컨데, str에서 find로 각 알파벳 순서 찾으면 그게 24en 표 상의 수 이므로 이것을 by로 바꾸고
# 이걸 또 4개씩 이어 붙이고, 그걸 8개씩 끝어서 이어주는 것으로 다시 아스키 코드 -> 문자로 변환.
# 졸리지만 않으면 충분히 적고 잤을텐데 아쉽다.