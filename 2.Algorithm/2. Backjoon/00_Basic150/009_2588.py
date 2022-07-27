A = int(input())
B = map(int,input())
C = []
for num in B:
    C += int(num)*A

print(C[2])
print(C[1])
print(C[0])
print(C[2]+10*C[1]+100*C[0])