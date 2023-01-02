# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")

for case_num in range(1, int(input()) + 1):
    Field = input()
    print(f"#{Field.count('(') + Field.count(')') - Field.count('()')}")