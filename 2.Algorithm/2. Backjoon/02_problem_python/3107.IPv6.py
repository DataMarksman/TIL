# BOJ. 3107 IPv6
# 설계 의도: 스트링 기법
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')


IP_list = list(input().split(':'))
for check in range(len(IP_list)):
    if IP_list[check] == '' and check == 0:
        IP_list[check] = '0000'
    elif IP_list[check] == '' and check == len(IP_list)-1:
        IP_list[check] = '0000'
    elif IP_list[check] == '':
        IP_list[check] = '0000'*(9-len(IP_list))
    elif 0 < len(IP_list[check]) < 4:
        IP_list[check] = '0'*(4-len(IP_list[check]))+IP_list[check]

IP_list = ''.join(IP_list)
ans = ''
for printing in range(7):
    ans += IP_list[printing*4:(printing*4)+4] + ':'
ans += IP_list[28:]
print(ans[:39])
