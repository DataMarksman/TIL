# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

while True:
    code_list = [[] for _ in range(32)]
    try:
        for get_code in range(32):
            code_list[get_code] = input()
        pc_address = 0
        memory_address = '00000000'
        for read_code in range(32):
            line = code_list[read_code]
            code, numb = line[:3], line[3:]
            pc_address += 1

            if code == '000':
                 code_list[int('0b'+numb, 2)] = memory_address
            elif code == '001':
                memory_address = code_list[int('0b'+numb, 2)]
            elif code == '010':
                if int(memory_address, 2) == 0:
                    pc_address = int('0b' + numb, 2)
            elif code == '100':
                ans = bin(int(ans, 2) - 1)
            elif code == '101':
                ans = bin(int(ans, 2) + 1)
                if len(ans) > 10:
                    ans = '0b' + ans[len(ans)-8:]
            elif code == '110':
                pc_address = int('0b' + numb, 2)
            elif code == '111':
                print(ans[len(ans) - 8:])
                ans = '0b00000'
            if pc_address >= 32:
                print(ans[len(ans) - 8:])
                break


    except:
        break
        #
        # code, numb = line[:3], line[3:]
        # pc_address += 1
        # if code == '000':
        #      memory_dict[numb] = memory_address
        # elif code == '001':
        #     ans = memory_dict[numb]
        # elif code == '010':
        #     if int(memory_address, 2) == 0:
        #         pc_address = int('0b' + numb, 2)
        # elif code == '100':
        #     ans = bin(int(ans, 2) - 1)
        # elif code == '101':
        #     ans = bin(int(ans, 2) + 1)
        #     if len(ans) > 10:
        #         ans = '0b' + ans[len(ans)-8:]
        # elif code == '110':
        #     pc_address = int('0b' + numb, 2)
        # elif code == '111':
        #     print(ans[len(ans) - 8:])
        #     ans = '0b00000'
        # if pc_address >= 32:
        #     print(ans[len(ans) - 8:])
        #     break

