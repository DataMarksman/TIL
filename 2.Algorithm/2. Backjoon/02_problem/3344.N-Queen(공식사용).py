# 3344. N-Queen
# 재귀? 안된다. while? 안된다. 비트? 이것마저 안된다...
# 답은 공식 대입 뿐...

N = int(input())
even_list = [2*i for i in range(1, (N//2)+1)]
odd_list = [2*j+1 for j in range((N+1)//2)]
print(odd_list)
print(even_list)
check = N % 6
if check != 2 and check != 3:
    ans_list = odd_list + even_list
    print(*ans_list, sep='\n')
elif check == 2:
    odd_list[0], odd_list[1] = odd_list[1],odd_list[0]
    odd_list.remove(5)
    odd_list.append(5)
    ans_list = even_list + odd_list
    print(*ans_list, sep='\n')
elif check == 3:
    even_list.remove(2)
    even_list.append(2)
    odd_list.remove(1)
    odd_list.remove(3)
    odd_list.append(1)
    odd_list.append(3)
    ans_list = even_list + odd_list
    print(*ans_list, sep='\n')


"""
<N-Queen Rule>
1. If the remainder from dividing n by 6 is not 2 or 3 
    then the list is simply all even numbers followed by all odd numbers not greater than n.
2. Otherwise, write separate lists of even and odd numbers (2, 4, 6, 8 – 1, 3, 5, 7).
3. If the remainder is 2, swap 1 and 3 in odd list and move 5 to the end (3, 1, 7, 5).
4. If the remainder is 3, move 2 to the end of even list and 1,3 to the end of odd list (4, 6, 8, 2 – 5, 7, 1, 3).
"""
