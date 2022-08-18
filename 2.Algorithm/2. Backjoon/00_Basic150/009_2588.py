A = int(input())
B = list(map(int,input()))
C = []


for i in range(len(B)):
    C += [int(B[i])*A]

print(C[2])
print(C[1])
print(C[0])
print(C[2]+10*C[1]+100*C[0])