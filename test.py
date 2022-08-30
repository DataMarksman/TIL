A, B = tuple(map(int, input().split()))
if A == B:
    print('==')
else:
    print(f'{">" if A > B else "<"}')