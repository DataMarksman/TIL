# BOJ. 2866. 문자열 잘라내기
# 설계 의도: 확인하면서 잘라주기
# 개선점:
# 약간 느리다?
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N, M = map(int, input().split())
dump_list = input()
str_list = [input() for _ in range(N-1)]
str_list = list(map(list, zip(*str_list)))
ans = 0
flag = True
temp_set = set()
for first_check in range(M):
    str_list[first_check] = ''.join(str_list[first_check])
    if str_list[first_check] in temp_set:
        flag = False
        break
    else:
        temp_set.add(str_list[first_check])
while flag and len(str_list):
    if flag:
        ans += 1
    temp_set = set()
    for check in range(M):
        str_list[check] = str_list[check][1:]
        if str_list[check] in temp_set:
            flag = False
            break
        else:
            temp_set.add(str_list[check])
print(ans)