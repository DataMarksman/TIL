T = int(input())
words = ''
for i in range(T):
    a , b = input().split()
    words = words + a*int(b)

for u in range(0,len(words),9):
    print(words[u:u+9])