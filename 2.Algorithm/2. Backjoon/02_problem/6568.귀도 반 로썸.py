# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
memory_dict = {}
memory_address = bin(0)
pc_address = 0
ans = bin(0)
for command in range(32):
    line = input()
    code, numb = line[:3], line[3:]
    pc_address += 1
    if code == '000':
         memory_dict[numb] = memory_address
    elif code == '001':
        ans = memory_dict[numb]
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
        for dumping in range(command+1, 32):
            input()
        break
    if pc_address >= 32:
        for dumping in range(command+1, 32):
            input()
        break
print(ans[len(ans)-8:])
