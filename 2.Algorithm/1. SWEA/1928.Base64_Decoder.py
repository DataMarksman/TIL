# 1928. Base64 Decoder D2

# 64 encoding 문제.
# 보통 인크립 할때, 프로그램을 써서 몰랐는데, 그 구조를 이해하는데 정말 도움이 많이 되었다.

dict_24bit = str('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')

T = int(input())
for tc in range(1, T+1):
    str_list = list(input())
    encrp_number = str()
    answer = str('')
    for encryp in range(len(str_list)):
        code_A = str(bin(dict_24bit.index(str_list[encryp]))[2:])
        if len(code_A) >= 6:
            encrp_number += str(code_A)
        else:
            code_B = (str('000000')+code_A)[-6:]
            encrp_number += str(code_B)

    for ans_encryp in range(len(encrp_number)//8):
        code_C = chr(int(encrp_number[(8*ans_encryp):8*(ans_encryp+1)], 2))
        answer += code_C
    print(f'#{tc} {answer}')


