# BOJ. 1043 거짓말
# 설계 의도:
# 1. 처음에 값을 받을때, 1차 체크를 하자. 진실을 알고 있는 사람들이 속한 집단은 해체해서 Truth_set에 저장한다.
# 2. 이렇게 set()에 저장되면, 중복이 제거되며, 이 set의 인자들이 판별의 도구가 된다.
# 3. 1차로 걸렀던 거름망에서 살아남은 아이들을 "List"에 저장한다. List다. Set으로 하면 안된다! 가능하긴 한데 귀찮아진다!
# 4. while에 조건을 두개 부여하고 반복을 돌린다.
#     - 4.1: 게스트 리스트의 소진 = 거짓말 할 수 있는 파티가 없다.
#     - 4.2: flag의 True 반환 실패 = 남은 파티들 중에 진실을 아는 사람들이 참가하는 파티가 없다.
# 5. flag는 진실을 아는 조합이 끼어있을 때만 작동하기 때문에, 이것이 True로 변화하지 않았다는 것은 반복문을 멈춰야 할 때를 의미한다.
# 개선점:
# 1. 야!!!! 게스트는 같은 놈들이 계속 올수도 있잖아!!!! 그걸 Set으로 받을 생각을 하면 어떡하냐!!!

N, M = tuple(input().split())
truth_list = list(map(int, input().split()))
truth_set = set()
if truth_list[0]:
    true_teller = set(truth_list[1:])
    truth_set |= true_teller
guest_list = []
for party in range(int(M)):
    lines = list(map(int, input().split()))
    realist = set(lines[1:])
    if realist & truth_set:
        truth_set |= realist
    else:
        guest_list.append(list(realist))

flag = True
while guest_list and flag:
    flag = False
    size = len(guest_list)
    new_guest_list = []
    for checking in range(size):
        lie_real = set(guest_list.pop())
        if lie_real & truth_set:
            truth_set |= set(lie_real)
            flag = True
        else:
            new_guest_list.append(list(lie_real))
    else:
        guest_list = new_guest_list[:]
print(len(guest_list))
